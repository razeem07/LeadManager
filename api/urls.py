
from django.urls import path
from api import views

urlpatterns = [

    path('leads/',views.LeadListCreateView.as_view()),
    path("leads/<int:pk>/",views.LeadRetrieveUpdateDestroyView.as_view()),
    
]
