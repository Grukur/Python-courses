from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

llist1 = ['Rob', 'Anna', 'Raul', 'Jose']

@app.route('/<name>')
def home(name):
    return render_template('test_1.html', content=name, lista=[llist1])



# @app.route('/<name>')
# def user(name):
#     return f'Hello {name}'
#
# @app.route('/admin')
# def admin():
#     return redirect(url_for('user', name='Admin!'))

if __name__ == '__main__':
    app.run()

