from .views import FollowersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FollowersViewSet, basename='followers')
urlpatterns = router.urls