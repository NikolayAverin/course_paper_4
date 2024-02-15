import json
import csv
from abc import ABC
from config import *


class Saver(ABC):
    def add_vacancy(self, data):
        """Метод, сохраняющий вакансии в файл"""
        pass

    def delete_vacancy(self, data):
        """Метод, удаляющий вакансии из файла"""
        pass


class JSONSaver(Saver):
    def add_vacancy(self, data):
        vacancies_list_for_json = []
        for item in data:
            vacancy_dict = dict()
            vacancy_dict['name'] = item.name
            vacancy_dict['area'] = item.area
            vacancy_dict['requirement'] = item.requirement
            vacancy_dict['min_pay'] = item.min_pay
            vacancy_dict['max_pay'] = item.max_pay
            vacancy_dict['currency'] = item.currency
            vacancy_dict['url'] = item.url
            vacancies_list_for_json.append(vacancy_dict)

        with open(VACANCY_JSON, 'w') as file:
            json.dump(vacancies_list_for_json, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, data):
        pass


class CSVSaver(Saver):
    def add_vacancy(self, data):
        vacancies_list_for_csv = []
        for item in data:
            vacancy_dict = dict()
            vacancy_dict['name'] = item.name
            vacancy_dict['area'] = item.area
            vacancy_dict['requirement'] = item.requirement
            vacancy_dict['min_pay'] = item.min_pay
            vacancy_dict['max_pay'] = item.max_pay
            vacancy_dict['currency'] = item.currency
            vacancy_dict['url'] = item.url
            vacancies_list_for_csv.append(vacancy_dict)

        with open(VACANCY_CSV, 'w', newline='') as file:
            fc = csv.DictWriter(file, fieldnames=vacancies_list_for_csv[0].keys())
            fc.writeheader()
            fc.writerows(vacancies_list_for_csv)

    def delete_vacancy(self, data):
        pass


class TXTSaver(Saver):
    def add_vacancy(self, data):
        vacancies_list_for_txt = []
        for item in data:
            vacancies_list_for_txt.append(item)

        with open(VACANCY_TXT, 'w', encoding='UTF-8') as file:
            for vacancy in vacancies_list_for_txt:
                file.write(f'{str(vacancy)}\n')

    def delete_vacancy(self, data):
        pass
