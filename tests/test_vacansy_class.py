from src.vacansy_class import *


def test_init():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        None, None, None, 'RUB')
    assert vacancy_1.name == 'Разработчик'
    assert vacancy_1.url == 'https://test1.ru'
    assert vacancy_1.area == 'Самара'
    assert vacancy_1.requirement == 'Нужно уметь всё'
    assert vacancy_1.min_pay == 50000
    assert vacancy_1.max_pay == 100000
    assert vacancy_1.currency == 'RUB'
    assert vacancy_2.requirement == ''
    assert vacancy_2.min_pay == 0
    assert vacancy_2.max_pay == 0


def test_str():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        None, None, None, 'RUB')
    vacancy_3 = Vacancy('Разработчик', 'https://test3.ru', 'Самара',
                        'Нужно уметь всё', None, 100000, 'RUB')
    vacancy_4 = Vacancy('Разработчик', 'https://test4.ru', 'Самара',
                        None, 50000, None, 'RUB')
    assert vacancy_1.__str__() == 'Разработчик, зарплата: 50000 - 100000 RUB, в Самара, ссылка https://test1.ru'
    assert vacancy_2.__str__() == 'Разработчик, зарплата не указана, в Самара, ссылка https://test2.ru'
    assert vacancy_3.__str__() == 'Разработчик, зарплата до 100000 RUB, в Самара, ссылка https://test3.ru'
    assert vacancy_4.__str__() == 'Разработчик, зарплата от 50000 RUB, в Самара, ссылка https://test4.ru'


def test_repr():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        None, None, None, 'RUB')
    vacancy_3 = Vacancy('Разработчик', 'https://test3.ru', 'Самара',
                        'Нужно уметь всё', None, 100000, 'RUB')
    vacancy_4 = Vacancy('Разработчик', 'https://test4.ru', 'Самара',
                        None, 50000, None, 'RUB')
    assert vacancy_1.__repr__() == 'Разработчик, зарплата: 50000 - 100000 RUB, в Самара, ссылка https://test1.ru'
    assert vacancy_2.__repr__() == 'Разработчик, зарплата не указана, в Самара, ссылка https://test2.ru'
    assert vacancy_3.__repr__() == 'Разработчик, зарплата до 100000 RUB, в Самара, ссылка https://test3.ru'
    assert vacancy_4.__repr__() == 'Разработчик, зарплата от 50000 RUB, в Самара, ссылка https://test4.ru'


def test_lt():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        'Нужно уметь всё', 70000, 150000, 'RUB')
    assert vacancy_1.__lt__(vacancy_2) is True


def test_cast_to_object_list():
    vacancies_dict = {'items': [{'name': 'Build Engineer (Tanks Blitz)', 'area': {'name': 'Москва'}, 'salary': None,
                                 'url': 'https://api.hh.ru/vacancies/84724067?host=hh.ru', 'snippet':
                                     {'requirement': 'Уверенное владение <highlighttext>Python</highlighttext> '
                                                     '(2.7,3.x)/Bash. Опыт работы c системами управления конфигурациями'
                                                     ' Ansible/Puppet. Понимание CI/CD-методологий...'}},
                                {'name': 'Стажер-разработчик Python', 'area': {'name': 'Оренбург'}, 'salary':
                                    {'from': 50000, 'to': 100000, 'currency': 'RUR'}, 'url':
                                     'https://api.hh.ru/vacancies/92363159?host=hh.ru', 'snippet':
                                     {'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть активным'
                                                     ' и внедрять эффективные решения.'}}]}
    vacancies_list = Vacancy.cast_to_object_list(vacancies_dict)
    assert len(vacancies_list) == 2
    assert vacancies_list[0].name == 'Build Engineer (Tanks Blitz)'
    assert vacancies_list[0].min_pay == 0


def test_filter_keyword_vacancies():
    vacancies_dict = {'items': [{'name': 'Build Engineer (Tanks Blitz)', 'area': {'name': 'Москва'}, 'salary': None,
                                 'url': 'https://api.hh.ru/vacancies/84724067?host=hh.ru', 'snippet':
                                     {'requirement': 'Уверенное владение <highlighttext>Python</highlighttext> '
                                                     '(2.7,3.x)/Bash. Опыт работы c системами управления конфигурациями'
                                                     ' Ansible/Puppet. Понимание CI/CD-методологий...'}},
                                {'name': 'Стажер-разработчик Python', 'area': {'name': 'Оренбург'}, 'salary':
                                    {'from': 50000, 'to': 500000, 'currency': 'RUR'}, 'url':
                                     'https://api.hh.ru/vacancies/92363159?host=hh.ru', 'snippet':
                                     {'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть активным'
                                                     ' и внедрять эффективные решения.'}}]}
    vacancies_list = Vacancy.cast_to_object_list(vacancies_dict)
    filter_word = 'build engineer'
    filtered_vacancies = Vacancy.filter_keyword_vacancies(vacancies_list, filter_word)
    assert len(filtered_vacancies) == 1


def test_filter_min_salary():
    vacancies_dict = {'items': [{'name': 'Стажер-разработчик Python', 'area': {'name': 'Оренбург'},
                                 'salary': {'from': 70000, 'to': 100000, 'currency': 'RUR'}, 'url':
                                     'https://api.hh.ru/vacancies/92363159?host=hh.ru', 'snippet':
                                     {'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть активным'
                                                     ' и внедрять эффективные решения.'}},
                                {'name': 'Стажер-разработчик Python', 'area': {'name': 'Оренбург'}, 'salary':
                                    {'from': 50000, 'to': 500000, 'currency': 'RUR'},
                                 'url': 'https://api.hh.ru/vacancies/92363159?host=hh.ru', 'snippet':
                                     {'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть активным'
                                                     ' и внедрять эффективные решения.'}}]}

    vacancies_list = Vacancy.cast_to_object_list(vacancies_dict)
    min_salary = 60000
    filtered_vacancies = Vacancy.filter_min_salary(vacancies_list, min_salary)
    assert len(filtered_vacancies) == 1


def test_filter_max_salary():
    vacancies_dict = {'items': [{'name': 'Стажер-разработчик Python', 'area': {'name': 'Оренбург'},
                                 'salary': {'from': 70000, 'to': 100000, 'currency': 'RUR'}, 'url':
                                     'https://api.hh.ru/vacancies/92363159?host=hh.ru', 'snippet':
                                     {'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть активным'
                                                     ' и внедрять эффективные решения.'}},
                                {'name': 'Стажер-разработчик Python', 'area': {'name': 'Оренбург'}, 'salary':
                                    {'from': 50000, 'to': 500000, 'currency': 'RUR'},
                                 'url': 'https://api.hh.ru/vacancies/92363159?host=hh.ru', 'snippet':
                                     {'requirement': 'Отличные коммуникативные навыки. Любовь к коду. Быть активным'
                                                     ' и внедрять эффективные решения.'}}]}

    vacancies_list = Vacancy.cast_to_object_list(vacancies_dict)
    max_salary = 200000
    filtered_vacancies = Vacancy.filter_max_salary(vacancies_list, max_salary)
    assert len(filtered_vacancies) == 1
