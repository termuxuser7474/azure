import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Blob storage (we will configure later)

    BLOB_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=images47;AccountKey=vkg1Mu/5tULkZaZb19YJ3BCxMVI4GKQL2PBPQmwvynfy2HlDmP2E7sKVFqf27wjl2i8TI8s3H3oq+AStwvKdrQ==;EndpointSuffix=core.windows.net"
    BLOB_CONTAINER = "images"

    # Azure SQL Database
    SQL_SERVER = "cms-server-123.database.windows.net"
    SQL_DATABASE = "cms"
    SQL_USER_NAME = "cmsadmin"
    SQL_PASSWORD = "CMS4dmin"

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://cmsadmin:CMS4dmin@cms-server-123.database.windows.net:1433/cms"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = "ENTER_CLIENT_SECRET_HERE"
    CLIENT_ID = "ENTER_CLIENT_ID_HERE"

    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"