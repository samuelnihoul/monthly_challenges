from django.shortcuts import HttpResponse
from django.shortcuts import render

def monthly_challenge(request,month):
    challenge_text=None
    if month=='january':
        challenge_text="Eat no meat for the entire month!"
    elif month=='february':
        challenge_text='Walk for at least 20 minutes every day!'
    elif month=='march':
        challenge_text='Learn Django for at least 20 minutes every day!'
    return HttpResponse()
