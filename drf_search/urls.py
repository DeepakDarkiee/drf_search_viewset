
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from polls import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.HelloView.as_view(), name='hello'),
    # path('questions/', views.QuestionsAPIView.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('core.urls')),
    path('', include('polls.urls')),
]
