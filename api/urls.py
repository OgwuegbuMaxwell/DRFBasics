from django.urls import include, path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('student/<int:pk>/', views.studentDataView),
    
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    
    path('products/', views.Products.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    
    path('sales/', views.Sales.as_view()),
    path('sales/<int:pk>/', views.SaleDetail.as_view()),
]


