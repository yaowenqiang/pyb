import os

# ~/.bash_profile

# export DB_USEr=""
# export DB_PASSr=""


db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
print(db_user)
print(db_pass)