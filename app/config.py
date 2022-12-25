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
    'database': os.environ.get('POSTGRES_DB', 'Mailing')
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

# URL for send mail on outside service
url_for_send = os.getenv("URL_FOR_SEND", 'localhost')

# JWT token for outside service
jwt_token = os.getenv("JWT_TOKEN_FOR_OUTSIDE_SERVICE")

# email and password for send email
my_email = os.getenv("MY_EMAIL")
my_email_password = os.getenv("MY_EMAIL_PASSWORD")

# smtp server
smtp_server_gmail = os.getenv("SMTP_SERVER_GMAIL", 'smtp.gmail.com')
smtp_port_gmail = os.getenv("SMTP_PORT_GMAIL", 465)

# List users for send statistics
list_users_for_send_statistics = os.getenv("LIST_USERS_FOR_SEND_STATISTICS", [my_email])
