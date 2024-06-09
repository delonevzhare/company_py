"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

from collections import defaultdict

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

#Задача 1: Вывести названия всех отделов
def print_department_titles(departments):
    for department in departments:
        print(department['title'])
print("Названия всех отделов: ")
print_department_titles(departments)
print()
    
#Задача 2: Вывести имена всех сотрудников компании  
def print_all_employees(departments):
    for department in departments:
        for employee in department['employers']:
            print(f"{employee['first_name']} {employee['last_name']}")
print("Имена всех сотрудников компании: ")
print_all_employees(departments)
print()

#Задача 3: Вывести имена сотрудников с указанием отдела
def print_all_employees_with_department(departments):
    for department in departments:
        for employee in department['employers']:
            print(f"{employee['first_name']} {employee['last_name']} работает в {department['title']}")
print("Имена всех сотрудников с указанием отдела: ")
print_all_employees_with_department(departments)
print()

#Задача 4: Вывести имена всех сотрудников компанипи, которые получают больше 100К
def print_high_salary_employees(departments):
    for department in departments:
        for employee in department['employers']:  
            if employee['salary_rub'] > 100000:
                print(f"{employee['first_name']} {employee['last_name']} получает {employee['salary_rub']} рублей")
print("Сотрудники, получающие больше 100К: ")
print_high_salary_employees(departments)
print()    

#Залача 5: Вывести позиции, на которых получают меньше 80К
def print_low_salary_positions(departments):
    for department in departments:
        for employee in department['employers']:
            if employee['salary_rub'] < 80000:
                print(employee['position'])
print("Позиции с зарплатой менее 80К: " )
print_low_salary_positions(departments)
print()

#Задача 6: Посчитать, сколько денег уходит в месяц на каждый отдел
def print_department_monthly_expenses(departments):
    for department in departments:     
        total_salary = sum(employee['salary_rub'] for employee in department['employers'])
        print(f"{department['title']} тратит {total_salary} рублей в месяц")
print("Месячные расходы по отделам: ")
print_department_monthly_expenses(departments)
print()

#Задача 7: Вывести названия отделов с указанием минимальной зарплаты в нем
def print_department_min_salary(departments):
    for department in departments:
        min_salary = min(employee['salary_rub'] for employee in department["employers"])
        print(f"{department['title']} - минимальная зарплата: {min_salary} рублей")
print("Минимальная зарплата по отделам: ")
print_department_min_salary(departments)
print()

#Задача 8: Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нем
def print_department_salary_stats(departments):
    for department in departments:
        salaries = [employee['salary_rub'] for employee in department['employers']]
        min_salary = min(salaries)
        max_salary = max(salaries)
        avg_salary = sum(salaries)/len(salaries)
        print(f"{department['title']} - Мин: {min_salary}, Макс: {max_salary}, Сред: {avg_salary:.2f}")
print("Статистика зарплат по отделам: ")
print_department_salary_stats(departments)
print()

#Задача 9: Вывести среднюю зарплату по всей компании
def print_company_average_salary(departments):
    all_salaries = [employee['salary_rub'] for department in departments for employee in department['employers']]
    avg_salary = sum(all_salaries)/len(all_salaries)
    print(f"{avg_salary:.2f} рублей")
print("Средняя зарплата по всей компании: ")
print_company_average_salary(departments)
print()

#Задача 10: Вывести названия должностей, которые получают больше 90К
def print_high_salary_positions(departments):
    positions = set()
    for department in departments:
            for employee in department['employers']:
                if employee['salary_rub'] > 90000:
                   positions.add(employee['position'])
    for position in positions:
        print(position)
print("Позиция с зарплатой больше 90К: ")
print_high_salary_positions(departments)
print()

#Задача 11: Посчитать среднюю зарплату по каждому отделу среди девушек
def print_average_salary_for_females(departments):
    female_names = ['Michelle', 'Nicole', 'Christina', 'Caitlin']
    for department in departments:
        female_salaries = [employee['salary_rub'] for employee in department['employers'] if employee['first_name'] in female_names]
        if female_salaries:
            avg_salary = sum(female_salaries) / len(female_salaries)
            print(f"{department['title']} - Средняя зарплата девушек: {avg_salary:.2f} рублей")
        else:
            print(f"{department['title']} - Нет девушек с заданным именем")
