import requests


class Jlaceholder:

    def __init__(self):
        self.URL = 'https://jsonplaceholder.typicode.com'


class Posts(Jlaceholder):

    def get_all_posts(self):
        path = '/posts'

        return requests.request("GET", self.URL + path)

    def get_post(self, post_id):
        path = f'/posts/{str(post_id)}'

        return requests.request("GET", self.URL + path)

    def get_post_comments(self, post_id):
        path = f'/posts/{str(post_id)}/comments'

        return requests.request("GET", self.URL + path)

    def post_posts(self, title, body, userid):
        path = '/posts'

        data = dict(
            title=title,
            body=body,
            userId=userid,
        )

        return requests.request("POST", self.URL + path, data=data)

    def put_posts(self, post_id,  title, body, userid):
        path = f'/posts/{str(post_id)}'

        data = dict(
            title=title,
            body=body,
            userId=userid,
        )

        return requests.request("PUT", self.URL + path, data=data)

    def patch_posts(self, post_id,  data):
        path = f'/posts/{str(post_id)}'

        return requests.request("PATCH", self.URL + path, data=data)


    def del_post(self, post_id):
        path = f'/posts/{str(post_id)}'

        return requests.request("DELETE", self.URL + path)

