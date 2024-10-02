import json
def insert( orderid, email, price, address):
    with open("acceptedorders.json", "r") as rf:
        acceptedorders = json.load(rf)
    #     acceptedorders[orderid] = [price, address]
    #
    # with open("acceptedorders.json", "w") as wf:
    #      json.dump(acceptedorders, wf, indent=4)
#         return 1
#
insert("2","dhkhdks@gmail.com","13456789","palakol")
