import random
import string

import pytest

from pages.jsonplaceholder import Posts


class Test:
    random_post_id = random.choices(Posts().get_all_posts().json())[0].get('id')
    test_data_update_field = [
        ('title', ''.join(random.choices(string.ascii_letters, k=10))),
        ('body', ''.join(random.choices(string.ascii_letters, k=100))),
        ('userid', random.randrange(1, 100, 1))
    ]

    def test_get_all_posts(self):
        response = Posts().get_all_posts()

        assert response.json() \
               and response.status_code == 200 \
               and response.reason == 'OK'

    @pytest.mark.parametrize("post_id", [random_post_id])
    def test_get_post(self, post_id):
        response = Posts().get_post(str(post_id))

        assert response.status_code == 200 \
               and response.reason == 'OK'

        assert response.json().get('id') == post_id

    @pytest.mark.parametrize("post_id", [random_post_id])
    def test_get_post_comments(self, post_id):
        response = Posts().get_post_comments(str(post_id))

        assert response.status_code == 200 \
               and response.reason == 'OK'

        assert response.json() \
               and response.json()[0].get('postId') == post_id

    def test_create_post(self):
        title = ''.join(random.choices(string.ascii_letters, k=10))
        body = ''.join(random.choices(string.ascii_letters, k=100))
        userid = random.randrange(1, 100, 1)

        post = Posts().post_posts(title=title, body=body, userid=userid)

        assert post.status_code == 201
        assert post.json().get('userId') == str(userid)
        assert post.json().get('title') == title
        assert post.json().get('body') == body

    def test_update_post(self):
        post_id = random.randrange(1, 100, 1)
        title = ''.join(random.choices(string.ascii_letters, k=10))
        body = ''.join(random.choices(string.ascii_letters, k=100))
        userid = random.randrange(1, 100, 1)

        put = Posts().put_posts(post_id=post_id, title=title, body=body, userid=userid)

        assert put.status_code == 200
        assert put.json().get('userId') == str(userid)
        assert put.json().get('title') == title
        assert put.json().get('body') == body

    @pytest.mark.parametrize("key, value", test_data_update_field)
    def test_update_field_post(self, key, value):
        post_id = random.randrange(1, 100, 1)

        patch = Posts().patch_posts(post_id=post_id, data={key: value})

        assert patch.status_code == 200
        assert patch.json().get(key) == str(value)

    @pytest.mark.parametrize("post_id", [random_post_id])
    def test_delete_post(self, post_id):
        response = Posts().del_post(str(post_id))

        assert response.status_code == 200 \
               and response.reason == 'OK'

