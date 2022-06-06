from sre_parse import CATEGORIES
from django import forms
from .models import Post, Category,User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from ckeditor.fields import RichTextField, CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

class postformulario(forms.Form):
    option = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    list_categories = (
        ('Deportes', 'Deportes'),
        ('Recetas', 'Recetas' ),
        ('Cine', 'Cine'),
        ('Educación', 'Educación'),
        ('Tecnología', 'Tecnología'),
        ('Música', 'Música'),
        ('Política', 'Política'),
    )

    title = forms.CharField(max_length=100)
    category = forms.ChoiceField(choices = Category.Categories)
    subtitle = forms.CharField(widget=CKEditorWidget())
    image = forms.ImageField()
    text = forms.CharField(widget=CKEditorWidget())
    status = forms.ChoiceField(choices = option)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetí la contraseña', widget=forms.PasswordInput)

class AvatarFormulario(forms.Form):
    avatar= forms.ImageField(label="Avatar") 

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar mail")
    password1 = forms.CharField(label="Ingrese nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    last_name= forms.CharField(label="Modificar apellido")
    first_name= forms.CharField(label="Modificar nombre")

    class Meta:
        model= User
        fields=('email','password1','password2','last_name','first_name')
        help_texts={campito: "" for campito in fields}