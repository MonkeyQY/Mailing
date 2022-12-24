# database
import os

from dotenv import load_dotenv

load_dotenv()  #

# # url for OAuth2 google
# sign_in_with_google_url = os.getenv("SIGNING_KEY", 'http://localhost:5000/add/authCode')

# params servers
host = os.getenv("HOST", 'localhost')
port = int(os.getenv("PORT", 5000))

DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', '5432'),
    'username': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PASS', 'postgres'),
    'database': os.environ.get('POSTGRES_DB', 'ListenerNotification')
}


# API prefix
prefix_api = os.getenv("PREFIX_API", '/api/v1')

# API DOCS URL
docs_url = os.getenv("DOCS_URL", '/docs')

# endpoints paths
add_client_path = os.getenv("ADD_CLIENT_PATH", '/client/add')
remove_client_path = os.getenv("REMOVE_CLIENT_PATH", '/client/remove')
update_client_path = os.getenv("UPDATE_CLIENT_PATH", '/client/update')

add_new_mailing_path = os.getenv("ADD_NEW_MAILING_PATH", '/mailing/add')
remove_mailing_path = os.getenv("REMOVE_MAILING_PATH", '/mailing/remove')
update_mailing_path = os.getenv("UPDATE_MAILING_PATH", '/mailing/update')

detail_mailing_path = os.getenv("DETAIL_MAILING_PATH", '/mailing/detail')
total_mailing_path = os.getenv("TOTAL_MAILING_PATH", '/mailing/total')