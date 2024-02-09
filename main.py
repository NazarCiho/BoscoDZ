def get_user_input():
    name=input("'Введіть Ім'я: ")
    month=input("'Введіть Місяць: ")
    year=input("'Введіть вік: ")
    return name, month, year
def validate_month(month):
    a=0
    if int(month)<=12 and int(month)>0:
        pass
    else:
        a=True
    return a
def validate_year(year):
    b=0
    if int(year)<120 and int(year)>5:
        pass
    else:
        b=True
    return b
def create_test_file(name,year,month):
    with open('Filedz.txt', 'w',encoding='utf-8') as file:
        file.write(name + '\n')
        file.write(year + '\n')
        file.write(month + '\n')
