from flask import Flask, render_template, url_for, request, redirect
import os
from flask import send_from_directory  # these two lines are for the favicon.ico route
import csv
app = Flask(__name__)  # __name__ is __main__

# endpoints
@app.route("/")  # decorator, < > something that we can pass
def index():  
    print(url_for('static', filename='favicon.ico'))  # prints the URL for the file name
    return render_template('index.html')

@app.route("/<string:page_name>")  
def html_page(page_name):    
    return render_template(page_name) 




@app.route("/favicon.ico")  # decorator
def blog():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

def write_to_file(data):
    with open('database.TXT', mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline ='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])  # Get means the browser wants us to send info, POST is to save information
def submit_form():
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
    except:
        return ('no submitted to database')
    else:
        return redirect('/thankyou.html')
    else:
        "Please go back and try again"



# @app.route("/user/<username>/<int:post_id>")  # decorator, < > something that we can pass , <int: > ask for an int
# def show_user_profile(username = None, post_id = None):  # username = default_username
#     return render_template('index.html', name = username, post_id = post_id)  # the name on the HTML == username

