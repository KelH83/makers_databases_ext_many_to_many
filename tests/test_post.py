from lib.post import Post

def test_post_constructs():
    post = Post(1, "Test post")
    assert post.id == 1
    assert post.title == "Test post"

def test_posts_format_nicely():
    post = Post(1, "Test post")
    assert str(post) == "Title:Test post, Post ID:1"


