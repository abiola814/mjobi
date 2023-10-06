"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from chat import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls', namespace='project')),
    path('chat/', views.index,name='chat'),
     path('chat/<str:username>', views.chat,name='chatmessage'),
    path('addcustomer/<str:name>',views.addcustomer,name="addcustomer"),
     path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
        path('api/messages', views.message_list, name='message-list'),
]
