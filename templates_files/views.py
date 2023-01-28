import re

import requests
from django.shortcuts import render
from .models import LastVacancyModel
from .models import Main
from .models import Navigation
from .models import Demand
from .models import Geography
from .models import Skills

def LastVacancy(request):

    navigation = Navigation.objects.all()
    context = {'navigation': navigation}

    return render(request, 'LastVacancy.html' , context)

def HomePage(request):
    home_info = Main.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'home_info': home_info}
    return render(request, 'HomePage.html', context)

def SkillsPage(request):
    skills_info = Skills.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'skills_info': skills_info}
    return render(request, 'Skills.html', context)

def GeographyPage(request):
    geography_info = Geography.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'geography_info': geography_info}
    return render(request, 'Geography.html', context)

def DemendPage(request):
    demand_info = Demand.objects.all()
    navigation = Navigation.objects.all()
    context = {'navigation': navigation, 'demand_info': demand_info}
    return render(request, 'Demend.html', context)
