from turtle import title
from unicodedata import category, name
from django.shortcuts import render
from .models import Post, Category, User, Avatar
from django.views.generic import TemplateView,CreateView,UpdateView
from django.views.generic.detail import DetailView
from .forms import postformulario,UserRegisterForm,AvatarFormulario,UserEditForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class BlogHomePageView(TemplateView):
    template_name= "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.all()
        return context
    

    
@login_required
def postdetail(request, id):
    post = Post.objects.get(id = id)
    return render(request, "blog/post-detail.html", {'post':post})

class DeporteView(TemplateView):
    template_name= 'blog/deportes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.filter(category__name='Deportes')
        return context

class MusicaView(TemplateView):
    template_name= 'blog/musica.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.filter(category__name='Música')
        return context

class CineView(TemplateView):
    template_name  = 'blog/cine.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.filter(category__name='Cine')
        return context

   

class TecnologiaView(TemplateView):
    template_name= 'blog/tecnologia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.filter(category__name='Tecnología')
        return context

class PoliticaView(TemplateView):
    template_name= 'blog/politica.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.filter(category__name='Política')
        return context

class EducacionView(TemplateView):
    template_name= 'blog/educacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.filter(category__name='Educación')
        return context

class RecetasView(TemplateView):
    template_name= 'blog/recetas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.postobjects.filter(category__name='Recetas')
        return context

@login_required
def AddPostView(request):
    
    avatar = Avatar.objects.filter(user=request.user)
    if request.method == 'POST':
        formulario = postformulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            category = informacion['category']
            category_obj = Category.objects.get(name=category)
            post = Post(title=informacion['title'], author=request.user, subtitle=informacion['subtitle'], image=informacion['image'], category=category_obj, text=informacion['text'], status=informacion['status'])
            post.save()
            posts = Post.postobjects.all()
            return render(request, "blog/index.html",{'posts':posts})
    else:
        formulario = postformulario()
    return render(request, "blog/add_post.html", {'formulario':formulario, 'url': avatar[0].imagen.url})


def loginrequest(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user= authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                posts = Post.postobjects.all()
                avatar = Avatar.objects.filter(user=request.user)
                if len(avatar)!=0:
                    return render(request,"blog/index.html", {"mensaje":f"Bienvenido a Blogged {usuario}!" , "posts": posts , "url": avatar[0].imagen.url})
                else:
                    return render(request,"blog/index.html", {"mensaje":f"Bienvenido a Blogged {usuario}!" , "posts": posts})
            else:

                return render(request,"blog/index.html", {"mensaje":f"Usuario o contraseña incorrecta."})

        else:
            return render(request,"blog/index.html",{"mensaje":f"Error:Formulario erroneo"})
    form = AuthenticationForm()

    return render(request, "blog/login.html", {'form':form})

def register(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"index.html", {"mensaje":"Usuario creado."})
        
    else:
        form = UserRegisterForm() 
        
    return render(request,"blog/registro.html", {"form":form})

@login_required
def deletepost(request, id):
    post = Post.objects.get(id = id)
    post.delete()

    posts = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "blog/index.html", contexto)



@login_required
def agregaravatar(request):

    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        miformulario = AvatarFormulario(request.POST, request.FILES)
        if miformulario.is_valid():
            avatarviejo= Avatar.objects.filter(user=request.user)
            if len(avatarviejo)!=0:
                avatarviejo.delete()
            avatar = Avatar(user= request.user, imagen= miformulario.cleaned_data['avatar'])
            avatar.save()
            posts= Post.postobjects.all()
            return render(request,'blog/index.html', {'user': user, 'mensaje':'AVATAR AGREGADO','posts':posts})
    else:
        miformulario= AvatarFormulario()
    return render(request,'blog/agregaravatar.html', {'miformulario':miformulario,'user':user})

@login_required
def editprofile(request):
    usuario = request.user
    
    if request.method == "POST":
        formulario = UserEditForm(request.POST, instance=usuario)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.first_name=informacion['first_name']
            usuario.last_name=informacion['last_name']

            usuario.save()

            return render(request,'blog/index.html', {'usuario': usuario, 'mensaje': 'Perfil editado exitosamente'})
    else:
        formulario= UserEditForm(instance=usuario)
    return render(request, 'blog/edit-profile.html', {'formulario':formulario})


@login_required
def editpost(request, id):
    post = Post.objects.get(id = id)

    if request.method == 'POST':
        miformulario = postformulario(request.POST,request.FILES)

        print(miformulario)

        if miformulario.is_valid():
            informacion = miformulario.cleaned_data

            post.title = informacion['title'] 
            post.subtitle = informacion['subtitle']
            post.text = informacion['text']
            post.image =informacion['image']

            post.save()
            posts = Post.objects.all()
            return render(request, "blog/index.html",{'posts':posts})
            
    else:
        miformulario = postformulario(initial={'title': post.title, 'subtitle': post.subtitle, 'text': post.text, 'image': post.image})

    return render(request,"blog/edit_post.html", {"miformulario": miformulario, "id":id})

@login_required
def profile(request):
    avatar = Avatar.objects.filter(user=request.user)
    if len(avatar)!=0:
        return render(request, 'blog/profile.html', {'url':avatar[0].imagen.url})
    else:
        return render(request,'blog/profile.html')


def AboutView(request):
    return render(request,"blog/about.html")


def noexiste(request):
    return render(request,"blog/noexiste.html")


