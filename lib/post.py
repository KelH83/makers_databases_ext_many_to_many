class Post:
    def __init__(self, id, title, tags = []):
        self.id = id
        self.title = title
        self.tags = tags

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Title:{self.title}, Post ID:{self.id}"
