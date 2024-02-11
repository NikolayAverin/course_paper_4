from src.classes import *


def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите запрос для поиска: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split(' ')
    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)
