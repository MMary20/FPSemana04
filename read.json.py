import json

path = input()

try:
    with open(path, "rt", encoding = "utf-8") as file:
        json_data = file.read()
        data = json.loads(json_data)
        print(data)

except:
    print("Ocorreu um erro!")
finally:   
    print("Processo concluído!")