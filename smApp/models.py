from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_user = models.BooleanField(default=False)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for user profile (e.g., address, phone number, etc.)

class Customer(models.Model):
    APPROVAL_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer')
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='customer_images/', null=True, blank=True)
    approve = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default='pending')

    def __str__(self):
        return self.name


class PlasticCollection(models.Model):
    PAYMENT_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]
    user_id = models.CharField(max_length=50,null=True)
    place = models.CharField(max_length=50,null=True)
    date = models.DateField()
    time = models.TimeField(null=True)
    amount_collected = models.DecimalField(max_digits=100, decimal_places=2,null=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='pending')
    plastic_amount = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.place

class Payment(models.Model):
    user_id = models.CharField(max_length=50,null=True)
    payment_id = models.CharField(max_length=50,null=True)
    cardNumber = models.CharField(max_length=50,null=True)
    cardDate = models.CharField(max_length=50,null=True)
    cvc = models.CharField(max_length=50,null=True)
    nameOnCard = models.CharField(max_length=50,null=True)
    streetAddress = models.CharField(max_length=50,null=True)
    zipCode = models.CharField(max_length=50,null=True)
    date = models.DateField(auto_now_add = True,null=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    
    def __str__(self):
        return self.user_id


class EducationalResource(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='educational_resources/', null=True, blank=True)
    def __str__(self):
            return self.title

class PlasticCollectionSchedule(models.Model):
    place = models.CharField(max_length=50,null=True)
    date = models.DateField()
    time = models.TimeField(null=True)
    amount_collected = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    def __str__(self):
        return self.place

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    # Additional fields related to notifications
