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

    def insert_user_complete(self, usr, pas, img_data):
        database = "creds"
        collection = self.db[database]

        collection.insert_one({"User": {
            "Username": usr,
            "Password": pas,
            "Image_data": img_data}
        })

    def insert_user_img(self, name, img_data):
        database = "creds"
        collection = self.db[database]

        collection.update_one({"User.Username": name}, {"$set": {"User.Image_data": img_data}})

    def ask_profile_image(self, name):
        database = "creds"
        collection = self.db[database]

        user_data = collection.find_one({"User.Username": name})
        if user_data:
            username = name
            address = user_data.get('User', {}).get("Address")
            contact = user_data.get('User', {}).get("Contact_no")
            image = user_data.get('User', {}).get("Image_data")
            return username, address, contact, image
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

    def insert_into_orderhistory(self, name, dict1):
        database = "creds"
        collection1 = self.db[database]

        store_check = collection1.find_one({"User.Username": name})
        compare_id = store_check.get("_id")

        database = "order_history"
        collection2 = self.db[database]
        order_details = [dict1]

        result = collection2.insert_many(order_details)

        for identify in result.inserted_ids:
            collection1.update_one({"_id": compare_id}, {"$push": {"User.Order_history": identify}})
        return True


if __name__ == '__main__':
    b = Backend()

    # dict1 = {"0": {'Item_name': 'fish', 'price': 229, 'quantity': 3, 'total': 687}, "1": {'Item_name': 'paper towel', 'price': 195, 'quantity': 2, 'total': 390}, "2": {'Item_name': 'lipstick', 'price': 199, 'quantity': 1, 'total': 199}}
    # b.insert_into_orderhistory("Arvind", dict1)

    # rezz, myid = b.login_check("Arvind", "rat")
    # print(myid)
    # --------------------------------------------------------------------------------
    # Inserting products data
    # iserting = [{"blush": 789}, {"foundation": 225}, {"mascara": 299}, {"perfume": 999}]
    # b.inserting_item(iserting)

    # ------------------------------------------------------------------------------
    # Inserting image data for user
    # uname = "Prateek"
    # image_path = 'images/ast.jpg'
    # with open(image_path, 'rb') as img_file:
    #     binary_data = img_file.read()
    #
    # b.insert_user_img(uname, binary_data)

    # ------------------------------------------------------------------------------
    # Inserting all data for user

    # uname = "Shubham"
    # paswrd = "photo"
    # image_path = 'images/hand_of_happiness.jpg'
    #
    # with open(image_path, 'rb') as image_file:
    #     bn_data = image_file.read()
    #
    # b.insert_user_complete(uname, paswrd, bn_data)

    # ------------------------------------------------------------------------------
    # print(b.ask_profile_image("Prateek"))
