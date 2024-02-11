import requests
import json
from abc import ABC, abstractmethod
from config import *


class APIServices(ABC):
    @abstractmethod
    def get_vacancies(self, vacancy_name):
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


class Vacancy:
    def __init__(self, name, url, area, requirement, min_pay, max_pay, currency):
        self.name = name
        self.url = url
        self.min_pay = min_pay
        self.max_pay = max_pay
        self.area = area
        self.requirement = requirement
        self.currency = currency
        if self.requirement is None:
            self.requirement = ''

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

    @staticmethod
    def filter_vacancies(vacancies_list, filter_words):
        filtered_vacancies = []
        formated_filter_words = Vacancy.get_format_list(filter_words)
        for vacancy in vacancies_list:
            vacancy_words = f'{vacancy.area.lower()} {vacancy.name.lower()} {vacancy.requirement.lower()}'
            formated_vacancies_list = Vacancy.get_format_list(vacancy_words)
            if set(formated_filter_words).issubset(formated_vacancies_list):
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    @staticmethod
    def get_format_list(data_to_format):
        alpha_str = ''
        for symbol in data_to_format:
            if symbol.isalpha() or symbol == ' ':
                alpha_str += symbol
            else:
                alpha_str += ' '
        alpha_list = alpha_str.split(' ')
        result_list = []
        for word in alpha_list:
            if word != '':
                result_list.append(word)
        return result_list


class Saver(ABC):
    def add_vacancy(self, data):
        pass

    def delete_vacancy(self, data):
        pass


class JSONSaver(Saver):
    def add_vacancy(self, data):
        vacancies_list_for_json = []
        for item in data:
            vacancy_dict = {}
            vacancy_dict['name'] = item.name
            vacancy_dict['url'] = item.url
            vacancy_dict['area'] = item.area
            vacancy_dict['requirement'] = item.requirement
            vacancy_dict['min_pay'] = item.min_pay
            vacancy_dict['max_pay'] = item.max_pay
            vacancy_dict['currency'] = item.currency
            vacancies_list_for_json.append(vacancy_dict)

        with open(VACANCY_JSON, 'w') as file:
            json.dump(vacancies_list_for_json, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, data):
        pass
