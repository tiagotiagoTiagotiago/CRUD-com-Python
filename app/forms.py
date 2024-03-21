from django.forms import ModelForm
from app.models import Usuario

# Create the form class.
class UsuarioForm(ModelForm):
     class Meta:
        model = Usuario
        fields = ["nome", "cpf", "email", "numero_telefone", "cep"]