import requests


class DogCeo:

    def __init__(self):
        self.URL = 'https://dog.ceo/'


class AllDogs(DogCeo):

    def get_all_dogs(self):
        path = 'api/breeds/list/all'

        return requests.request("GET", self.URL + path)


class RandomImage(DogCeo):

    def get_single_random_image(self):
        path = 'api/breeds/image/random'

        return requests.request("GET", self.URL + path)

    def get_multiple_random_image(self, image_count):
        path = f'api/breeds/image/random/{image_count}'

        return requests.request("GET", self.URL + path)


class ByBreed(DogCeo):

    def get_all_images_breed(self, breed):
        path = f'api/breed/{breed}/images'

        return requests.request("GET", self.URL + path)

    def get_single_random_image_breed(self, breed):
        path = f'api/breed/{breed}/images/random'

        return requests.request("GET", self.URL + path)

    def get_multiple_random_image_breed(self, breed, image_count):
        path = f'api/breed/{breed}/images/random/{image_count}'

        return requests.request("GET", self.URL + path)


class SubBreed(DogCeo):

    def get_all_sub_breeds(self, breed):
        path = f'api/breed/{breed}/list'

        return requests.request("GET", self.URL + path)

    def get_all_sub_breeds_images(self, breed, sub_breed):
        path = f'api/breed/{breed}/{sub_breed}/images'

        return requests.request("GET", self.URL + path)

    def get_single_random_image_sub_breed(self, breed, sub_breed):
        path = f'api/breed/{breed}/{sub_breed}/images/random'

        return requests.request("GET", self.URL + path)

    def get_multiple_random_image_sub_breed(self, breed, sub_breed, image_count):
        path = f'api/breed/{breed}/{sub_breed}/images/random/{image_count}'

        return requests.request("GET", self.URL + path)
