from src.api_services_classes import *


def test_get_vacancies():
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies('Python')
    assert type(hh_vacancies) is dict
    assert len(hh_vacancies) != 0
