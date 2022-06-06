from django.urls import path
from .views import BlogHomePageView, editpost, AboutView, noexiste, postdetail, profile, editprofile, agregaravatar, DeporteView, AddPostView ,MusicaView,TecnologiaView,EducacionView,PoliticaView,RecetasView,CineView,loginrequest,register,deletepost
from django.contrib.auth.views import LogoutView
app_name= 'Blog'

urlpatterns = [
    path('', BlogHomePageView.as_view(), name='home'),
    path('deportes/', DeporteView.as_view(),name='deportes'),
    path('musica/', MusicaView.as_view(),name='musica'),
    path('cine/', CineView.as_view(),name='cine'),
    path('recetas/', RecetasView.as_view(),name='recetas'),
    path('tecnologia/', TecnologiaView.as_view(),name='tecnologia'),
    path('educacion/', EducacionView.as_view(),name='educacion'),
    path('politica/', PoliticaView.as_view(),name='politica'),
    path('about/', AboutView, name= 'about'),
    path('add_post/', AddPostView, name='add_post'),
    path('edit_post/<id>', editpost , name='edit_post'),
    path('accounts/edit-profile', editprofile, name='edit-profile'),
    path('accounts/profile', profile, name='profile'),
    path('delete_post/<id>', deletepost , name='delete_post'),
    path('accounts/login', loginrequest, name='login'),
    path('accounts/register', register, name='register'),
    path('agregaravatar/', agregaravatar, name='agregaravatar'),
    path('accounts/logout', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('noexiste', noexiste, name='noexiste'),
    path('postdetail/<id>', postdetail, name= 'post-detail'),
]