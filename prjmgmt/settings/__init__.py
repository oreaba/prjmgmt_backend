"""
created by eng.Mohamed Hamdy
M.Sc Computer Science, AUC
mhamdy@aucegypt.edu
"""


from .base import *
# you need to set "SYNDO_CONF = 'prod' as an environment variable
# in your OS (on which your website is hosted)

if ADM_PM_ENV == EnvType.LOCAL:
    from .local import *
elif ADM_PM_ENV == EnvType.PRODUCTION:
    from .prod import *
else:
    pass #you can load staging if you want

# if os.environ['SYNDO_CONF']     == 'prod':
#     from .prod import *
# elif os.environ['SYNDO_CONF']   == 'dev':
# elif os.environ['SYNDO_CONF']   == 'stg':
#     from .dev import *
# elif os.environ['SYNDO_CONF']   == 'loc':
#     from .dev import *