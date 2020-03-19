from django.contrib import admin
from django.urls import path, include
import ouruser.views
import ouruser.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ouruser.views.home, name = 'index'),
    path('user/', include('ouruser.urls'))
]