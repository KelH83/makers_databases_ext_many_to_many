from lib.database_connection import DatabaseConnection
from lib.post_repository import ArtistRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog_posts_tags.sql")

# Retrieve all artists
blog_repository = blogRepository(connection)
blogs = blog_repository.all()

# List them out
for blog in blogs:
    print(blog)
