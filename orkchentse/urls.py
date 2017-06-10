from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from orkchentse.storymaker.views.story import story


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^story/$', story, name='story'),
]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
