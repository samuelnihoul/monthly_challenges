

from django.urls import path
from . import views

urlpatterns=[
    path('<int:month>',views.monthly_challeng_by_number),
    path('<str:month>',views.monthly_challenge)
]
