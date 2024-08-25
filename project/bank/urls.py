from django.urls import path
from . import views 

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('', views.login, name="login"),
    path('login_page/<str:id>', views.login_page, name="login_page"),
    path('logout/<str:id>', views.logout, name="logout"),
    
    #acount activation
    path('Account_Activation/<str:email>/', views.account_activate, name='account_activate'),
    path('resend-code/<str:email>/', views.resend_activation_code, name='resend_activation_code'),
    
    #pass reset
    path('pass_reset_knower', views.pass_reset_knower, name="pass_reset_knower"),
    path('pass_reset_code_enter/<str:id>', views.pass_reset_code_enter, name="pass_reset_code_enter"),
    path('pass_reset/<str:id>', views.pass_reset, name="pass_reset"),
    
    #Functions ==================================
    
    path('deposit/<str:id>', views.deposit, name="deposit"),
    path('withdraw/<str:id>', views.withdraw, name="withdraw"),
    path('show_info/<str:id>', views.show_info, name="show_info"),

]
