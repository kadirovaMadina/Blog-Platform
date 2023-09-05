# Blog Platform


Welcome to the **Blog Platform** project! This project was created to develop a RESTful API using the Django REST Framework to manage and provide blog related resources.


## Project Goals

- Development of a powerful API for managing blog posts, comments and users.
- Providing an easy way to create, edit and delete blog posts.
- Implementation of a system of likes and dislikes for rating posts.
- Providing a friendly user interface for working with the API through Swagger.

## Technologies used

- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) Django: Powerful Python web framework.
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) Django REST Framework: A library for building APIs based on Django.
- ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) Swagger: A tool for creating interactive API documentation.

---

## Entities

The Blog Platform project consists of the following objects:

1. User:
    - Nickname: generated based on the user's email.
    - E-mail: the user's e-mail address.
    - Password: user's password.
    - Role: the role of the user (admin or user).
    - Additional profile information such as name, contact details, etc.



2. Post (represents a post published by the user):
    - Title: title for the post.
    - Description: description of the post.
    - Photo: The image that the user pinned when creating a post.
    - User: the user who posted the post (the user's foreig key).
    - Date: The date and time the post was created.
    


3. Comments (represents the text that the user left on the post):
      - Text: the text that the user left.
      - User: the user who wrote the comment (the user's foreign key).
      - Post: the post that was commented on (foreign key of posts).
      - Date: the date and time the comment was created.


## Features

1) Registration and Authentication: Users can register on the platform and authorize through token authentication to access secure parts of the API.

2) User Management: Administrators can manage users, assign different roles and rights to them (eg administrator, normal user).

3) Post Management: Users can create, view, update and delete blog posts. They can add a title, content, images, videos, and specify a category for each entry.

4) Commenting on Posts: Users can leave comments on blog posts. They can also manage their comments, edit and delete them.


7) API documentation: The platform provides API documentation using Swagger. Users can see available APIs and their options.

8) Pagination and Filtering: Post and comment lists support pagination, which improves performance and usability. An option to filter by various parameters is also available.

9) Access Rights Protection: Users have access only to those functions for which they have the appropriate rights. For example, only the creator of the post, administrators, and moderators can edit or delete posts.

## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

---

## How to start
1) Clone the repository: 
```
git clone https://github.com/kadirovaMadina/Blog-Platform.git
```
2) Create a virtual environment: 
```
python -m venv .venv
```
3) Activate the virtual environment: 
```
source .venv\Scripts\activate.bat
```
4) Install dependencies: 
```
pip install -r requirements.txt
```
5) Run make migrations: 
```
python manage.py makemigrations
```
6) Run migrate: 
```
python manage.py migrate
```
6) Load fixtures:
```
python manage.py load_users
python manage.py load_posts
python manage.py load_comments
```
7) Run the development server: 
```
python manage.py runserver
```
Open admin panel [localhost:8000/admin](http://localhost:8000/admin)

Default admin: admin@example.com

Default password: admin

Open Swagger API documentation [localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)


