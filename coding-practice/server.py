from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    
    return render_template('form.html')

@app.route('/results')
def show_results():
    
    return render_template('results.html')

@app.route('/save-name', methods=['POST']):
def save_name():
    """submits user input(name) to this route and adds it to a session w/ key: name
    and redirects to homepage"""

    user = request.form.get('name')
    saved_user = session[user]

    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

