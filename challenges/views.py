from django.shortcuts import HttpResponse
from django.shortcuts import render

monthly_challenges={
    "january":"Eat no meat for the entire month!",
    "february":"Walk for at least 20 minutes every day!",
        "march":"Learn Django for at least 20 minutes every day!",
    "april":"Eat no meat for the entire month!",
    "may":"Walk for at least 20 minutes every day!",
        "june":"Learn Django for at least 20 minutes every day!",
    "july":"Eat no meat for the entire month!",
    "august":"Walk for at least 20 minutes every day!",
        "september":"Learn Django for at least 20 minutes every day!",
    "october":"Eat no meat for the entire month!",
    "november":"Walk for at least 20 minutes every day!",
        "december":"Learn Django for at least 20 minutes every day!"
}

def monthly_challeng_by_number(request,month):
    return HttpResponse(monthly_challenges[month-1])

def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not found')
