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
