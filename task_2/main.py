#Гурский
print("start code")
code_in=str(input("Введите код квалификации: "))
import json
n=0

with open('dump.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for sl in data:
        if sl.get("model")!="data.specialty":
            continue

        fields = sl.get("fields", {})
        if (sl["fields"]["code"]) == code_in[0:12]:
            print(("Найдено").center(40,"="))
            print(f'{code_in[0:12]} >> Специальность "{sl["fields"]["title"]}", {sl["fields"]["c_type"]}')
    for sl in data:
        if sl.get("model")!="data.skill":
            continue

        fields = sl.get("fields", {})
        if (sl["fields"]["code"]) == code_in:
            print(f'{code_in}>> Квалификация "{sl["fields"]["title"]}"' )
            n+=1
if n==0:
    print(("Не найдено").center(40,"="))
print("end code")