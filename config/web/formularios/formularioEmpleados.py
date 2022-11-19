from django import forms

class FormularioEmpleados(forms.Form):
    CARGOS=(
        (1,'mesero'),
        (2,'chef'),
        (3,'recepcionista')
    )

    nombre=forms.CharField(
        required=True,
        max_length=15,
        label='Nombre ',
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )

    apellido = forms.CharField(
        required=True,
        max_length=15,
        label='Apellido ',
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )

    cargo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-select mb-3'}),
        choices=CARGOS
    )