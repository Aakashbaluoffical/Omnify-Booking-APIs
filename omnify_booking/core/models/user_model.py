from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    
    def create_user(self, username, password=None, role='user', **extra_fields):
        if not username:
            raise ValueError("Username must be set")
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('role', 'superadmin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255,unique=True)
    role = models.CharField(max_length=50,choices=[('admin','Admin'),('supradmin','SuperAdmin'),('user','User')])
    name = models.CharField(max_length=100)
    email = models.EmailField(unique= True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



   





    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()


    class Meta:
        db_table = 'user_tbl'
        verbose_name  = 'user_tbl'
        verbose_name_plural = 'user_tbls'
        ordering = ['-created_at']

        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['role','is_active'])
        ]

    def __str__(self):
        return self.username
