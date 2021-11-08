from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from rest_framework import routers
from .views import EvaluadoViewset, EvaluadorViewset


router = routers.DefaultRouter()
router.register('Evaluado', EvaluadoViewset)
router.register('Evaluador', EvaluadorViewset)


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
    path('creaEvaluado/', views.creaEvaluado, name='creaEvaluado'), #Administrador
    path('creaEvaluador/', views.creaEvaluador, name='creaEvaluador'), #Administrador
    path('creaActividad/', views.creaActividad, name='creaActividad'), #Administrador
    path('asignarEvaluacion/', views.asignarEvaluacion, name='asignarEvaluacion'), #Administrador
    path('actividadPendiente/', views.actividadPendiente, name='actividadPendiente'), #Administrador
    path('revisionPendiente/', views.revisionPendiente, name='revisionPendiente'), #Administrador
    path('actividadRealizada/', views.actividadRealizada, name='actividadRealizada'), #Administrador
    path('baseFormulario/', views.baseFormulario, name='baseFormulario'),
    path('estadoEvaluado', views.estadoEvaluado, name='estadoEvaluado'), #Evaluador
    path('evaluacionesRealizadas/', views.evaluacionesRealizadas, name='evaluacionesRealizadas'), #Evaluador
    path('api/', include(router.urls)),
]
