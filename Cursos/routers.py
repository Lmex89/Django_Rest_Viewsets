from rest_framework.routers import DefaultRouter

from Cursos.views import CursosViewSet, AlumnosViewSet

router = DefaultRouter()
router.register(r'cursos',CursosViewSet)
router.register(r'alumnos',AlumnosViewSet)

urlpatterns=router.urls