from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, CourseViewSet

router = DefaultRouter()

router.register('students', StudentViewSet, basename="talabalar")
router.register('courses', CourseViewSet)

urlpatterns = router.urls
