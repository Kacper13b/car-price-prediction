from django.urls import path

from .views import GetCarsView, PredictCarPriceView, DeleteCarView

app_name = 'cars'

urlpatterns = [
    path('all_cars/', GetCarsView.as_view(), name="list_cars"),
    path('create_prediction/', PredictCarPriceView.as_view(), name="create_prediction"),
    path('<pk>/delete/', DeleteCarView.as_view(), name="delete_car")
]
