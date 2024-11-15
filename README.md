DRFBasics is a Django REST Framework project designed to showcase the implementation of various CRUD operations using different types of views—function-based views, class-based views, and mixins. This project serves as an introductory guide to understanding and utilizing Django REST Framework's capabilities for building RESTful APIs, featuring operations on models such as Students, Employees, Products, and Sales.

### Student List API Endpoint
The following screenshot shows the response from the /api/v1/students/ endpoint, which lists all students currently stored in the database. This endpoint supports both GET (to retrieve the list of students) and POST (to add a new student) methods, showcasing the basic functionality of a RESTful API using Django REST Framework.

![Screenshot (220)](https://github.com/user-attachments/assets/8739be4e-fdde-473a-9e22-71de58ea4be3)



### Student Detail API Endpoint
The following screenshot shows the response from the /api/v1/student/1/ endpoint. This endpoint allows you to perform GET, PUT, and DELETE operations on a specific student record based on their primary key (pk). It is used for retrieving details, updating data, or deleting a particular student.

![Screenshot (221)](https://github.com/user-attachments/assets/7a16ac1d-ee91-4b46-a297-7ecb812d2251)



Blogs API Endpoint
The following screenshot shows the response from the /api/v1/blogs/ endpoint, which provides a list of all blog posts or allows the creation of new posts. This endpoint supports both GET and POST methods.

![Screenshot (222)](https://github.com/user-attachments/assets/2b01a703-7685-4451-9871-760b7f98ddef)



Comments API Endpoint
The following screenshot shows the response from the /api/v1/comments/ endpoint, which provides a list of all comments or allows adding new comments. This endpoint supports both GET and POST methods.

![Screenshot (223)](https://github.com/user-attachments/assets/9b04ed38-95ab-4684-a2c6-656693686e95)




Books API Endpoint with Filter Capability
The following screenshot shows the response from the /api/v1/books/ endpoint, which provides a list of all books or allows the creation of new books. This endpoint has pagination and filter capabilities, allowing you to view books page by page and filter by title.

![Screenshot (224)](https://github.com/user-attachments/assets/c516e831-d711-420a-bc88-0bce86d14ae6)




Blogs API Endpoint with Search Capability
The following screenshot shows the response from the /api/v1/blogs/ endpoint, which provides a list of all blog posts or allows the creation of new posts. This endpoint includes pagination, search, and ordering functionalities to enhance the way blog data can be retrieved.

![Screenshot (225)](https://github.com/user-attachments/assets/f2c9ddc1-3ef1-4164-979a-a5bade270512)


