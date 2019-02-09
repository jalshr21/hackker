"#hello world#" 
from flask import Flask, request, render_template  # Here, we load the Flask python package
import webbrowser

# Now, let's create our app. A Flask application is created by running
# Flask(__name__) and assigning it to a variable. In this case: app
app = Flask(__name__)

# Now that our server is created, let's configure it.
# First, we'll create a server path.
# Our first path will be '/say_hello'


@app.route('/say_hello', methods=('GET', 'POST'))  # This is how you create a path in Flask
def hello():  # Here, we create a function for the /say_hello path
    # Any code indented by four spaces from this point on will run
    # when a client requests our server at the '/say_hello' path
    #
    # We want to make sure everything is working, so let's return
    # some data!
    # Flask will take the data after return, and translate it into
    # an HTTP response.

    if request.method == 'GET':
        return render_template("tmp.html")
    animal = request.form['animal']
    if not animal:
        return 'Error: No animal provided'
    if animal == 'dog':
        image_url = "https://d17fnq9dkz9hgj.cloudfront.net/uploads/2018/04/Frenchie_05.jpg"
    elif animal == 'cat':
        image_url = "https://data.whicdn.com/images/298844185/large.jpg?t=1507433077"
    else:
        image_url = 'https://img.purch.com/h/1000/aHR0cDovL3d3dy5saXZlc2NpZW5jZS5jb20vaW1hZ2VzL2kvMDAwLzAwOS82Nzkvb3JpZ2luYWwvMDkwNTExLXBsYXR5cHVzLTAyLmpwZw=='


    # say hello, with the user's animal name included
    return '''
        <h1>Hello {animal_name}!</h1>
        <image style="width: 100%" src="{image_src}" />
    '''.format(animal_name=animal, image_src=image_url)

# new code below
@app.route('/')
def index():
    return 'Welcome to the server root with changes'
