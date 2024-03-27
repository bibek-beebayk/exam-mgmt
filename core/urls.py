from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from exam import views as exam_views

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path("", exam_views.index_view, name="index"),
    path("<pk>/", exam_views.ExamDetailView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
