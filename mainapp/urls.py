from django.urls import path
from .import views

urlpatterns=[
    path("houses/", views.HouseListView.as_view()),
    path("houses/<str:pk>/", views.HouseDetailView.as_view()),
    path("contact-us/", views.ContactTeamView.as_view()),
]