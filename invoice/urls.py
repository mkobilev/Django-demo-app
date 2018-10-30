from django.urls import path
from invoice import views

urlpatterns = [

    path('customers/', views.customers_list),


]

"""


    path('customers/<int:pk>/', views.snippet_detail),

    path('products/', views.snippet_list),
    path('products/<int:pk>/', views.snippet_detail),

    path('invoices/', views.snippet_list),
    path('invoices/<int:pk>/', views.snippet_detail),
    path('invoices/<int:pk>/items/', views.snippet_list),
    path('invoices/<int:pk>/items/<int:pk>', views.snippet_detail),
    
"""