import json


class Database2:

    def insert(self , name , email, mobile,password,type,address,city):
        with open("vendors.json","r") as rf:
            vendors=json.load(rf)

            if email in vendors:
                return 0
            else:
                vendors[email]=[name,mobile,password,type,address,city]

        with open("vendors.json","w") as wf:
            json.dump(vendors,wf,indent=4)
            return 1

    def search(self, email, password):
        with open("vendors.json", "r") as rf:
            vendors = json.load(rf)
            if email in vendors:
                if vendors[email][2] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
