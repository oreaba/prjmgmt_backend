from ldap3 import Server, Connection
from ldap3.core.exceptions import LDAPSocketOpenError, LDAPBindError
def login():
    domain = 'adm.local' 
    server = Server(f'ldap://{domain}')
    username = input("Enter username: ")
    username += '@adm.gov.ae'
    password = input("Enter password: ")
    try:
        with Connection(server, user=username, password=password, auto_bind=True) as conn:
            print("welcome ", conn.extend.standard.who_am_i())
    except LDAPSocketOpenError as ex:
        print(f"Can not connect to remote server: {domain}")
    except LDAPBindError as ex:
        print(f"Incorrect Credentials.")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    login()