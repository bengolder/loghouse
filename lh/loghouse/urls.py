from rest_framework import routers
from loghouse.api_viewsets import (
        PostViewSet,
        StreamViewSet,
        TagViewSet,
        )

router = routers.DefaultRouter()
router.register('post', PostViewSet)
router.register('stream', StreamViewSet)
router.register('tag', TagViewSet)
urlpatterns = router.urls

