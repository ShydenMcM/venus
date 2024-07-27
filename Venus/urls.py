"""Venus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Venus
    2. Add a URL to urlpatterns:  path('', Venus.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from landing.views import home, page1, page2, page3, page4, final, gift
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", home, name="home"),
        path("page1", page1, name="page1"),
        path("page2", page2, name="page2"),
        path("page3", page3, name="page3"),
        path("page4", page4, name="page4"),
        path("final", final, name="final"),
        path("gift", gift, name="gift")
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + debug_toolbar_urls()
)
