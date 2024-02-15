import requests
import json
from abc import ABC, abstractmethod


class APIServices(ABC):
    @abstractmethod
    def get_vacancies(self, vacancy_name):
        """Метод, получающий список вакансий по переданному значению"""
        pass


class HeadHunterAPI(APIServices):
    def get_vacancies(self, vacancy_name):
        params = {
            'text': vacancy_name,
            'area': 113,
            'per_page': 100
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        json_data = json.loads(data)
        return json_data
