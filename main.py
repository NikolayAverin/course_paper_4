from src.classes import *

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies('Python')
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
json_saver = JSONSaver
json_saver.add_vacancy(vacancies_list)
vacancy_dict = {}
vacancies_list_for_json = []

for item in vacancies_list:
    vacancy_dict['name'] = item.name
    vacancy_dict['url'] = item.url
    vacancy_dict['area'] = item.area
    vacancy_dict['requirement'] = item.requirement
    vacancy_dict['min_pay'] = item.min_pay
    vacancy_dict['max_pay'] = item.max_pay
    vacancy_dict['currency'] = item.currency
    print(vacancy_dict)
    vacancies_list_for_json.append(vacancy_dict)

print(vacancies_list_for_json)