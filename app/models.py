#in memory data-models


#stores user credentials
# Format : { 'username': hashed_password }
users_dict = {}


# stores user blog posts
# Format : { "username : [ { "title": ... , "content": ... }, ...] }
posts_dict = {}