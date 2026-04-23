import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # --- YOUR Blob Storage Configuration ---
    # Using your AccountName: cmsimages1
    BLOB_ACCOUNT = "cmsimages1"
    BLOB_STORAGE_KEY = "GXgNYFobRd80M4VFxs8Rpmna/AP7CLBkxEpbOdLlRsrKiKqCygm8BYL4vu6KlEow6jEvGeTMANXU+ASt2kbV8Q=="
    BLOB_CONTAINER = "images"
    
    # Keeping your friend's connection string format but with YOUR key/name
    BLOB_CONNECTION_STRING = f"DefaultEndpointsProtocol=https;AccountName={BLOB_ACCOUNT};AccountKey={BLOB_STORAGE_KEY};EndpointSuffix=core.windows.net"

    # --- YOUR Azure SQL Database Configuration ---
    SQL_SERVER = "cms-server-12.database.windows.net"
    SQL_DATABASE = "cms"
    SQL_USER_NAME = "cmsadmin"
    SQL_PASSWORD = r'M@ss@@@786' # Using 'r' to protect the @ symbols
    
    # URL-encoding the password is REQUIRED because of the '@' symbols
    encoded_password = quote_plus(SQL_PASSWORD)

    # Finalized Connection String using your friend's port 1433 trick
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{encoded_password}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&TrustServerCertificate=no"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- YOUR MS Authentication (Entra ID) ---
    # Using your Client ID: b0aa7bed...
    CLIENT_ID = "b0aa7bed-08a1-4cd3-8f30-1dcc23610899"
    CLIENT_SECRET = "J.N8Q~B36P1BTmRFTC2GMlZqh2ow58HKcDeOrbtS"
    
    # Using your Tenant ID from your screenshot (Default Directory)
    TENANT_ID = "dfea0168-ba77-4a17-99c3-03898e023df2"
    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"