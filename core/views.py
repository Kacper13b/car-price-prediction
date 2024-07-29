import pandas as pd
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, RedirectView, DeleteView

from core.forms import RegisterForm, CarPricePredictionForm
from core.models import Car, CustomUser
from core.utils import predict_car_price


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'core/register.html'
    success_url = '/login'
    form_class = RegisterForm
    success_message = "Your profile was created successfully"


class UserLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('cars:list_cars')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class GetCarsView(LoginRequiredMixin, ListView):
    model = Car
    paginate_by = 100
    template_name = 'cars/list_cars.html'

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user.id).order_by('id')


class DeleteCarView(LoginRequiredMixin, DeleteView):
    model = Car
    success_url = '/'
    template_name = 'cars/car_confirm_delete.html'


class PredictCarPriceView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'cars/predict_form.html'
    success_url = '/'
    form_class = CarPricePredictionForm
    success_message = "Price prediction created successfully"

    def form_valid(self, form):
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            dataframe = pd.DataFrame(
                {
                    "Marka pojazdu": form_data['brand'],
                    "Model pojazdu": form_data['model'],
                    "Wersja": form_data['version'],
                    'Rok produkcji': form_data['year'],
                    'Przebieg': form_data['mileage'],
                    'Pojemność skokowa': form_data['displacement'],
                    'Moc': form_data['power'],
                    "Rodzaj paliwa": form_data['fuel_type'],
                    "Skrzynia biegów": form_data['gearbox'],
                    "Napęd": form_data['propulsion'],
                    "Kolor": form_data['color'],
                    "Bezwypadkowy": 'Tak' if form_data['is_accident_free'] is True else 'Nie',
                    "Stan": form_data['condition'],
                },
                index=[0],
            )
            car = form.save(commit=False)

            form.instance.user = CustomUser.objects.get(id=self.request.user.id)
            price = predict_car_price(dataframe)[0]
            car.price = price
            car.save()
            return render(self.request, self.template_name, {'car_price': price, 'form': form})



