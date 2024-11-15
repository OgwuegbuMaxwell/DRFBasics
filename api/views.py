from typing import List
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from blogs.models import Blog, Comment
from books.models import Book
from customers.models import Customer
from employees.models import Employee
from products.models import Product
from sales.models import Sale
from students.models import Student
from .serializers import StudentSerializer, EmpployeeSerializer, ProductSerializer, SaleSerializer, CustomerSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter


from blogs.serializers import BlogSerializer, CommentSerializer

from .paginations import CustomPagination
from books.filters import BookFilter

######### Function Based Views #########

# # Manual serializer
# def studentsView(request):
#     students = Student.objects.all()
#     students_list = list(students.values())
#     return JsonResponse(students_list, safe=False)


# Function-based view to handle Student data using Django REST Framework
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        # Get all the data from the students table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Function-based view to handle specific Student record based on primary key (pk)
@api_view(['GET', 'PUT', 'DELETE'])
def studentDataView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        # Update existing Data
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    


######### Class Based Views #########

# Class-based views for handling Employee data
# Class based views do not require decorators
class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmpployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmpployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class-based view to handle specific Employee record based on primary key (pk)
class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return employee
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmpployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serilizer = EmpployeeSerializer(employee, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_200_OK)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




########### Using Mixins ############

# Using mixins to create a reusable view for Products
class Products(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


# Using mixins to manipulate single Product details
class ProductDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
    
    
    
########## Generics ###########

# Using generics to list and create Sales objects

# class Sales(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Sale.objects.all()
#     serializer_class = SaleSerializer

# Another way of listing and creating the objects
class Sales(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


# Using generics to retrieve, update, and delete Sale objects
class SaleDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = 'pk'




################### Viewset ###################

# CustomerViewset class provides methods to list, create, retrieve, update, and delete Customer objects.
# It is useful for handling customer-related operations through a RESTful API using ViewSets.
class CustomerViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, response, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



########## ModelViewSet ##########

# BookViewset class extends ModelViewSet to provide complete CRUD operations for Book objects.
# This class leverages Django REST Framework's ModelViewSet to simplify API view creation for books.
class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Use custom pagination for book listing
    pagination_class = CustomPagination
    
    # support for filter
    
    # usimg gloabal filter
    # filterset_fields = ['title']
    
    # Using custom filter
    filterset_class = BookFilter



############ Nested Serializers #############

# BlogsView provides a list and create view for Blog objects.
# It allows clients to create a new blog post or list all available blog posts, showcasing nested relationships with comments.
class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title', 'blog_body']
    ordering_fields = ['id', 'blog_title']


# CommentsView provides a list and create view for Comment objects.
# It is used to add or list comments, which can be associated with a specific blog post.
class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# BlogDetailView provides retrieve, update, and delete functionality for Blog objects.
# This view allows clients to retrieve a single blog post, update its details, or delete it.
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'


# CommentDetailView provides retrieve, update, and delete functionality for Comment objects.
# This view is useful to manage individual comments, providing access to retrieve, update, or delete a specific comment.
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'