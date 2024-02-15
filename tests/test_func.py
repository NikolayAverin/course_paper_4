import pytest
import mock
import builtins
from src.func import *


def test_user_interaction():

    with mock.patch('builtins.input', side_effect=['python', 'java', 0, 0, 'да', 1, 'txt']):
        assert user_interaction() is None

    with pytest.raises(OSError):
        user_interaction()


def test_keyword_processing():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Волгоград',
                        'Нужно уметь всё', 70000, 100000, 'RUB')
    test_vacancies = [vacancy_1, vacancy_2]

    with mock.patch.object(builtins, 'input', lambda _: 'самара'):
        assert keyword_processing(test_vacancies) == [vacancy_1]

    with pytest.raises(SystemExit):
        with mock.patch('builtins.input', side_effect=['test', 'нет']):
            keyword_processing(test_vacancies)

    with pytest.raises(SystemExit):
        with mock.patch('builtins.input', side_effect=['test', 'test']):
            keyword_processing(test_vacancies)

    with mock.patch('builtins.input', side_effect=['test', 'да', 'самара']):
        assert keyword_processing(test_vacancies) == [vacancy_1]

    with pytest.raises(OSError):
        get_min_salary_vacancies(test_vacancies)


def test_get_min_salary_vacancies():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        'Нужно уметь всё', 70000, 100000, 'RUB')
    test_vacancies = [vacancy_1, vacancy_2]

    with mock.patch.object(builtins, 'input', lambda _: 60000):
        assert get_min_salary_vacancies(test_vacancies) == [vacancy_2]

    with mock.patch.object(builtins, 'input', lambda _: 0):
        assert get_min_salary_vacancies(test_vacancies) == [vacancy_1, vacancy_2]

    with mock.patch('builtins.input', side_effect=[90000, 'да', 60000]):
        assert get_min_salary_vacancies(test_vacancies) == [vacancy_2]

    with pytest.raises(SystemExit):
        with mock.patch('builtins.input', side_effect=[90000, 'нет']):
            get_min_salary_vacancies(test_vacancies)

    with pytest.raises(StopIteration):
        with mock.patch('builtins.input', side_effect=['test']):
            get_min_salary_vacancies(test_vacancies)

    with pytest.raises(SystemExit):
        with mock.patch('builtins.input', side_effect=[90000, 'test']):
            get_min_salary_vacancies(test_vacancies)

    with pytest.raises(OSError):
        get_min_salary_vacancies(test_vacancies)


def test_get_max_salary_vacancies():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        'Нужно уметь всё', 70000, 150000, 'RUB')
    test_vacancies = [vacancy_1, vacancy_2]

    with mock.patch.object(builtins, 'input', lambda _: 120000):
        assert get_max_salary_vacancies(test_vacancies) == [vacancy_1]

    with mock.patch.object(builtins, 'input', lambda _: 0):
        assert get_max_salary_vacancies(test_vacancies) == [vacancy_1, vacancy_2]

    with mock.patch('builtins.input', side_effect=[50000, 'да', 120000]):
        assert get_max_salary_vacancies(test_vacancies) == [vacancy_1]

    with pytest.raises(SystemExit):
        with mock.patch('builtins.input', side_effect=[50000, 'нет']):
            get_max_salary_vacancies(test_vacancies)

    with pytest.raises(SystemExit):
        with mock.patch('builtins.input', side_effect=[50000, 'test']):
            get_max_salary_vacancies(test_vacancies)

    with pytest.raises(StopIteration):
        with mock.patch('builtins.input', side_effect=['test']):
            get_max_salary_vacancies(test_vacancies)

    with pytest.raises(OSError):
        get_max_salary_vacancies(test_vacancies)


def test_sorted_by_max_salary():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        'Нужно уметь всё', 70000, 150000, 'RUB')
    test_vacancies = [vacancy_1, vacancy_2]

    with mock.patch('builtins.input', side_effect=['да', 1]):
        assert sorted_by_max_salary(test_vacancies) == [vacancy_2]

    with mock.patch('builtins.input', side_effect=['да', 3]):
        assert sorted_by_max_salary(test_vacancies) == [vacancy_2, vacancy_1]

    with mock.patch('builtins.input', side_effect=['нет', 1]):
        assert sorted_by_max_salary(test_vacancies) == [vacancy_2]

    with mock.patch('builtins.input', side_effect=['нет', 3]):
        assert sorted_by_max_salary(test_vacancies) == [vacancy_2, vacancy_1]

    with pytest.raises(SystemExit):
        with mock.patch('builtins.input', side_effect=['test']):
            sorted_by_max_salary(test_vacancies)

    with pytest.raises(StopIteration):
        with mock.patch('builtins.input', side_effect=['да', 'test']):
            sorted_by_max_salary(test_vacancies)

    with pytest.raises(OSError):
        sorted_by_max_salary(test_vacancies)


def test_save_to_file():
    vacancy_1 = Vacancy('Разработчик', 'https://test1.ru', 'Самара',
                        'Нужно уметь всё', 50000, 100000, 'RUB')
    vacancy_2 = Vacancy('Разработчик', 'https://test2.ru', 'Самара',
                        'Нужно уметь всё', 70000, 100000, 'RUB')
    test_vacancies = [vacancy_1, vacancy_2]

    with mock.patch.object(builtins, 'input', lambda _: '0'):
        assert save_to_file(test_vacancies) is None
    with mock.patch.object(builtins, 'input', lambda _: 'json'):
        assert save_to_file(test_vacancies) is None
    with mock.patch.object(builtins, 'input', lambda _: 'csv'):
        assert save_to_file(test_vacancies) is None
    with mock.patch.object(builtins, 'input', lambda _: 'txt'):
        assert save_to_file(test_vacancies) is None
    with mock.patch.object(builtins, 'input', lambda _: 'test'):
        assert save_to_file(test_vacancies) is None

    with pytest.raises(OSError):
        save_to_file(test_vacancies)
