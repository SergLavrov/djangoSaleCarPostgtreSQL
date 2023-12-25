from django.urls import path
from .import views
# from .views import home, postcar, list_cars, car_detail ...

urlpatterns = [
    path('', views.home),
    path('postcar/', views.postcar),
    path('list_cars/', views.list_cars),
    path('car_detail/<int:car_id>/', views.car_detail),
    # path('update_car/', views.update_car),
    path('update_car/<int:car_id>/', views.update_car),
    path('delete_car/<int:car_id>/', views.delete_car),
]
