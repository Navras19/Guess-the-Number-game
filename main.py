import random
from game_data import data
from art import logo , vs
print(logo)

def celebrity():
    return random.choice(data)
    
  
    # name = celebrity_person['name']
    # follower_count=  celebrity_person['follower_count']
    # description = celebrity_person['description']
    # country = celebrity_person['country']
celebrity()

def get_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    # print(f"{name}:{account[follower_count]}")
    print(f"{name}, {description}, from {country}")

account_a = celebrity()
account_b = celebrity()
get_data(account_a)
a_account_follower = account_a[follower_count]
print(a_account_follower)