print("Средняя зарплата девушек по отделам: ")
print_average_salary_for_females(departments)
print()

#Задача 12: Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную
def print_unique_vowel_last_names(departments):
    vowels = 'aeiouyAEIOUY'
    unique_names = set()
    for department in departments:
            for employee in department['employers']:
                if employee['last_name'][-1] in vowels:
                    unique_names.add(f"{employee['first_name']} {employee['last_name']}")
    for name in unique_names:
        print(name)
print("Имена людей, чьи фамилии заканчиваются на гласную букву: ")
print_unique_vowel_last_names(departments)
print()

#Функция для расчета налогов:
def calculate_taxes(salary, department, taxes):
    total_tax = 0
    for tax in taxes:
        if tax['department'] is None or tax['department'] == department:
            total_tax += salary * tax['value_percents'] / 100
    return total_tax

#Задача 13: Вывести список отделов со средним налогом на сотрудников этого отдела
def print_average_tax_per_department(departments, taxes):
    for department in departments:
        total_tax = sum(calculate_taxes(employee['salary_rub'], department['title'], taxes) for employee in department['employers'])
        average_tax = total_tax / len(department['employers'])
        print(f"{department['title']} - Средний налог: {average_tax:.2f} рублей")
print("Средний налог по отделам: ")
print_average_tax_per_department(departments, taxes)
print()

#Задача 14: Вывести список всех сотрудников с указанием зарплаты "на руки" и зарплаты с учетом налогов
def print_salary_after_taxes(department, taxes):
    for department in departments:
        for employee in department['employers']:
            total_tax = calculate_taxes(employee['salary_rub'], department['title'], taxes)
            net_salary = employee['salary_rub'] - total_tax
            print(f"{employee['first_name']} {employee['last_name']} - Зарплата: {employee['salary_rub']}, На руки: {net_salary:.2f} рублей")
print("Зарплаты с учетом налогов: ")
print_salary_after_taxes(departments, taxes)
print()

#Задача 15: вывести список отделов, отсортированный по месячной налоговой нагрузке 
def print_department_sorted_by_tax(department, taxes):
    department_taxes = []
    for department in departments:
        total_tax = sum(calculate_taxes(employee['salary_rub'], department['title'], taxes) for employee in department['employers'])
        department_taxes.append((department['title'], total_tax))
    sorted_departments = sorted(department_taxes, key=lambda x: x[1], reverse=True)
    for dept, tax in sorted_departments:
        print(f"{dept} - Налоговая напгрузка: {tax:.2f} рублей")
print("Отделы по налоговой нагрузке: ")
print_department_sorted_by_tax(departments, taxes)
print()

#Задача 16: Вывести всех сотрудников, за которых компания платит больше 100К налогов в год
def print_employees_high_annual_tax(departments, taxes):
    for department in departments:
        for employee in department['employers']:
            annual_tax = calculate_taxes(employee['salary_rub'], department['title'], taxes) *12
            if annual_tax > 100000:
                print(f"{employee['first_name']} {employee['last_name']} - Годовой налог: {annual_tax:.2f} рублей")
print("Сотрудники с годовым налогом больше 100К: ")
print_employees_high_annual_tax(departments, taxes)
print()

#Задача 17: Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов
def print_employee_lowest_tax(departments, taxes):
    min_tax = float('inf')
    min_tax_employee = None
    for department in departments:
        for employee in department['employers']:
            total_tax = calculate_taxes(employee['salary_rub'], department['title'], taxes)
            if total_tax < min_tax:
                min_tax = total_tax
                min_tax_employee = employee
    if min_tax_employee:
        print(f"{min_tax_employee['first_name']} {min_tax_employee['last_name']} - Налог: {min_tax:.2f} рублей")
print("Сотрудник с наименьшим налогом: ")
print_employee_lowest_tax(departments, taxes)
print()

