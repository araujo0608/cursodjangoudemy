from django.urls import path
from recipes.views import home

# domain.com/
urlpatterns = [
    path('', home), # /
]