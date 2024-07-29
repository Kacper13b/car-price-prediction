from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    token = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.username


class Car(models.Model):
    BRAND_CHOICES = (
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Porsche', 'Porsche'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    brand = models.CharField(null=False, blank=False, max_length=300, verbose_name='Marka pojazdu', choices=BRAND_CHOICES)
    model = models.CharField(null=True, blank=True, max_length=300, verbose_name='Model pojazdu')
    version = models.CharField(null=True, blank=True, max_length=300, verbose_name='Wersja')
    year = models.IntegerField(null=True, blank=True, verbose_name='Rok produkcji')
    mileage = models.IntegerField(null=True, blank=True, verbose_name='Przebieg')
    displacement = models.IntegerField(null=True, blank=True, verbose_name='Pojemność skokowa')
    power = models.IntegerField(null=True, blank=True, verbose_name='Moc')
    fuel_type = models.CharField(null=True, blank=True, max_length=300, verbose_name='Rodzaj paliwa')
    gearbox = models.CharField(null=True, blank=True, max_length=300, verbose_name='Skrzynia biegów')
    propulsion = models.CharField(null=True, blank=True, max_length=300, verbose_name='Napęd')
    color = models.CharField(null=True, blank=True, max_length=300, verbose_name='Kolor')
    is_accident_free = models.BooleanField(null=False, blank=False, verbose_name='Bezwypadkowy')
    condition = models.CharField(null=True, blank=True, max_length=300, verbose_name='Stan')
    price = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=50, verbose_name='Cena')

    def __str__(self):
        return f"{self.id} {self.brand} {self.model} - {self.price}"
