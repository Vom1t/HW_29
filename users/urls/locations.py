from rest_framework import routers

from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register(r'', LocationViewSet)

urlpatterns = router.urls
