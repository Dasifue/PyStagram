from django.shortcuts import render
from account.models import User


 

def find_recomendations(user: User) -> list[User]:
    followings = user.followings.all()

    followings_sets = [set(user.followings.all()) for user in followings]

    recomendations = set
    for i in range(0, len(followings_sets)):
        recomendations = followings_sets[i].intersection(*followings_sets[i:])
    
    recomendations.remove(user)
    for fl in followings:
        if fl in recomendations:
            recomendations.remove(fl)
    return list(recomendations)[:11]



        

