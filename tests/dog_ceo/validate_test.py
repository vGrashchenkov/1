import random

import pytest

from models.dog_ceo import dog_ceo_models
from pages.dog_ceo.dog_ceo import All_dogs, Random_image, By_breed, Sub_breed


class TestValidate:
    data_single_image = dict(
        single_random_image=Random_image().get_single_random_image(),
        single_random_image_breed=By_breed().get_single_random_image_breed('akita'),
        single_random_image_sub_breed=Sub_breed().get_single_random_image_sub_breed('hound', 'english')
    )

    data_multiple_image = dict(
        multiple_random_image=Random_image().get_multiple_random_image(random.randint(1, 10)),
        all_images_breed=By_breed().get_all_images_breed('labrador'),
        multiple_random_image_breed=By_breed().get_multiple_random_image_breed('pinscher', random.randint(1, 10)),
        all_sub_breeds_images=Sub_breed().get_all_sub_breeds_images('mountain', 'swiss'),
        multiple_random_image_sub_breed=Sub_breed().get_multiple_random_image_sub_breed('spaniel',
                                                                                        'cocker',
                                                                                        random.randint(1, 10))

    )

    @pytest.mark.parametrize("response",
                             data_single_image.values(),
                             ids=list(data_single_image.keys()))
    def test_validate_single_image(self, response):
        assert dog_ceo_models.Model_single_image.parse_obj(response.json())

    @pytest.mark.parametrize("response",
                             data_multiple_image.values(),
                             ids=list(data_multiple_image.keys()))
    def test_validate_multiple_image(self, response):
        assert dog_ceo_models.Model_multiple_image.parse_obj(response.json())

    def test_validate_list_all_json(self):
        response = All_dogs().get_all_dogs().json()

        assert dog_ceo_models.Model_all_breeds.parse_obj(response)

    @pytest.mark.parametrize("breed", ['bulldog', 'frise', 'hound'])
    def test_validate_breed_list(self, breed):
        response = Sub_breed().get_all_sub_breeds(breed).json()

        assert dog_ceo_models.Model_breed_list.parse_obj(response)
