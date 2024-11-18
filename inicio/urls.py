from django.urls import path
from inicio.views import vista, vista2, vista3, inicio, vista4, vista5, template1 


urlpatterns = [   
    path('vista/', vista),
    path('vista2/', vista2),
    path('vista3/', vista3), 
    path('inicio/', inicio),  
    path('vista4/', vista4), 
    path('vista5/<nombre>/', vista5),
    path('template1/', template1),
    
]


