import pymongo


class Backend:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        cli = "Activity2"
        self.db = client[cli]

    def login_check(self, usr, pas):
        database = "creds"
        collection = self.db[database]
        verify = collection.find_one({"User.Username": usr})

        # print(verify), return object ID (Use this to verify user orders and user orignilaity)

        if verify:
            # identification = verify.get("_id")
            user_data = verify.get("User")
            if (user_data.get("Username")) == usr and (user_data.get("Password") == pas):
                username = user_data.get("Username")
                return True, username
            else:
                return False
        else:
            return False

    def item_list(self, item_to_check):
        database = "Items_list"
        collection = self.db[database]
        verify = collection.find_one({item_to_check: {"$exists": True}})
        if verify:
            return verify.get(item_to_check)

    def inserting_item(self, ins_dict):
        database = "Items_list"
        collection = self.db[database]
        collection.insert_many(ins_dict)


if __name__ == '__main__':
    b = Backend()
    # rezz, myid = b.login_check("Arvind", "rat")
    # print(myid)
    # --------------------------------------------------------------------------------
    # iserting = [{"blush": 789}, {"foundation": 225}, {"mascara": 299}, {"perfume": 999}]
    # b.inserting_item(iserting)
    # print(b.item_list("grapes"))
