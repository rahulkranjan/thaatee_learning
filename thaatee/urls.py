from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('apiV1user/', include('users.urls')),
    path('apiV1blog/', include('thaatee_blog.urls')),
    path('apiV1lms/', include('thaatee_lms.urls')),
    path('apiV1frontend/', include('thaatee_frontend.urls')),
    path('apiV1cart/', include('thaatee_cart.urls')),
    path('clientblog/', include('thaatee_blog.client_urls')),
    path('clientfrontend/', include('thaatee_frontend.client_urls')),
    path('clientuser/', include('users.client_urls')),
    path('clientlms/', include('thaatee_lms.client_urls')),
    path('clientcart/', include('thaatee_cart.client_urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
