from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class Mymanager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError("users must have an email")
    
        
        
        
        if not username:
            raise ValueError("enter username")
        
        user = self.model(
              email = self.normalize_email(email),
           
      
              username = username
             

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
         
        user = self.create_user(
              email = self.normalize_email(email),
        
              username=username,
             
            
              password = password
        ) 
        user.is_admin = True
      
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
       


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,blank=True,unique=True)
    username = models.CharField(max_length=30,unique=True)
    last_login = models.DateTimeField(verbose_name="last_login",auto_now=True)
    date_joined = models.DateTimeField(verbose_name="date_joined",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
  
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        
       
        'email',
       
      ]
    objects = Mymanager()

    def __str__(self):
        return self.username 

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_lable):
        return True    


   

 