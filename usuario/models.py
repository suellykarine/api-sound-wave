from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, email, senha=None):
        if not email:
            raise ValueError("Usuários devem ter um email")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(senha)
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
