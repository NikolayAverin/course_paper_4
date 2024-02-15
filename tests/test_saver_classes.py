import json

from src.saver_classes import *
from src.vacansy_class import *
from config import *


def test_add_vacancy():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        None, 100000, 200000, 'RUB')
    vacancies_list = [vacancy_1, vacancy_2]
    txt_saver = TXTSaver()
    txt_saver.add_vacancy(vacancies_list)
    with open(VACANCY_TXT) as file:
        test_txt = file.read()

    assert test_txt == f'{vacancy_1.__str__()}\n{vacancy_2.__str__()}\n'

    csv_saver = CSVSaver()
    csv_saver.add_vacancy(vacancies_list)
    with open(VACANCY_CSV) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        count = 0
        item_all = []
        for row in reader:
            if count == 0:
                count += 1
            else:
                item_all.append(Vacancy(row[0], row[6], row[1], row[2], row[3], row[4], row[5]).__str__())

    assert item_all == [vacancy_1.__str__(), vacancy_2.__str__()]

    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancies_list)
    with open(VACANCY_JSON) as json_file:
        test_json = json.load(json_file)

    assert test_json == [{'area': 'Самара',
                         'currency': 'RUB',
                          'max_pay': 100000,
                          'min_pay': 50000,
                          'name': 'Разработчик',
                          'requirement': 'Нужно уметь всё',
                          'url': 'https://test1.ru'},
                         {'area': 'Самара',
                          'currency': 'RUB',
                          'max_pay': 200000,
                          'min_pay': 100000,
                          'name': 'Разработчик',
                          'requirement': '',
                          'url': 'https://test2.ru'}]
