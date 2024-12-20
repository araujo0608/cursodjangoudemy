from django.urls import path
from recipes import views

app_name = 'recipes'

# domain.com/
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]