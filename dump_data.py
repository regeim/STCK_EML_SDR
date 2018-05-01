import json
import jsonpickle

class User(object):
    def __init__(self, email, interval):
        self.email = email
        self.stock = ['otp','vlkay','sp500','oil']
        self.interval = interval


# with open('data/user_data.json', 'w') as output:
#     user1 = User('forsimi@gmail.com',86400)
#     user1_json=jsonpickle.encode(user1)
#     json.dump(user1_json,output)
#
#
# del user1
#
#
# with open('data/user_data.json', 'r') as input:
#     user_py=jsonpickle.decode(json.load(input))
#     print(user_py.email)
#     print(user_py.stocks)
#     print(user_py.interval)
