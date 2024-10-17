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
    
    def find_by_post(self, post_id):
        rows = self._connection.execute(
            'SELECT posts.id, posts.title, tags.name FROM tags JOIN posts_tags ON posts_tags.tag_id = tags.id JOIN posts ON posts_tags.post_id = posts.id WHERE posts.id = %s',[post_id])
        row = rows[0]
        tags = []
    
        for row in rows:
            tags.append(row["name"])

        if rows:
            first_row = rows[0]
            return Post(first_row["id"], first_row["title"], tags)

