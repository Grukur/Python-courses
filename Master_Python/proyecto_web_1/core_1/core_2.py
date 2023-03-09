from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('template_1.html')

@app.route('/test')
def test():
    return render_template('template_2.html')

@app.route('/post', methods=['POST', 'GET'])
def posting():
    return render_template()

@app.route('/<usr>')
def user(usr):
    return render_template()



if __name__ == '__main__':
    app.run(debug=True)