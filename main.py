from game_data import data
from art import logo , versus
import random



print(logo)

user_a=random.choice(data)




def data_format(user):
    name=user["name"]
    description=user["description"]
    country=user["country"]
    return f"{name},{description} from {country}"







your_score=0

person_guess=True
while person_guess:
    user_b = random.choice(data)
    print(f"Compare A : {data_format(user_a)}.")
    print(versus)
    print(f"Aganist B : {data_format(user_b)}.")
    if user_a == user_b:
        user_b = random.choice(data)

    winner = input("Who has more follwers ? Type A or B : ").upper()
    if (winner=="A" and user_a["follower_count"] > user_b["follower_count"]):
        your_score+=1
        print(f"Your correct ,score is :{your_score}")
        user_a=user_b
    elif (winner=="B" and user_b["follower_count"]>user_a["follower_count"]):
        your_score+=1
        print(f"Your correct , score is :{your_score}")
        user_a=user_b
    else:
        print(f"Sorry you choose wrong person , score is : {your_score}")
        break










