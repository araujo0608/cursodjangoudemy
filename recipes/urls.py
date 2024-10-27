from django.urls import path
from recipes.views import home, about, contact

# domain.com/
urlpatterns = [
    path('', home), # /
    path('about/', about), # /about/
    path('contact/', contact), # /contact/
]