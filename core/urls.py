from django.contrib import admin
from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('berita/<int:id>/', views.detail_berita, name='detail_berita'),
    path('program/sarjana/', views.program_sarjana, name='program_sarjana'),
    path('program/profesi/', views.program_profesi, name='program_profesi'),
    path('program/magister/', views.program_magister, name='program_magister'),
    path('pendaftaran/dosen/', views.pendaftaran_dosen, name='pendaftaran_dosen'),
    path('pendaftaran/mahasiswa/', views.pendaftaran_mahasiswa, name='pendaftaran_mahasiswa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)