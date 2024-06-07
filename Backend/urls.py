from django.urls import path
from Backend import views

urlpatterns=[
    path('main_page/',views.main_page,name="main_page"),
    path('category_page/', views.category_page, name="category_page"),
    path('details_page/', views.details_page, name="details_page"),
    path('show_category/', views.show_category, name="show_category"),
    path('edit_page/<int:catid>/', views.edit_page, name="edit_page"),
    path('update_category/<int:catid>/', views.update_category, name="update_category"),
    path('delete_category/<int:catid>/', views.delete_category, name="delete_category"),
    path('login_page/',views.login_page,name="login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('pro_page/', views.pro_page, name="pro_page"),
    path('pdetails_page/', views.pdetails_page, name="pdetails_page"),
    path('show_products/', views.show_products, name="show_products"),
    path('edit_product/<int:proid>/', views.edit_product, name="edit_product"),
    path('update_products/<int:proid>/', views.update_products, name="update_products"),
    path('delete_products/<int:proid>/', views.delete_products, name="delete_products"),
    path('delete_contact/<int:conid>/', views.delete_contact, name="delete_contact"),
    path('contact_data/', views.contact_data, name="contact_data"),

]
