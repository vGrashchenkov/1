import random

import pytest

from models.dog_ceo import dog_ceo_models
from pages.dog_ceo.dog_ceo import All_dogs, Random_image, By_breed, Sub_breed


class TestValidate:

    def test_validate_list_all_json(self):
        response = All_dogs().get_all_dogs().json()

        assert dog_ceo_models.Model_all_breeds.parse_obj(response)

    def test_validate_single_random_image_json(self):
        response = Random_image().get_single_random_image().json()

        assert dog_ceo_models.Model_single_image.parse_obj(response)

    @pytest.mark.parametrize("image_count", [random.randint(1, 10)])
    def test_validate_multiple_random_image_json(self, image_count):
        response = Random_image().get_multiple_random_image(image_count).json()

        assert dog_ceo_models.Model_multiple_image.parse_obj(response)

    @pytest.mark.parametrize("breed", ['akita'])  # переписать на фикстуру
    def test_validate_all_images_breed_json(self, breed):
        response = By_breed().get_all_images_breed(breed).json()

        assert dog_ceo_models.Model_multiple_image.parse_obj(response)

    @pytest.mark.parametrize("breed", ['akita'])  # переписать на фикстуру
    def test_validate_single_random_image_breed_json(self, breed):
        response = By_breed().get_single_random_image_breed(breed).json()

        assert dog_ceo_models.Model_single_image.parse_obj(response)

    @pytest.mark.parametrize("breed, image_count", [('akita', random.randint(1, 10))])  # переписать на фикстуру
    def test_validate_multiple_random_image_breed_json(self, breed, image_count):
        response = By_breed().get_multiple_random_image_breed(breed, image_count).json()

        assert dog_ceo_models.Model_multiple_image.parse_obj(response)

    @pytest.mark.parametrize("breed", ['schnauzer'])  # переписать на фикстуру
    def test_validate_all_sub_breeds_json(self, breed):
        response = Sub_breed().get_all_sub_breeds(breed).json()

        assert dog_ceo_models.Model_breed_list.parse_obj(response)

    @pytest.mark.parametrize("breed, sub_breed", [('schnauzer', 'giant')])  # переписать на фикстуру
    def test_validate_all_sub_breeds_images_json(self, breed, sub_breed):
        response = Sub_breed().get_all_sub_breeds_images(breed, sub_breed).json()

        assert dog_ceo_models.Model_multiple_image.parse_obj(response)

    @pytest.mark.parametrize("breed, sub_breed", [('schnauzer', 'giant')])  # переписать на фикстуру
    def test_validate_single_random_image_sub_breed_json(self, breed, sub_breed):
        response = Sub_breed().get_single_random_image_sub_breed(breed, sub_breed).json()

        assert dog_ceo_models.Model_single_image.parse_obj(response)

    @pytest.mark.parametrize("breed, sub_breed, image_count", [('schnauzer', 'giant', random.randint(1, 10))])  # переписать на фикстуру
    def test_validate_multiple_random_image_sub_breed_json(self, breed, sub_breed, image_count):
        response = Sub_breed().get_multiple_random_image_sub_breed(breed, sub_breed, image_count).json()

        assert dog_ceo_models.Model_multiple_image.parse_obj(response)