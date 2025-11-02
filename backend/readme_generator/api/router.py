from rest_framework.routers import DefaultRouter
from .views import ReadmeRequestViewset

router = DefaultRouter()
router.register(r'requests', ReadmeRequestViewset, basename='readmerequest')

urlpatterns = router.urls