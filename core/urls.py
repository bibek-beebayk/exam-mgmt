from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from exam import views as exam_views
from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path("", exam_views.homepage, name="home"),
    path("exam/", exam_views.index_view, name="index"),
    path("exam/<pk>/", exam_views.ExamDetailView.as_view()),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
