from django.contrib import admin
from .models import (Administrador,
                         AuthGroup,
              AuthGroupPermissions,
                    AuthPermission,
                          AuthUser,
                    AuthUserGroups,
           AuthUserUserPermissions,
                             Cargo,
                             Casos,
                    DjangoAdminLog,
                 DjangoContentType,
                  DjangoMigrations,
                     DjangoSession,
                    EvaluacionCaso,
                          Evaluado,
                         Evaluador,
                           Persona,
                         Resultado)
# Register your models here.

admin.site.register(Administrador)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(Cargo)
admin.site.register(Casos)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)
admin.site.register(EvaluacionCaso)
admin.site.register(Evaluado)
admin.site.register(Evaluador)
admin.site.register(Persona)
admin.site.register(Resultado)