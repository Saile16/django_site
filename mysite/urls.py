"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include  # agregamos include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Django toma el template de login desde un folder llamado registration recordar y crear eso
    path('accounts/login/', LoginView.as_view(), name='login'),
    # funcion logout
    # en settings esta la redireccion tanto para log in y out
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    # confirmar , esto agregamos para que inicie la pagina webcon este url
    path('', include('blog.urls')),

]
