from django.urls import path, include

from purbeurre.views import home, search, detail, ml


urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('mentions_legal/', ml, name='ml'),
    path('search/', search, name='search'),
    path('detail/<str:substitut_detail>/', detail, name='detail'),
]
