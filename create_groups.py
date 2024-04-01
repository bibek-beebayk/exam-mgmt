import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from exam.models import Exam, LiveExam, Question, Answer, ExamAttempt
from users.models import Student, Stream, User

def create_groups():
    group_name = "teachers"
    content_type_classes = [Exam, LiveExam, Question, Answer, ExamAttempt, Student, Stream]
    if not Group.objects.filter(name=group_name).exists():
        group = Group.objects.create(name=group_name)

        for ctype in content_type_classes:
            content_type = ContentType.objects.get_for_model(ctype)
            permissions = Permission.objects.filter(content_type=content_type)
            group.permissions.add(*permissions)
    else:
        group = Group.objects.get(name=group_name)
        group.permissions.clear()
        for ctype in content_type_classes:
            content_type = ContentType.objects.get_for_model(ctype) 
            permissions = Permission.objects.filter(content_type=content_type)
            group.permissions.add(*permissions)


def create_admin_user():
    users = User.objects.filter(username="admin")
    if users.exists():
        return
    else:
        user = User.objects.create(
            username="admin",
            email="admin@admin.com",
        )
        user.set_password("admin")
        user.save()

create_admin_user()
create_groups()