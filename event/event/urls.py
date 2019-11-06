"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from eventform import views
from eventform.views import home,allmeetup,signup,signin,logoutuser,create_event,joinevent,registration,registered
#from eventform.view impo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('meetup/',allmeetup),
    path('signup/',signup),
    path('signin/',signin),
    path('logout/',views.logoutuser),
    path('createevent/',create_event),
    path('joinevent/<int:event_id>/',joinevent),
    path('registration/',registration),
    path('registered/<int:event_id>/',registered),
]
