from src.classes import *

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies('Python')
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)


filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower()
filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)


json_saver = JSONSaver()
json_saver.add_vacancy(filtered_vacancies)
