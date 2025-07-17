from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Producto, Empleado, Perfil, Publicacion


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = Perfil
        fields = ['avatar', 'bio', 'fecha_nacimiento']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # recibimos el usuario
        super().__init__(*args, **kwargs)
        self.fields['first_name'].initial = user.first_name
        self.fields['last_name'].initial = user.last_name
        self.fields['email'].initial = user.email
        self.user = user

    def save(self, commit=True):
        perfil = super().save(commit=False)
        self.user.first_name = self.cleaned_data['first_name']
        self.user.last_name = self.cleaned_data['last_name']
        self.user.email = self.cleaned_data['email']
        if commit:
            self.user.save()
            perfil.user = self.user
            perfil.save()
        return perfil

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    asunto = forms.CharField(label='Asunto', max_length=150)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
        
#Forms tercer entregable

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo']
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'informacion', 'precio']
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'puesto', 'dni']

class BuscarProductoFormulario(forms.Form):
    nombre = forms.CharField(label = "Nombre del producto", max_length=100)
