from rest_framework import routers
from .api import NoteViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('notes', NoteViewSet, 'Notes')

urlpatterns = router.urls
