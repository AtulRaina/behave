import json


class json_read():
    def perfom():
        with open('confi.json') as file:
            data=json.load(file)
        for k,v in data.items():
            print(k)
            for m, n in v.items():
                print(m)
                print(n[0])
                print(n[1])
