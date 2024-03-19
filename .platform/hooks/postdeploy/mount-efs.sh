#!/bin/bash
echo 'installing efs-utils...'
yum -y install amazon-efs-utils
echo 'Done.'

# the below variables are fetched from environment variables
# EFS_MOUNT_DIR='/efs-adm-pm-db'
# EFS_FILE_SYSTEM_ID='fs-0f3e8f95d2a818694'

echo "Mounting EFS filesystem ${EFS_FILE_SYSTEM_ID} to directory ${EFS_MOUNT_DIR} ..."

echo 'Stopping NFS ID Mapper...'
service rpcidmapd status &> /dev/null
if [ $? -ne 0 ] ; then
    echo 'rpc.idmapd is already stopped!'
else
    service rpcidmapd stop
    if [ $? -ne 0 ] ; then
        echo 'ERROR: Failed to stop NFS ID Mapper!'
        exit 1
    fi
fi

echo 'Checking if EFS mount directory exists...'
if [ ! -d ${EFS_MOUNT_DIR} ]; then
    echo "Creating directory ${EFS_MOUNT_DIR} ..."
    mkdir -p ${EFS_MOUNT_DIR}
    if [ $? -ne 0 ]; then
        echo 'ERROR: Directory creation failed!'
        exit 1
    fi
else
    echo "Directory ${EFS_MOUNT_DIR} already exists!"
fi

mountpoint -q ${EFS_MOUNT_DIR}
if [ $? -ne 0 ]; then
    echo "mount -t efs -o tls ${EFS_FILE_SYSTEM_ID}:/ ${EFS_MOUNT_DIR}"
    mount -t efs -o tls ${EFS_FILE_SYSTEM_ID}:/ ${EFS_MOUNT_DIR}
    if [ $? -ne 0 ] ; then
        echo 'ERROR: Mount command failed!'
        exit 1
    fi
    chmod 777 ${EFS_MOUNT_DIR}
    runuser -l  ec2-user -c "touch ${EFS_MOUNT_DIR}/it_works"
    if [[ $? -ne 0 ]]; then
        echo 'ERROR: Permission Error!'
        exit 1
    else
        runuser -l  ec2-user -c "rm -f ${EFS_MOUNT_DIR}/it_works"
    fi
else
    echo "Directory ${EFS_MOUNT_DIR} is already a valid mountpoint!"
fi
echo 'EFS mount complete.'


echo "Applyging migrations and creating a new superuser"
source /var/app/venv/*/bin/activate
cd /var/app/current/
python manage.py makemigrations < <(yes y) && python manage.py migrate
python manage.py loaddata fixtures/*.json
python manage.py collectstatic < <(yes yes)
sudo chmod 777 ${EFS_MOUNT_DIR}/adm-pm.db.sqlite3
# python manage.py mysuperuser
# sudo chmod 777 ${EFS_MOUNT_DIR}/adm-pm.db.sqlite3