from django.test import TestCase
from people.models import People


class PeopleTestCase(TestCase):
    def setUp(self):
        super().setUp()

    def test_people_to_dict(self):
        expected_dict = {
            "people_id": 6,
            "name": "Owen Lars",
            "birth_year": "52BBY",
            "eye_color": "blue",
            "gender": "male",
            "hair_color": "brown, grey",
            "height": 178,
            "mass": 120,
            "skin_color": "light",
            "homeworld": "http://swapi.dev/api/planets/1/"
        }

        p = People(id=2, **expected_dict)
        p_dict = p.to_dict()
        self.assertEqual(p.id, 2)
        self.assertEqual(p_dict, expected_dict)