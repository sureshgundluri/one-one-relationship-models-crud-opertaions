from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def insert_country(request):
    code=input('enter code :')
    name=input('enter name:')
    population=int(input('enter no of persons:'))
    king=input('enter name of king:')
    C=Country.objects.get_or_create(c_code=code,c_name=name,c_population=population,c_king=king)[0]
    C.save()
    return HttpResponse('country inserted successfully')
def insert_capital(request):
    code=input('enter code :')
    name=input('enter name:')
    population=int(input('enter no of persons:'))
    king=input('enter name of king:')
    capital=input('enter capital:')
    C=Country.objects.get_or_create(c_code=code,c_name=name,c_population=population,c_king=king)[0]
    C.save()
    T=Capital.objects.get_or_create(c_code=C,c_capital=capital)[0]
    T.save()
    return HttpResponse('capital inserted successfully')

def details_countries(request):
    T=Country.objects.order_by('-c_name')
    T=Country.objects.order_by(Length('c_name'))
    T=Country.objects.exclude(c_name='America')
    T=Country.objects.filter(c_population__lt=1460000000)
    T=Country.objects.filter(c_population__gt=1460000000)
    T=Country.objects.filter(c_population__gte=1450000000)
    T=Country.objects.filter(c_population__lte=1450000000)
    T=Country.objects.filter(c_name__startswith='A')
    T=Country.objects.filter(c_name__endswith='ia')
    T=Country.objects.filter(c_name__in=('America','Russia'))
    T=Country.objects.filter(c_name__contains=('in'))
    T=Country.objects.all()

    d={'data':T}
    return render(request,'details_countries.html',d)


def details_capital(request):
    T=Capital.objects.order_by('c_capital')
    T=Capital.objects.order_by(Length('c_capital'))
    T=Capital.objects.exclude(c_code=1)

    d={'data':T}
    return render(request,'details_capital.html',d)

def update_country(request):
    Country.objects.update_or_create(c_name='sri lanka',defaults={'c_population':230000000,'c_name':'sri lanka','c_king':'Ranil Wickremesinghe'})
    return HttpResponse('Updated country successfully')
    

def delete_country(request):
    Country.objects.filter(c_name='sri lanka').delete()
    return HttpResponse('Country deleted successfully')

    