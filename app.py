from flask import Flask, render_template, request, redirect, url_for

# I used the first link to help me set up flask. The second link I used to learn how to do post and get methods.
# The last link I used to learn how to better structure my CSS and HTML to make it pop out a bit.
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
# https://sparkdatabox.com/tutorials/python-flask/get-and-post-methods-in-flask
# https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML

# sets app variable to create the instance of Flask so that it can run
app = Flask(__name__)

# returns to the login page
@app.route('/')
def login():
    return render_template('login_page.html')


# this is where my post and method actions are
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        # gets data from the form section of login_page.html
        username = request.form['username']
        password = request.form['password']

        # redirects to the success page
        return redirect(url_for('success_page', username=username))
    else:
        # redirects to the home page
        return redirect(url_for('login'))

# redirects to the html page with the buttons and links
@app.route('/success/<username>')
def success_page(username):
    return render_template('diff_page.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
