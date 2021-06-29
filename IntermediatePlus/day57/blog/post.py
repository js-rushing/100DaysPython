import requests


class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/8615618024037d9a88ac"
        self.posts = requests.get(self.url).json()
