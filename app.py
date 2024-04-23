from flask import Flask, render_template, request, redirect #importamos lo que necesitamos 
from flask_sqlalchemy import SQLAlchemy

import random

app = Flask(__name__) 
app.app_context().push()
POSTS = []


class BlogPost:
    title: str
    content: str
    author: str
    date_created: str
    id: int

    def create(
        self,
        title,
        content,
        author,
        date_created
    ):
        self.id = random.randint(10000, 99999)
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date_created
        POSTS.append(self)

    def get(self):
        from copy import copy
        return copy(POSTS)
    
    # Como hacer un get específico?
    def get_id(self, id):
        position = None
        for index, post in enumerate(POSTS):
            if post.id == int(id):
                position = index
                break
        return POSTS[position]

    def update(
            self,
            id,
            title=None,
            content=None,
            author=None
        ):
        for post in POSTS:
            if post.id == int(id):
                if title: post.title = title
                elif content: post.content = content
                elif author: post.author = author

    def delete(self, id):
        position = None
        for index, post in enumerate(POSTS):
            if post.id == int(id):
                position = index
                break
        del POSTS[position]

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)