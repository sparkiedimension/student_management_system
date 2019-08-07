from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class AdministratorManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Administrators must have a username')

        user = self.model(username=username,)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.save(using=self._db)
        return user


class Administrator(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)

    objects = AdministratorManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True