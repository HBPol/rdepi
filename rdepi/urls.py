"""rdepi URL Configuration

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
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login/')),
    path('coreapp/', include('coreapp.urls')),
    path('admin/', admin.site.urls, name='admin'),
    # This is Django's default authentication urls
    path ('accounts/', include('django.contrib.auth.urls')),
]
"""
In the development server user uploaded files (media) can be served using django.contrib.staticfiles.views.serve() view.
To access the MEDIA_URL in template django.template.context_processors.media must be added to the context_processors
inside the TEMPLATES config (in settings.py).
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
