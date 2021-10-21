from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    #------Usuario-------
    path('login/', views.inicio, name='login'),
    path('loginA/', views.loginA, name='loginA'),
    path('loginE/', views.loginE, name='loginE'),
    path('index/', views.index, name='index'),
    path('caso1/', views.caso1, name="caso1"),
    path('caso2/', views.caso2, name="caso2"),
    path('vistaA/', views.vistaA, name='vistaA'),
    path('vistaE/', views.vistaE, name='vistaE'),
    path('', views.perfil, name="perfil"),
    path('seleccion/', views.seleccion, name='seleccion'),
    path('video/', views.video, name='video'),
    path('foto/', views.foto, name='foto'),
    path('cuestionario/', views.cuestionario, name='cuestionario'),
    path('final/', views.final, name='final'),
    path('creaEvaluado/', views.creaEvaluado, name='creaEvaluado'),
    path('creaEvaluador/', views.creaEvaluador, name='creaEvaluador'),
    path('creaActividad/', views.creaActividad, name='creaActividad'),
    path('asignarEvaluacion/', views.asignarEvaluacion, name='asignarEvaluacion'),
    path('estadoEvaluado/', views.estadoEvaluado, name='estadoEvaluado'),
    path('totalEvaluados/', views.totalEvaluados, name='totalEvaluados'),

]
