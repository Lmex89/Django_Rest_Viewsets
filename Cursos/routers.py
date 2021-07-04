from rest_framework.routers import DefaultRouter

from Cursos.views import CursosViewSet, AlumnosViewSet, MaestrosViewSet

router = DefaultRouter()
router.register(r'cursos', CursosViewSet)
router.register(r'alumnos', AlumnosViewSet)
router.register(r'maestros', MaestrosViewSet)
urlpatterns = router.urls
