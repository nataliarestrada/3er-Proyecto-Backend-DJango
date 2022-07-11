from .views import ContactsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet, basename='contact')
urlpatterns = router.urls