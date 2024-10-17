from lib.post_repository import PostRepository
from lib.post import Post


def test_get_all_records(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    posts = repository.all() 

    assert posts == [
        Post(1,'How to use Git'),
        Post(2,'Python classes'),
        Post(3,'Using a REPL'),   
        Post(4,'My weekend in Edinburgh'),
        Post(5,'The best chocolate cake EVER'),
        Post(6,'A foodie week in Spain'),
        Post(7,'SQL basics')
    ]

def test_find_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    tags = repository.find_by_post(2)
    assert tags == Post(2,"Python classes",["coding","education"])
