from django.urls import path
form . import views

app_name = 'images'
urlpatterns = [
    path('create/', views.image_create,name='create'),
]