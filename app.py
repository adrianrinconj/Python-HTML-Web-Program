from flask import Flask, render_template, request, redirect, url_for

# I used the first link to help me set up flask. The second link I used to learn how to do post and get methods.
# The last link I used to learn how to better structure my CSS and HTML to make it pop out a bit.
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
# https://sparkdatabox.com/tutorials/python-flask/get-and-post-methods-in-flask
# https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login_page.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        # Process data from the form
        username = request.form['username']
        password = request.form['password']

        # Redirect to the success page
        return redirect(url_for('success_page', username=username))
    else:
        # redirects to the home page
        return redirect(url_for('login'))

@app.route('/success/<username>')
def success_page(username):
    return render_template('diff_page.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
