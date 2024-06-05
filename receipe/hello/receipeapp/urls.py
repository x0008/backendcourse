from django.contrib import admin
from django.urls import path,include
# from about import views
from receipeapp import views
# from result1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('receipe.urls'))
    # path('',views.home,name="home"),
    path('',views.new,name="new"),
    path('receipe/',views.main_page,name="main_page"),
    path('getreceipe/',views.view_page,name="view_page"),
    path('delete-recipe/<id>',views.delete_recipe,name="delete_page"),
    path('update-recipe/<id>',views.update_recipe,name="update_page"),
    # path('result/',result_page1,name="result"),
    path('login/',views.login_page,name="result"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_page,name="register")








]