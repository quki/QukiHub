import os
import posixpath
from .secret import SECRET_KEY, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf.global_settings import DEFAULT_FILE_STORAGE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY
DEBUG = False
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = ['app',
                  'django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'ckeditor',
                  'storages',
                  'pipeline',
                  ]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
PIPELINE = {
    'STYLESHEETS': {
        'vendor': {
            'source_filenames': (
                'app/content/bootstrap.min.css',
                'app/content/site.css',
            ),
            'output_filename': 'css/vendor.css',
        },
        'style': {
            'source_filenames': (
                'my/my.css',
            ),
            'output_filename': 'css/my/style.css',
        },
    },
    'JAVASCRIPT': {
        'vendor_pre': {
            'source_filenames': (
                'app/scripts/*.js',
                'app/scripts/modernizr-2.6.2.js'
            ),
            'output_filename': 'js/vendor/vendor.js',
        },
        'vendor_post': {
            'source_filenames': (
                'app/scripts/jquery-1.10.2.js',
                'app/scripts/bootstrap.js',
                'app/scripts/respond.js',
            ),
            'output_filename': 'js/vendor/vendor_post.js',
        },
        'fastagram': {
            'source_filenames': (
                'js/*.js',
            ),
            'output_filename': 'js/fastagram.js',
        }
    }
}
MIDDLEWARE_CLASSES = ['django.middleware.security.SecurityMiddleware',
                      'django.contrib.sessions.middleware.SessionMiddleware',
                      'django.middleware.common.CommonMiddleware',
                      'django.middleware.csrf.CsrfViewMiddleware',
                      'django.contrib.auth.middleware.AuthenticationMiddleware',
                      'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
                      'django.contrib.messages.middleware.MessageMiddleware',
                      'django.middleware.clickjacking.XFrameOptionsMiddleware',
                      ]

ROOT_URLCONF = 'QukiHub.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': ['django.template.context_processors.debug',
                               'django.template.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages', ],
    },
}, ]

WSGI_APPLICATION = 'QukiHub.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [{
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }, ]

LANGUAGE_CODE = 'ko-KR'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ckeditor

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here

                'CodeSnippet'
            ]},
        ],
        # https://github.com/django-ckeditor/django-ckeditor/tree/master/ckeditor/static/ckeditor/ckeditor/plugins/codesnippet/lib/highlight/styles
        # https://github.com/isagalaev/highlight.js/tree/master/src/styles
        'codeSnippet_theme': 'railscasts',
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'codesnippet',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    }
}
AWS_STORAGE_BUCKET_NAME = 'qukihub'
AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.ap-northeast-2.amazonaws.com'  # for seoul region
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'app/static_local'),)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

if DEBUG:
    STATIC_URL = '/static_local/'

else:
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

'''
1. STATICFILES_DIRS
    로컬에서 static serve시에 파일을 어디서 읽어 와야 하는지 Django에게 알려주는 역할을 한다.
    값을 튜플이나 리스트로 주게 되는데, 내가 앱마다 static폴더를 만들어 놓으면 그들 사이에서 파일을 찾아 주게 된다.

2. STATIC_ROOT
    collectstatic 실행시 STATICFILES_DIRS에 포함된 디렉토리로부터 읽어와 static파일을 한곳으로 모아주는 디렉토리
    이 과정에서 adim실행에 필요한 파일들도 복사 된다.
    STATIC_ROOT = os.path.join(BASE_DIR, 'app/static_deploy') : s3를 사용하지 않고 deploy server에 저장시킬 때

3. STATICFILES_STORAGE
    python manage.py collectstatic을 실행 할 때 쓰일 앱을 설정한다.

4. STATIC_URL
    template이 static file을 참조하는 경로

'''
