```
> pip install django-rest-framework django-environ langchain openai
```

```
> django-admin startproject psst_back .
> django-admin startapp accounts
> django-admin startapp psc
```

settings.py 更新

```python
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

....

environ.Env.read_env(BASE_DIR.joinpath('.env'))

....

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

....

INSTALLED_APPS = [
    ... ,
    'rest_framework',  # 追加
    'accounts',        # 追加
    'psc',             # 追加
]

....

AUTH_USER_MODEL = 'accounts.User'

....

DATABASES = {
    'default': env.db(),
}

....

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

....

OPENAI_SECRET_KEY = env('OPENAI_SECRET_KEY')  # 追加
```

accounts/models.py 更新  
accounts/admin.py 更新

参考:  
[Django の認証方法のカスタマイズ | Django ドキュメント | Django](https://docs.djangoproject.com/ja/4.2/topics/auth/customizing/#substituting-a-custom-user-model)

psc/models.py 更新  
psc/admin.py 更新
