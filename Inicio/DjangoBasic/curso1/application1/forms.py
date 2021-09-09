from django import forms

# Subclase de forms.Form
class AgregarTarea(forms.Form):
    # nombre del label tareass
    tarea = forms.CharField()