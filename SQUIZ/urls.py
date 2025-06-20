"""
URL configuration for SQUIZ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from . import views, settings

urlpatterns = [
	  path('',views.index, name="home"),
	  path('profile',views.profile, name="profile"),
	  path('thecategory/<str:slug>',views.thecategory, name="thecategory"),
	  path('quiz/<str:slug>',views.quiz, name="quiz"),
	  path('apropos',views.propos, name="apropos"),
	  path('categories',views.categories, name="categories"),
	  path('classement',views.classement, name="classement"),
	  path('singin',views.singin, name="singin"),
	  path('logout',views.logout, name="logout"),
	  path('login',views.login, name="login"),
	  path('faq',views.faq, name="faq"),
	  path('badges',views.badges, name="badges"),
	  path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

