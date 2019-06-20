from django.urls import path
from . import views
app_name ='mimeapp'
urlpatterns = [
    path('csv', views.csvview),
    path('pdf', views.pdfview),
    path('text', views.htmlview),
    path('xml', views.xmlview),
]