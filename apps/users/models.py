from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.users.usermanager import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    # def get_full_name(self):
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    def get_user(self):
        return self.email