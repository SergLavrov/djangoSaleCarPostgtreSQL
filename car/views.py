from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from car.forms import CarForm
from car.models import Auto


# Create your views here.

def home(request):
    return render(request, 'car/carForm.html', context={'form': CarForm()})


def postcar(request):
    carform = CarForm(request.POST)  # создаём объект формы и заполняем его данными
    if carform.is_valid():  # проверяем, что формы содержат все поля(корректность заполнения)
        auto = Auto(
            car_brand=carform.cleaned_data['car_brand'],
            year_production=carform.cleaned_data['year_production'],
            price=carform.cleaned_data['price'],
            color=carform.cleaned_data['color']
        )
        auto.save()
        return HttpResponse('Success')
    else:
        return HttpResponse("Invalid data")



def list_cars(request: HttpRequest) -> HttpResponse:
    return render(request, 'car/list_cars.html', {'cars': Auto.objects.all()})

def car_detail(request: HttpRequest, car_id: int) -> HttpResponse:
    return render(request, 'car/car_detail.html', {'car': Auto.objects.get(id=car_id)})



# ПИСАЛ САМ !!!

# ЭТО ОБНОВЛЕНИЕ / УДАЛЕНИЕ НА стороне BACKa (сервера)

# def update_car(request: HttpRequest) -> HttpResponse:
#     try:
#         car = Auto.objects.get(id=4)
#         car.year_production = 2020
#         car.save()
#         return HttpResponse('OK')
#     except:
#         return HttpResponse('Error')

def update_car(request: HttpRequest, car_id: int) -> HttpResponse:
    try:
        car = Auto.objects.get(id=car_id)
        car.price = 15500
        car.save()
        return HttpResponse('OK')
    except:
        return HttpResponse('Error')


def delete_car(request: HttpRequest, car_id: int) -> HttpResponse:
    try:
        car = Auto.objects.get(id=car_id)
        car.delete()
        return HttpResponse('OK')
    except:
        return HttpResponse('Error')
