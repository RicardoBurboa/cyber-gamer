"""cyber_gamer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from sitio import views as sitio_views
from contacto import views as contacto_views
from estaciones import views as estaciones_views
from juegos import views as juegos_views
from noticias import views as noticias_views
from productos import views as productos_views
from usuarios import views as user_views

#importar static (segundo renglón) para poder hacer uso del directorio de /media
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'GameRoom'
admin.site.site_title = 'Administración'
admin.site.index_title = 'Sitio Administrativo de GameRoom'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sitio_views.home, name='home'),
    path('about/', sitio_views.about, name='about'),
    path('contacto/', contacto_views.contacto, name='contacto'),
    path('estaciones/', estaciones_views.estaciones, name='estaciones'),
    path('juegos/', juegos_views.juegos, name='juegos'),
    path('noticias/', noticias_views.noticias, name='noticias'),
    path('productos/', productos_views.productos, name='productos'),

    path('register/', user_views.register, name='register'),
    path('perfil/', user_views.profile, name='profile'),
    # path('login/', user_views.login_view, name='login'),
    # path('logout/', user_views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
]

#para obtener las imágenes de los modelos (juegos, productos, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)