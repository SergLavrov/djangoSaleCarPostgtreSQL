from django import forms


class CarForm(forms.Form):
    car_brand = forms.CharField(label='Марка автомобиля', max_length=25)
    year_production = forms.IntegerField(label='Год выпуска', min_value=2000)
    price = forms.IntegerField(label='Цена', min_value=5000)
    color = forms.CharField(label='Цвет автомобиля', max_length=30, required=False)
