from database.dbConnection import database as db

def fetch_all_users_from_db():
    all_user = []
    all_user_information = {}
    test = db["users"]
    for t in test.find():
        all_user.append(t['username'])
        if t['status'] == 'active':
            all_user_information[t['_id']] = (t['username'], t['fullname'],
                                                t['type'])
    print(all_user)
    print("$$$$$")
    print(all_user_information)
    return all_user_information, all_user
