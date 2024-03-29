from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from exam import views as exam_views
from users import views as user_views

admin.AdminSite.index_template = "admin_index.html"

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path("", exam_views.homepage, name="home"),
    path("exam/", exam_views.index_view, name="index"),
    path("practice/", exam_views.practice_test_view, name="practice"),
    path("exam/<pk>/", exam_views.ExamDetailView.as_view()),
    path("live-exam/<pk>/", exam_views.live_exam_view, name="live-exam"),
    path("practice/<pk>/", exam_views.ExamDetailView.as_view()),
    # path("exam-summary/<pk>/", exam_views.ExamSummaryView.as_view()),
    path("exam-summary/<pk>/", exam_views.exam_summary_view, name="exam-summary"),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('profile/', user_views.profile_view, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
