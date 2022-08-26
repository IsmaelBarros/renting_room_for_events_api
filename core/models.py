from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from app import settings

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """create, save and return a new usr."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class EventType(models.Model):
    """Event type object."""
    type = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.type


class Event(models.Model):
    """Event object."""
    title = models.CharField(max_length=255)
    type = models.ForeignKey(
        EventType,
        on_delete=models.SET_NULL, 
        null=True
        )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Room(models.Model):
    """Room object."""    
    event = models.ForeignKey(
        Event,        
        on_delete=models.SET_NULL,
        null=True,
        blank=True,        
        )
    title = models.CharField(max_length=255)
    capacity = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    """Room object."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,        
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        Room,        
        on_delete=models.SET_NULL,
        null=True        
        )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.name
