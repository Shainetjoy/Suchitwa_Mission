from django.contrib import admin
from .models import User,UserProfile,Customer,PlasticCollection,Payment,EducationalResource,PaymentHistory,PlasticCollectionSchedule,Notification
# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Customer)
admin.site.register(PlasticCollection)
admin.site.register(Payment)
admin.site.register(EducationalResource)
admin.site.register(PaymentHistory)
admin.site.register(PlasticCollectionSchedule)
admin.site.register(Notification)
