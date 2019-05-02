import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'n+q8bpiudy_x-#4cjjrw4yi5r_srcal@i%2_io(7@q2)1fq-4n'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'academic',
    'judgment_facts',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'JF.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'JF.wsgi.application'

DATABASES = {
    #           HOSTINGER DATABASE          #
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u347988228_jf',
        'USER': 'u347988228_user',
        'PASSWORD': 'Conexao123$',
        'HOST': 'sql170.main-hosting.eu.',
        # 'OPTIONS': {
        #     'driver': 'SQL Server Native Client 11.0'
        # }
    }

    #           AZURE DATABASE              #
    # 'default': {
    #    'ENGINE': 'sql_server.pyodbc',
    #    'NAME': 'db_judgment_facts',
    #    'HOST': 'iffact.database.windows.net',
    #    'PORT': 1433,
    #    'USER': 'admin_iffact@iffact',
    #    'PASSWORD': 'Conexao123$',
    #    'OPTIONS': {
    #        'host_is_server': True,
    #        'driver': 'SQL Server Native Client 11.0'
    #    }
    # }
}


AUTH_PASSWORD_VALIDATORS = [
    {
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
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = "account.User"

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
