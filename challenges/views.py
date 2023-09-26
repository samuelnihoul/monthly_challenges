from django.shortcuts import HttpResponse,render
from django.http import HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request):
    list_items=''
    months=list(monthly_challenges.keys())
    return render(request,'challenges/index.html',{
        'months':months
    })

def monthly_challeng_by_number(request,month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month=months[month-1]
    redirect_path=reverse('month-challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text=monthly_challenges[month]
        response_data='challenges/challenge.html'
        return render(request,response_data,{
            'text':challenge_text,
            'month':month
        })
    except:
        return HttpResponseNotFound('This month is not found')
