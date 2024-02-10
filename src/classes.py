import requests
import json
from abc import ABC, abstractmethod
from config import *


class APIServices(ABC):
    @abstractmethod
    def get_vacancies(self, vacancie_name):
        pass


class HeadHunterAPI(APIServices):
    def get_vacancies(self, vacancie_name):
        params = {
            'text': vacancie_name,  # Текст фильтра. В имени должно быть слово "Аналитик"
            'area': 113,  # Поиск ощуществляется по вакансиям города Москва
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        json_data = json.loads(data)
        return json_data


class Vacancy:
    def __init__(self, name, url, area, requirement, min_pay, max_pay, currency):
        self.name = name
        self.url = url
        self.min_pay = min_pay
        self.max_pay = max_pay
        self.area = area
        self.requirement = requirement
        self.currency = currency

    def __str__(self):
        if self.min_pay == 0 and self.max_pay == 0:
            return f'{self.name}, зарплата не указана, в {self.area}'
        elif self.min_pay is None:
            return f'{self.name}, зарплата до {self.max_pay} {self.currency}, в {self.area}'
        elif self.max_pay is None:
            return f'{self.name}, зарплата от {self.min_pay} {self.currency}, в {self.area}'
        else:
            return f'{self.name}, зарплата: {self.min_pay} - {self.max_pay} {self.currency}, в {self.area}'

    def __repr__(self):
        if self.min_pay == 0 and self.max_pay == 0:
            return f'{self.name}, зарплата не указана, в {self.area}'
        elif self.min_pay is None:
            return f'{self.name}, зарплата до {self.max_pay} {self.currency}, в {self.area}'
        elif self.max_pay is None:
            return f'{self.name}, зарплата от {self.min_pay} {self.currency}, в {self.area}'
        else:
            return f'{self.name}, зарплата: {self.min_pay} - {self.max_pay} {self.currency}, в {self.area}'

    def __le__(self, other):
        result = self.min_pay <= other.min_pay
        return result

    def __ge__(self, other):
        result = self.max_pay >= other.max_pay
        return result

    @staticmethod
    def cast_to_object_list(data):
        vacancies_list = []
        for item in data['items']:
            if item['salary'] is None:
                item['salary'] = {'from': 0, 'to': 0, 'currency': ''}
            vacancies_list.append(
                Vacancy(item['name'], item['url'], item['area']['name'], item['snippet']['requirement'],
                        item['salary']['from'], item['salary']['to'], item['salary']['currency']))
        return vacancies_list


class Saver(ABC):
    @staticmethod
    def add_vacancy(data):
        pass

    def delete_vacancy(self, data):
        pass


class JSONSaver(Saver):
    @staticmethod
    def add_vacancy(data):
        vacancy_dict = {}
        with open(VACANCY_JSON, 'w', encoding='UTF-8') as file:
            for item in data:
                vacancy_dict['name'] = item.name
                vacancy_dict['url'] = item.url
                vacancy_dict['area'] = item.area
                vacancy_dict['requirement'] = item.requirement
                vacancy_dict['min_pay'] = item.min_pay
                vacancy_dict['max_pay'] = item.max_pay
                vacancy_dict['currency'] = item.currency
                json.dump(vacancy_dict, file, indent=1)
