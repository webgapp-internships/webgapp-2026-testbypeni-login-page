from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('forms/',views.forms, name="forms"),
    path('table/', views.table, name="table"),
    path('table_edit/<int:id>', views.table_edit, name="table_edit"),
    path('table_delete/<int:id>', views.table_delete, name="table_delete"),
    path('downloadtotalemployee_excel',views.downloadtotalrecord_excel,name='downloadtotalrecord_excel'),
    path('logout/', views.logout,name="logout"),
]
