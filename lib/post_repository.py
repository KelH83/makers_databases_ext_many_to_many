from lib.post import Post

class PostRepository:

    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"])
            posts.append(item)
        return posts

