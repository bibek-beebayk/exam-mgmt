import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-8tfn6ebkdf76eo$**gdl5ix%px8!95cmsbc94dk748l(2#jm3v"

DEBUG = True

ALLOWED_HOSTS = ["erp-tunnel.kalodhunga.com", "localhost", "127.0.0.1", "exam-management-production.up.railway.app", "onlinepiacademy.com"]

CSRF_TRUSTED_ORIGINS = ["https://erp-tunnel.kalodhunga.com", "https://exam-management-production.up.railway.app", "https://onlinepiacademy.com"]

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_ckeditor_5",
    "import_export",
    "users",
    "exam",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.context_users_info",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(
#         # Replace this value with your local database's connection string.
#         default='postgresql://postgres:postgres@localhost:5432/mysite',
#         conn_max_age=600
#     )
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("PGDATABASE", "exam"),
        "USER": os.environ.get("PGUSER", "postgres"),
        "PASSWORD": os.environ.get("PGPASSWORD", ""),
        "HOST": os.environ.get("PGHOST", ""),
        "PORT": os.environ.get("PGPORT", ""),
        "ATOMIC_REQUESTS": True,
    }
}

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kathmandu"

USE_I18N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]

if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"


customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]

# path to the custom CSS file
CKEDITOR_5_CUSTOM_CSS = "css/ckeditor5/admin_dark_mode_fix.css"  # CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage"  # optional
CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload",
        ],
    },
    #     "extends": {
    #         "blockToolbar": [
    #             "paragraph",
    #             "heading1",
    #             "heading2",
    #             "heading3",
    #             "|",
    #             "bulletedList",
    #             "numberedList",
    #             "|",
    #             "blockQuote",
    #         ],
    #         "toolbar": [
    #             "heading",
    #             "|",
    #             "outdent",
    #             "indent",
    #             "|",
    #             "bold",
    #             "italic",
    #             "link",
    #             "underline",
    #             "strikethrough",
    #             "code",
    #             "subscript",
    #             "superscript",
    #             "highlight",
    #             "|",
    #             "codeBlock",
    #             "sourceEditing",
    #             "insertImage",
    #             "bulletedList",
    #             "numberedList",
    #             "todoList",
    #             "|",
    #             "blockQuote",
    #             "imageUpload",
    #             "|",
    #             "fontSize",
    #             "fontFamily",
    #             "fontColor",
    #             "fontBackgroundColor",
    #             "mediaEmbed",
    #             "removeFormat",
    #             "insertTable",
    #         ],
    #         "image": {
    #             "toolbar": [
    #                 "imageTextAlternative",
    #                 "|",
    #                 "imageStyle:alignLeft",
    #                 "imageStyle:alignRight",
    #                 "imageStyle:alignCenter",
    #                 "imageStyle:side",
    #                 "|",
    #             ],
    #             "styles": [
    #                 "full",
    #                 "side",
    #                 "alignLeft",
    #                 "alignRight",
    #                 "alignCenter",
    #             ],
    #         },
    #         "table": {
    #             "contentToolbar": [
    #                 "tableColumn",
    #                 "tableRow",
    #                 "mergeTableCells",
    #                 "tableProperties",
    #                 "tableCellProperties",
    #             ],
    #             "tableProperties": {
    #                 "borderColors": customColorPalette,
    #                 "backgroundColors": customColorPalette,
    #             },
    #             "tableCellProperties": {
    #                 "borderColors": customColorPalette,
    #                 "backgroundColors": customColorPalette,
    #             },
    #         },
    #         "heading": {
    #             "options": [
    #                 {
    #                     "model": "paragraph",
    #                     "title": "Paragraph",
    #                     "class": "ck-heading_paragraph",
    #                 },
    #                 {
    #                     "model": "heading1",
    #                     "view": "h1",
    #                     "title": "Heading 1",
    #                     "class": "ck-heading_heading1",
    #                 },
    #                 {
    #                     "model": "heading2",
    #                     "view": "h2",
    #                     "title": "Heading 2",
    #                     "class": "ck-heading_heading2",
    #                 },
    #                 {
    #                     "model": "heading3",
    #                     "view": "h3",
    #                     "title": "Heading 3",
    #                     "class": "ck-heading_heading3",
    #                 },
    #             ]
    #         },
    #     },
    #     "list": {
    #         "properties": {
    #             "styles": "true",
    #             "startIndex": "true",
    #             "reversed": "true",
    #         }
    #     },
}

IMPORT_EXPORT_USE_TRANSACTIONS = True

from import_export.formats.base_formats import CSV, XLSX

IMPORT_FORMATS = [CSV, XLSX]

LOGIN_URL = '/login/'  # Replace with your custom login URL
