import pandas as pd
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import CustomUserSerializer, CreateCarSerializer, ListCarSerializer
from core.models import CustomUser, Car
from core.utils import predict_car_price


class UserViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)


class DeleteCarApiView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListCarSerializer
    queryset = Car.objects.all()


class CarApiView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListCarSerializer

    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        serializer = self.serializer_class(cars, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            dataframe = pd.DataFrame(
                {
                    "Marka pojazdu": serializer.validated_data['brand'],
                    "Model pojazdu": serializer.validated_data['model'],
                    "Wersja": serializer.validated_data['version'],
                    'Rok produkcji': serializer.validated_data['year'],
                    'Przebieg': serializer.validated_data['mileage'],
                    'Pojemność skokowa': serializer.validated_data['displacement'],
                    'Moc': serializer.validated_data['power'],
                    "Rodzaj paliwa": serializer.validated_data['fuel_type'],
                    "Skrzynia biegów": serializer.validated_data['gearbox'],
                    "Napęd": serializer.validated_data['propulsion'],
                    "Kolor": serializer.validated_data['color'],
                    "Bezwypadkowy": 'Tak' if serializer.validated_data['is_accident_free'] is True else 'Nie',
                    "Stan": serializer.validated_data['condition'],
                },
                index=[0],
            )
            serializer.save(
                user=CustomUser.objects.get(id=self.request.user.id),
                price=predict_car_price(dataframe)[0],
            )

            return Response(serializer.data)

