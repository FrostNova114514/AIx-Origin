"""
URL configuration for aixorigin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from website.views import home, submit_contract

urlpatterns = [
    path('', home, name='home'),
    path('story/', home, name='story'),
    path('information/', home, name='information'),
    path('application/', home, name='application'),
    path('community/', home, name='community'),
    path('announcement/', home, name='announcement'),
    path('faq/', home, name='faq'),
    path('api/contracts/', submit_contract, name='submit_contract'),
    path('admin/', admin.site.urls),
]

frontend_dist = settings.BASE_DIR / 'frontend' / 'dist'

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': frontend_dist / 'assets'}),
    re_path(r'^images/(?P<path>.*)$', serve, {'document_root': frontend_dist / 'images'}),
    re_path(r'^static/images/(?P<path>.*)$', serve, {'document_root': frontend_dist / 'static' / 'images'}),
]
