import random

import pytest

from models import dog_ceo_models
from pages.dogceo import AllDogs, RandomImage, ByBreed, SubBreed


class TestValidate:
    data_single_image = dict(
        single_random_image=RandomImage().get_single_random_image(),
        single_random_image_breed=ByBreed().get_single_random_image_breed('akita'),
        single_random_image_sub_breed=SubBreed().get_single_random_image_sub_breed('hound', 'english')
    )

    data_multiple_image = dict(
        multiple_random_image=RandomImage().get_multiple_random_image(random.randint(1, 10)),
        all_images_breed=ByBreed().get_all_images_breed('labrador'),
        multiple_random_image_breed=ByBreed().get_multiple_random_image_breed('pinscher', random.randint(1, 10)),
        all_sub_breeds_images=SubBreed().get_all_sub_breeds_images('mountain', 'swiss'),
        multiple_random_image_sub_breed=SubBreed().get_multiple_random_image_sub_breed('spaniel',
                                                                                       'cocker',
                                                                                       random.randint(1, 10))

    )

    @pytest.mark.parametrize("response",
                             data_single_image.values(),
                             ids=list(data_single_image.keys()))
    def test_validate_single_image(self, response):
        assert dog_ceo_models.ModelSingleImage.parse_obj(response.json())

    @pytest.mark.parametrize("response",
                             data_multiple_image.values(),
                             ids=list(data_multiple_image.keys()))
    def test_validate_multiple_image(self, response):
        assert dog_ceo_models.ModelMultipleImage.parse_obj(response.json())

    def test_validate_list_all_json(self):
        response = AllDogs().get_all_dogs().json()

        assert dog_ceo_models.ModelAllBreeds.parse_obj(response)

    @pytest.mark.parametrize("breed", ['bulldog', 'frise', 'hound'])
    def test_validate_breed_list(self, breed):
        response = SubBreed().get_all_sub_breeds(breed).json()

        assert dog_ceo_models.ModelBreedList.parse_obj(response)


class TestStatus:
    test_data_response = dict(
        all_dogs=AllDogs().get_all_dogs(),
        all_sub_breeds=SubBreed().get_all_sub_breeds('whippet'),
        single_random_image=RandomImage().get_single_random_image(),
        single_random_image_breed=ByBreed().get_single_random_image_breed('pinscher'),
        single_random_image_sub_breed=SubBreed().get_single_random_image_sub_breed('sheepdog', 'english'),
        multiple_random_image=RandomImage().get_multiple_random_image(random.randint(1, 10)),
        all_images_breed=ByBreed().get_all_images_breed('tervuren'),
        multiple_random_image_breed=ByBreed().get_multiple_random_image_breed('terrier', random.randint(1, 10)),
        all_sub_breeds_images=SubBreed().get_all_sub_breeds_images('mountain', 'swiss'),
        multiple_random_image_sub_breed=SubBreed().get_multiple_random_image_sub_breed('poodle',
                                                                                       'standard',
                                                                                       random.randint(1, 10))
    )

    @pytest.mark.parametrize("response",
                             test_data_response.values(),
                             ids=list(test_data_response.keys()))
    def test_status_code_is_200(self, response):
        assert response.status_code == 200, response.status_code

    @pytest.mark.parametrize("response",
                             test_data_response.values(),
                             ids=list(test_data_response.keys()))
    def test_status_in_response(self, response):
        status = response.json().get('status')
        assert status == 'success', status
