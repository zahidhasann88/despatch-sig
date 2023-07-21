from database.dbConnection import database as db


def validation(data):
    print(data,' printing from authServices validation()')
    # print(Database.db)
    user = db.users.find_one({'username': data['username']})
    print(user)
    if user is None:
        return False, user
    if user['password'] != data['password']:
        return False, None
    return True, user


def save_register_info(data):
    # print(data)
    info = {'username': data['username'], 'password': data['password'],
            'gender': data['gender'], 'rank': data['occupation'], 'email': data['email'],
            'bday': data['birthday'], 'terms': data['terms']}
    db.users.insert_one(info)
    return
