from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class Mymanager(BaseUserManager):
    def create_user(self,phone,username,email,select_country,password=None):
        if not email:
            raise ValueError("users must have an email")
        if not phone:
            raise ValueError("phone number is required for business branding")
        if not select_country:
            raise ValueError("select country")
        
        
        
        if not username:
            raise ValueError("enter username")
        
        user = self.model(
              email = self.normalize_email(email),
              phone=phone,
      
              username = username
             

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone,username,email,select_country,password=None):
         
        user = self.create_user(
              email = self.normalize_email(email),
              phone=phone,
              username=username,
              select_country = select_country,
            
              password = password
        ) 
        user.is_admin = True
      
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
       


class Account(AbstractBaseUser):
    CHOICES= (
        ('kenya', 'kenya'),
        ('Tanzania', 'Tanzania'),
        ('Ghana', 'Ghana'),
         ('lesotho', 'Lesotho'),
        ('Tanzania', 'Tanzania'),
        ('mozambique', 'mozambique'),
         ('D.R.C', 'D.R.C'),
        
        
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone=models.CharField(validators=[phone_regex],max_length=13,blank=False,unique=True)
    select_country =models.CharField(choices=CHOICES,max_length=200,blank=False,default="Kenya")
    email = models.EmailField(verbose_name="email",max_length=60,blank=True,unique=True)
    username = models.CharField(max_length=30,unique=True)
    last_login = models.DateTimeField(verbose_name="last_login",auto_now=True)
    date_joined = models.DateTimeField(verbose_name="date_joined",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    has_paid = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = [
        
       
        'email',
       
        'username',
        'select_country'
    
        
        ]
    objects = Mymanager()

    def __str__(self):
        return self.username + self.phone

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_lable):
        return True    


   

 