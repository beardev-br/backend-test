from django.forms import ModelForm
from app.models import Cars

# Create the form class.
class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ['user_name', 'license_plate', 'car_brand', 'car_year', 'car_color', 'RENAVAM']