DRFBasics is a Django REST Framework project designed to showcase the implementation of various CRUD operations using different types of views—function-based views, class-based views, and mixins. This project serves as an introductory guide to understanding and utilizing Django REST Framework's capabilities for building RESTful APIs, featuring operations on models such as Students, Employees, Products, and Sales.

### Student List API Endpoint
The following screenshot shows the response from the /api/v1/students/ endpoint, which lists all students currently stored in the database. This endpoint supports both GET (to retrieve the list of students) and POST (to add a new student) methods, showcasing the basic functionality of a RESTful API using Django REST Framework.
![Screenshot (220)](https://github.com/user-attachments/assets/8739be4e-fdde-473a-9e22-71de58ea4be3)



### Student Detail API Endpoint
The following screenshot shows the response from the /api/v1/student/1/ endpoint. This endpoint allows you to perform GET, PUT, and DELETE operations on a specific student record based on their primary key (pk). It is used for retrieving details, updating data, or deleting a particular student.

![Screenshot (221)](https://github.com/user-attachments/assets/7a16ac1d-ee91-4b46-a297-7ecb812d2251)
