from django import forms
from .models import Bem

class BemForm(forms.ModelForm):
    class Meta:
        model = Bem
        fields = ["nome", "identificador_rfid", "categoria", "fornecedor", "departamento", "data_aquisicao", "status"]
        widgets = {
            "data_aquisicao": forms.DateInput(attrs={"type": "date"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
