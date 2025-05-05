from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from config import settings


def index(request):
    return HttpResponse(f"Hello, Django!")


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('books/', include('books.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('tran/', include('transactions.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
