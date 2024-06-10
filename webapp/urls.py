from django.urls import path

from webapp import views

urlpatterns=[
    path('',views.homepage,name="home"),
    path('about/',views.aboutpage,name="about"),
    path('contact/',views.contactpage,name="contact"),
    path('Our_products/',views.Our_products,name="Our_products"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('singlepage/<int:proid>/',views.singlepage,name="singlepage"),
    path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
    path('register_page/',views.register_page,name="register_page"),
    path('save_register/',views.save_register,name="save_register"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('user_login_page/',views.user_login_page,name="user_login_page"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('delete_item/<int:pid>/', views.delete_item, name="delete_item"),
    path('payment_page', views.payment_page, name="payment_page"),
    path('save_payment', views.save_payment, name="save_payment"),

]