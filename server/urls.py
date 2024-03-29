from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('products/', include('product.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('user/', include('cart.urls')),
]

# urlpatterns += [re_path(r'^.*',
#                         TemplateView.as_view(template_name='index.html'))]
