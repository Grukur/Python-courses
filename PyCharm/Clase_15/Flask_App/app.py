from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
posts = {
    0: {'post_id': 0,
        'title': 'Hacia donde vamos?',
        'content': 'mmm esto es un avance?.... Hell Yeah!!!'
       }
}


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>') # aqui ingresa el int del diccionario, en etse caso 0
def post(post_id):
    post = posts.get(post_id)
    if not post: # post will be None if not found! not None -> True
        return render_template('404.html', message=f'A post with id {post_id} was not found.... dang!')
    return render_template('post.html', post=post)


@app.route('/post/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post', post_id=post_id))
    return render_template('create.html') # este return solo se activa, si el request es tipo GET, si es tipo POST, retorna el if


if __name__ == '__main__':
    app.run(debug=True)
