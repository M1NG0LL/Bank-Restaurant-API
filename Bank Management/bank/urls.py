from django.urls import path
from . import views 

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('', views.login, name="login"),
    path('login_page/<str:id>', views.login_page, name="login_page"),
    path('logout/<str:id>', views.logout, name="logout"),
    # path('email_auth', views.email_auth, name="email_auth"),
    
    #Functions ==================================
    
    path('deposit/<str:id>', views.deposit, name="deposit"),
    path('withdraw/<str:id>', views.withdraw, name="withdraw"),
    path('show_info/<str:id>', views.show_info, name="show_info"),

]
