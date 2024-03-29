from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.core.views import MainPageView, LogInView
from config.settings import DEBUG

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),

    path('api/core/', include('app.core.urls_core')),
    path('api/', include('app.barometer.urls_barometer')),
    path('api/', include('app.owm_forecast.urls_owm_forecast')),
    path('api/', include('app.rgb_control.urls_rgb_control')),

    path('login/', LogInView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if DEBUG:
    import debug_toolbar

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
