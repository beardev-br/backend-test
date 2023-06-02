from django.forms import ModelForm
from app.models import Carros

# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['Nome_do_usuário_do_veículo', 'Placa_do_Carro', 'Marca_do_Carro', 'Ano_do_Carro', 'Cor_do_veículo', 'Número_do_RENAVAM']