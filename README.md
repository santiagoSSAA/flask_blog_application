# Backend Development Exercise: Building a Simple Blog Application

<img src="https://raw.githubusercontent.com/cat-milk/Anime-Girls-Holding-Programming-Books/master/Python/Drunk_Kobayashi_Python.png" alt="Image Description" width="400" height="200">

**Exercise: Building a Simple Blog Application**

In this exercise, you'll create a basic blog application using Flask, a popular Python web framework. The application will allow users to create, read, update, and delete blog posts.

**Prerequisites:**
- Basic knowledge of Python
- Understanding of HTML and CSS (for rendering templates)

## Step 1: Set up the Flask Environment
1. Install Flask using pip: `pip install flask`
2. Create a new Python file called `app.py`.

## Step 2: Create a Blog Post Model
1. In `app.py`, create a `BlogPost` class that represents a blog post.
2. The `BlogPost` class should have attributes like `title`, `content`, `author`, `date_created`, and a unique `id`.
3. Implement methods to create, update, and delete blog posts.

## Step 3: Create a Data Store
1. Create an in-memory data store (e.g., a list or dictionary) to store the blog posts.
2. Implement functions to interact with the data store, such as adding a new post, retrieving all posts, getting a post by ID, updating a post, and deleting a post.

## Step 4: Create Flask Routes
1. In `app.py`, create Flask routes for handling the following operations:
  - `/`: Render an HTML template that displays all blog posts.
  - `/create`: Render an HTML form for creating a new blog post.
  - `/post/<int:post_id>`: Render an HTML template that displays a specific blog post.
  - `/update/<int:post_id>`: Render an HTML form for updating an existing blog post.
  - `/delete/<int:post_id>`: Delete a blog post from the data store.

## Step 5: Create HTML Templates
1. Create HTML templates for rendering the blog posts and forms.
2. Use Jinja2 templating engine (included with Flask) to dynamically render the content.

## Step 6: Run the Flask Application
1. In `app.py`, add the following code to run the Flask application:

```python
if __name__ == '__main__':
   app.run(debug=True)
```

2. Run the application using `python app.py`.
3. Access the application in your web browser at `http://localhost:5000`.

## Step 7: Enhance the Application (Optional)
1. Implement form validation for creating and updating blog posts.
2. Add support for user authentication and authorization.
3. Store blog posts in a database (e.g., SQLite, PostgreSQL) instead of an in-memory data store.
4. Implement pagination for displaying blog posts.

## EVALUATION CRITERIA
- &#9989; Can run the project from different device & runs OK.
- &#9989; Can access to all endpoints without problems.
- &#9989; Can create a blogpost in project when running local.
- &#9989; Can request all blogposts from project & watch a HTML render with info.
- &#9989; Can update a specific blogpost & check new changes from GET render.
- &#9989; Can delete a specific blogpost & check in GET render.
