from django.urls import path
from . import views

urlpatterns = [
    # path('redirect-test/', views.test, name="test_redirect"),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('registration/', views.registration, name="registration"),
    path('issue/', views.issue, name="issue"),
    path('why/', views.why, name="why"),
    path('fr/', views.fr, name="fr"),
    path('nop/', views.nop, name="nop"),

]

app_name = "web"

