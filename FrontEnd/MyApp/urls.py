from django.urls import path
from . import views

urlpatterns=[
    path('api/',views.myform_view, name='myFormComplete'),
    path('consulta/Hashtags/',views.consulta_hashtag, name='consultaHashtag'),
    path('consulta/Menciones/',views.consulta_menciones, name='consultaMenciones'),
    path('consulta/Sentimientos/',views.consulta_sentimiento, name='consultaSentimiento'),
    path('grafica/Hashtags/',views.grafica_hashtag, name='graficaHashtag'),
    path('grafica/Menciones/',views.grafica_menciones, name='graficaMenciones'),
    path('grafica/Sentimientos/',views.grafica_sentimiento, name='graficaSentimiento'),
    path('informacion/estudiante/',views.datos_estudiante, name='datosEstudiante')
]