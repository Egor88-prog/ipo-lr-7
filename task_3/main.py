#Вариант 1  Гурский
import json
print("code start")

def print_all_lens():
     import json
     with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for line in data:
                print(f"{line["id"]}. {line["name"]}({line["latin_name"]}), пресноводная({line["is_salt_water_fish"]}),количество видов= {line["sub_type_count"]}")
            print("")

def print_len():
    import json
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        id_in=str(input("Введите id рыбы "))
        k=0
        for line in data:
            if id_in==line["id"]:
                print(f"{line["id"]}. {line["name"]}({line["latin_name"]}), пресноводная({line["is_salt_water_fish"]}),количество видов= {line["sub_type_count"]}")
                k+=1
                break
        if k==0:
            print("id не найдено")
        print("")
        
def add_len():
    import json
    with open('data.json', 'r', encoding='utf-8') as file:
        data_f = json.load(file)
        data={}
        data["id"]=str(input("Введите id: "))
        data["name"]=str(input("Введите название рыбы "))
        data["latin_name"]=str(input("Введите латинское (научное) название рыбы "))
        while True:
            match str(input("Рыба пресноводная да/нет ")):
                case "да":
                    data["is_salt_water_fish"]=bool(1)
                    break
                case "нет":
                    data["is_salt_water_fish"]=bool(0)
                    break
                case _:
                    print("Повторите попытку")
        data["sub_type_count"]=str(input("Введите количество подвидов рыбы "))
        data_f.append(data)
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data_f, file, ensure_ascii=False, indent=4)
    with open('data.json', 'r', encoding='utf-8') as file:
        data_f = json.load(file)
        data_f=sorted(data_f,key=lambda x:x["id"])
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data_f, file, ensure_ascii=False, indent=4)
        print("Запись добавлена\n")

def del_len():
    import json
    with open('data.json', 'r', encoding='utf-8') as file:
        data_f = json.load(file)
        del_id=str(input("Введите id для удаления "))
        data_f = [item for item in data_f if item.get("id") != del_id]
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data_f, file, ensure_ascii=False, indent=4)
def menu():
    interactions=-1
    while True:
        interactions+=1
        print ("1. Вывести все записи")
        print ("2. Вывести запись по полю ")
        print ("3. Добавить запись ")
        print ("4. Удалить запись по полю")
        print ("5. Выйти из программы")        
        n=str(input("Введите номер необходимой операции: "))
        print("")
        match n:
            case "1":
               print_all_lens()
            case "2":
                print_len()
            case "3":
                add_len()
            case "4":
                del_len()
            case "5":
                print(f"Было сделано {interactions} взаимодействий")
                break
            case _:
                print("Операция не найдена\n")
menu()
print("code end")