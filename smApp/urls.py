from django.urls import path
from smApp import views


urlpatterns = [
    path('', views.index,name= 'index'),
    path('signin', views.signin,name = 'signin'),
    path('logout_view', views.logout_view,name = 'logout_view'),
    path('signup',views.signup,name = 'signup'),
    path('staff_signup',views.staff_signup,name = 'staff_signup'),
    path('adminHomePage',views.adminHomePage,name = 'adminHomePage'),

    path('staff_list',views.staff_list,name='staff_list'),

    path('user_home',views.user_home,name='user_home'),
    path('staff_home',views.staff_home,name='staff_home'),
    path('user_base',views.user_base,name='user_base'),
    path('Monitoring',views.Monitoring,name='Monitoring'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('users_list',views.users_list,name='users_list'),
    path('approve_user/<int:user_id>/', views.update_approval_status, name='update_approval_status'),
    path('admin_view_users/<int:user_id>/', views.admin_view_users, name='admin_view_users'),
    path('educational_content_view', views.educational_content_view, name='educational_content_view'),
    path('add_educational_content',views.add_educational_content,name='add_educational_content'),
    path('educational_content_view_user', views.educational_content_view_user, name='educational_content_view_user'),
    path('add_collection_shedule', views.add_collection_shedule, name='add_collection_shedule'),
    path('admin_view_collection_shedule', views.admin_view_collection_shedule, name='admin_view_collection_shedule'),
    path('update_collection_schedule/<int:collection_id>/', views.update_collection_schedule, name='update_collection_schedule'),
    path('user_view_collection_shedule', views.user_view_collection_shedule, name='user_view_collection_shedule'),
    path('add_plastic_collection', views.add_plastic_collection, name='add_plastic_collection'),
    path('collected_plastic_details', views.collected_plastic_details, name='collected_plastic_details'),
    path('payment_list', views.payment_list, name='payment_list'),
    path('payment_form/<int:payment_id>/', views.payment_form, name='payment_form'),
    path('payment_success', views.payment_success, name='payment_success'),
    path('payment_confirm/<int:payment_id>/', views.payment_confirm, name='payment_confirm'),
    path('payment_history', views.payment_history, name='payment_history'),
    path('notification', views.notification, name='notification'),
    path('admin_view_payment_list', views.admin_view_payment_list, name='admin_view_payment_list'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),

    path('admin_view_chart', views.admin_view_chart, name='admin_view_chart'),


]