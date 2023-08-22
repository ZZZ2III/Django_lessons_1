from rest_framework import routers
from rest.api import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls