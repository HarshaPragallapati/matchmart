import json


class Database4:
    def insert(self,orderid,email,price,address,city):
        with open("acceptedorders.json", "r") as rf:
            acceptedorders = json.load(rf)
            acceptedorders[str(orderid)+"_"+str(email)] = [price, address,city]

        with open("acceptedorders.json", "w") as wf:
            json.dump(acceptedorders, wf, indent=4)
            return 1