from write_data import count_data

def input_data():
    dct = dict()
    Id = count_data("name.csv") 
    dct["id"] = Id     # list[0] - это Id СОТРУДНИКА
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["status"] = input('Введите Статус: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartament"] = input('Введите Квартира: ')
    dct["other"] = input('Введите Примечание: ')
    return dct
