from rest_framework.routers import DefaultRouter

from core.views import UserActivityView, UserActivityViewWithPagination

app_name = 'core'
router = DefaultRouter()
router.register(r'users', UserActivityView, 'user-activity')
router.register(r'users-paginated', UserActivityViewWithPagination,
                'user-activity-paginated')
urlpatterns = router.urls
