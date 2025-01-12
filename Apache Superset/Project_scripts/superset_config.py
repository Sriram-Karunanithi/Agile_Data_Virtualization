# Superset specific config
ROW_LIMIT = 5000

# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
# and encrypting sensitive information on the database
# Make sure you are changing this key for your deployment with a strong key.
# Alternatively you can set it with `SUPERSET_SECRET_KEY` environment variable.
# You MUST set this for production environments or the server will not refuse
# to start and you will see an error in the logs accordingly.
SECRET_KEY = 'QMvqFk2yf4T9o5E8W0tj/3t3BT9hkV3gd9XGvKaw9oZnKmeaZMZ3AQz1'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
# The check_same_thread=false property ensures the sqlite client does not attempt
# to enforce single-threaded access, which may be problematic in some edge cases
#SQLALCHEMY_DATABASE_URI = 'sqlite:////home/jennadar/Documents/database/ocra.db?check_same_thread=false'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:changeme@localhost:5432/dummy_database'


# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

# superset_config.py

# Set the Superset administrator user
ADMIN_USERNAME = 'admin'
ADMIN_FIRST_NAME = 'Jenny'
ADMIN_LAST_NAME = 'Nadar'
ADMIN_EMAIL = 'jennynadar9@gmail.com'
ADMIN_PASSWORD = 'changeme'

# Specify the security manager, e.g., for authentication
#SECURITY_MANAGER_CLASS = 'superset.security.SupersetSecurityManager'
