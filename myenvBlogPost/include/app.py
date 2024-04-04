from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Clave secreta para WTForms

# Almacén de datos en memoria (lista para las publicaciones del blog)
blog_posts = []

class BlogPost:
    def __init__(self, title, content, author):
        self.id = len(blog_posts) + 1  # Genera un ID automático
        self.title = title
        self.content = content
        self.author = author
        self.date_created = datetime.now()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BlogPostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        author = 'Your Name'  # Puedes obtener el autor de la sesión del usuario
        new_post = BlogPost(title, content, author)
        blog_posts.append(new_post)  # Agrega la nueva publicación a la lista en memoria
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, posts=blog_posts)

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])

if __name__ == '__main__':
    app.run(debug=True)
