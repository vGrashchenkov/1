import random

import pytest

from models.dog_ceo import dog_ceo_models
from pages.dog_ceo.dog_ceo import All_dogs, Random_image, By_breed, Sub_breed


class TestStatus:
    data_response = dict(
        all_dogs=All_dogs().get_all_dogs(),
        all_sub_breeds=Sub_breed().get_all_sub_breeds('whippet'),
        single_random_image=Random_image().get_single_random_image(),
        single_random_image_breed=By_breed().get_single_random_image_breed('pinscher'),
        single_random_image_sub_breed=Sub_breed().get_single_random_image_sub_breed('sheepdog', 'english'),
        multiple_random_image=Random_image().get_multiple_random_image(random.randint(1, 10)),
        all_images_breed=By_breed().get_all_images_breed('tervuren'),
        multiple_random_image_breed=By_breed().get_multiple_random_image_breed('terrier', random.randint(1, 10)),
        all_sub_breeds_images=Sub_breed().get_all_sub_breeds_images('mountain', 'swiss'),
        multiple_random_image_sub_breed=Sub_breed().get_multiple_random_image_sub_breed('poodle',
                                                                                        'standard',
                                                                                        random.randint(1, 10))
    )

    @pytest.mark.parametrize("response",
                             data_response.values(),
                             ids=list(data_response.keys()))
    def test_status_code_is_200(self, response):
        assert response.status_code == 200, response.status_code

    @pytest.mark.parametrize("response",
                             data_response.values(),
                             ids=list(data_response.keys()))
    def test_status_in_response(self, response):
        status = response.json().get('status')
        assert status == 'success', status
