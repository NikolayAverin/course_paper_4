from src.classes import *


def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите запрос для поиска: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    filtered_vacancies = keyword_processing(vacancies_list)
    filtered_min_salary_vacancies = get_min_salary_vacancies(filtered_vacancies)
    filtered_max_salary_vacancies = get_max_salary_vacancies(filtered_min_salary_vacancies)
    top_n = sorted_by_max_salary(filtered_max_salary_vacancies)
    save_to_file(top_n)


def keyword_processing(vacancies_list):
    while True:
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split(' ')
        filtered_vacancies = Vacancy.filter_keyword_vacancies(vacancies_list, filter_words)
        if len(filtered_vacancies) == 0:
            print("К сожалению таких результатов нет. Желаете ввести другие слова для поиска?")
            user_answer = input("Введите 'да', чтобы ввести другие ключевые слова, 'нет' для выхода: ")
            if user_answer.lower().strip() == 'да':
                continue
            elif user_answer.lower().strip() == 'нет':
                print('Попробуйте повторить поиск позже.')
                exit()
            else:
                print('Неверный ответ, работа программы завершается')
                exit()
        else:
            return filtered_vacancies


def get_min_salary_vacancies(filtered_vacancies):
    while True:
        try:
            min_salary = int(input("Введите значение минимальной зарплаты ('0' если не важно): "))
            filter_min_salary_vacancies = Vacancy.filter_min_salary(filtered_vacancies, min_salary)
            if len(filter_min_salary_vacancies) == 0:
                print("К сожалению таких результатов нет. Желаете ввести другие слова для поиска?")
                user_answer = input("Введите 'да', чтобы ввести другие ключевые слова, 'нет' для выхода: ")
                if user_answer.lower().strip() == 'да':
                    continue
                elif user_answer.lower().strip() == 'нет':
                    print('Попробуйте повторить поиск позже.')
                    exit()
                else:
                    print('Неверный ответ, работа программы завершается')
                    exit()
            else:
                return filter_min_salary_vacancies
        except ValueError:
            print("Значение минимальной зарплаты должно быть числом")
            continue


def get_max_salary_vacancies(filter_min_salary_vacancies):
    while True:
        try:
            max_salary = int(input("Введите значение максимальной зарплаты ('0' если не важно): "))
            if max_salary == 0:
                return filter_min_salary_vacancies
            else:
                filter_max_salary_vacancies = Vacancy.filter_max_salary(filter_min_salary_vacancies, max_salary)
                if len(filter_max_salary_vacancies) == 0:
                    print("К сожалению таких результатов нет. Желаете ввести другие слова для поиска?")
                    user_answer = input("Введите 'да', чтобы ввести другие ключевые слова, 'нет' для выхода: ")
                    if user_answer.lower().strip() == 'да':
                        continue
                    elif user_answer.lower().strip() == 'нет':
                        print('Попробуйте повторить поиск позже.')
                        exit()
                    else:
                        print('Неверный ответ, работа программы завершается')
                        exit()
                else:
                    return filter_max_salary_vacancies
        except ValueError:
            print("Значение максимальной зарплаты должно быть числом")
            continue


def sorted_by_max_salary(filter_max_salary_vacancies):
    print("Отсортировать вакансии по максимальной зарплате?")
    user_answer = input("Да/Нет: ")
    while True:
        try:
            if user_answer.lower().strip() == 'да':
                filter_max_salary_vacancies.sort(reverse=True)
                top_n = int(input(f"Какое количество вакансий показать? Максимально доступно "
                                  f"{len(filter_max_salary_vacancies)}: "))
                if top_n > len(filter_max_salary_vacancies):
                    print("Введено слишком большое количество, просто оставим все вакансии")
                    result = filter_max_salary_vacancies[:len(filter_max_salary_vacancies)]
                    return result
                else:
                    result = filter_max_salary_vacancies[:top_n]
                    return result
            elif user_answer.lower().strip() == 'нет':
                top_n = int(input(f"Какое количество вакансий показать? Максимально доступно "
                                  f"{len(filter_max_salary_vacancies)}: "))
                if top_n > len(filter_max_salary_vacancies):
                    print("Введено слишком большое количество, просто оставим все вакансии")
                    result = filter_max_salary_vacancies[:len(filter_max_salary_vacancies)]
                    return result
                else:
                    result = filter_max_salary_vacancies[:top_n]
                    return result
            else:
                print('Неверный ответ, работа программы завершается')
                exit()
        except ValueError:
            print("Количество вакансий должно быть числом")
            continue


def save_to_file(top_n):
    print("Выберите в каком формате сохранить данные, так же они будут выведены в терминал"
          "Доступно JSON, CSV(результат можно открыть в Excel), TXT. 0 для отображения только в терминале.")
    user_answer = input("Ваш выбор: ").lower().strip()
    if user_answer == '0':
        print(top_n)
    elif user_answer == 'json':
        json_saver = JSONSaver()
        json_saver.add_vacancy(top_n)
        print(top_n)
    elif user_answer == 'csv':
        csv_saver = CSVSaver()
        csv_saver.add_vacancy(top_n)
        print(top_n)
    elif user_answer == 'txt':
        txt_saver = TXTSaver()
        txt_saver.add_vacancy(top_n)
        print(top_n)
    else:
        print("Не знаю такой формат, просто покажу вам результаты в терминале.")
        print(top_n)
