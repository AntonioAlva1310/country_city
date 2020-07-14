from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from region.models import Country
from region.models import State

def index(request):
    countries = Country.objects.all()
    context = {

        'data' : countries
    }
    return render(request, 'region/index.html', context)


def states(request):
    states = State.objects.all()
    context = {

        'data' : states
    }
    return render(request, 'region/states.html', context)


def countries(request): 
    countries = Country.objects.all()
    context = {

        'data' : countries
    }
    return render(request, 'region/countries.html', context)



def show_by_country_page(request, country_id):
    country_selected = Country.objects.get(id = country_id)
    states_by_country = State.objects.filter(country = country_selected)
    print(states_by_country)
    context = {
            "country_selected" : country_selected,
            "states_by_country" : states_by_country
    }

    return render( request, 'region/country_selected.html', context)