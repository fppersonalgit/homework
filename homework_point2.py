# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("This tool helps to convert seconds in 00:00:00 format. Please enter seconds - \n"))

print(seconds)

hrs = seconds // 3600
minutes = seconds // 60
sec = seconds % 3600

if hrs > 24:
    hrs = hrs % 24
if minutes>60:
    minutes = minutes % 60
if sec > 60:
    sec = sec % 60

string_hrs = str(hrs)
string_minutes = str(minutes)
string_sec = str(sec)

if hrs < 10:
    string_hrs = "0" + string_hrs
if minutes < 10:
    string_minutes = "0" + string_minutes
if minutes < 10:
    string_sec = "0" + string_sec

if hrs == 24:
    string_hrs = "00"
if minutes == 60:
    string_minutes = "00"
if sec == 60:
    string_sec = "00"

print(string_hrs, ":", string_minutes, ":", string_sec)
