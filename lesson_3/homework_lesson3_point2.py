# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

e_name = input(str("Enter your name\n"))
e_lastname = input(str("Enter your last name\n"))
e_year = int(input("Enter year of birth\n"))
e_city = input(str("Enter city\n"))
e_email = input(str("Enter your email\n"))
e_telephone = input(str("Enter your telephone number\n"))

user_information = {
    "name": e_name,
    "lastname": e_lastname,
    "year": e_year,
    "city": e_city,
    "email": e_email,
    "telephone": e_telephone
}


def print_user_info(name, lastname, year, city, email, telephone):
    print(f"User information: {name}, {lastname}, {year}, {city}, {email}, {telephone}")


print_user_info(**user_information)
