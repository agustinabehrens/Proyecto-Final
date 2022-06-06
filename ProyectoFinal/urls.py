
from argparse import Namespace
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include,re_path
from .views import (HomePageView)
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
  



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('blog/', include('Blog.urls',namespace='blog'), name='blog'),
    path('chat/', include('chat.urls', namespace='chat'), name='chat'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  
