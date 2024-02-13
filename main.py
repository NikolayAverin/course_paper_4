from src.classes import *

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies('Python')
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
vacancies_list.sort(reverse=True)
print(vacancies_list[0:2])


# filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower()
# filtered_vacancies = Vacancy.filter_keyword_vacancies(vacancies_list, filter_words)
# print(filtered_vacancies)
# filter_min_salary = Vacancy.filter_min_salary(filtered_vacancies, 60000)
# print(filter_min_salary)


# json_saver = JSONSaver()
# json_saver.add_vacancy(filtered_vacancies)
