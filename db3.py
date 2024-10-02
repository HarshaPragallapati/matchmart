import json


class Database3:
    count=0


    def insert(self , name , type,address,email):
        with open("wdb.json","r") as rf:
            wdb=json.load(rf)
            Database3.count+=1
            wdb[Database3.count]=[type,name,address,email]

        with open("wdb.json","w") as wf:
            json.dump(wdb,wf,indent=4)
            return 1