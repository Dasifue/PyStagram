from django.shortcuts import render
from account.models import User


 

def find_recomendations(user: User) -> list[User]:
    followings = user.followings.all()

    followings = [set(user.followings.all()) for user in followings]

    recomendations = set
    for i in range(0, len(followings)):
        recomendations = followings[i].intersection(*followings[i:])
    
    recomendations.remove(user)

    return recomendations



        

