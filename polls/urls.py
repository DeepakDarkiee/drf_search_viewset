from django.conf.urls import url
from rest_framework import routers
from polls.views import QuestionsViewSet, ChoiceViewSet

router = routers.DefaultRouter()
router.register('Questions', QuestionsViewSet)
router.register('Choice', ChoiceViewSet)

urlpatterns = router.urls