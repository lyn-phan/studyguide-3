from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

@app.route('/form')
def show_form():
    
    return render_template('form.html')

@app.route('/results')
def show_results():
    
    return render_template('results.html')

@app.route('/results', methods=['POST'])
def receive_results():

    cheery = request.args.get('cheery')
    honest = request.args.get('honest')
    dreary = request.args.get('dreary')

    if cheery and honest and dreary:
        msg = "Do you really?"
    elif cheery and honest:
        msg = "You're a happy camper!"
    elif cheery and dreary:
        msg = "Well, which one is it?"
    elif cheery:
        msg = "Have a jolly good day!"
    elif honest:
        msg = "You should really take a shower today."
    elif dreary:
        msg = "Tomorrow is going to be just like today."
    elif honest and dreary:
        msg = "Are you really in sweats again?"
    else:
        msg = "Time to go on a walk"
    
    return render_template('/results', msg=msg)


@app.route('/save-name', methods=['POST'])
def save_name():
    """submits user input(name) to this route and adds it to a session w/ key: name
    and redirects to homepage"""

    name = request.form.get('name')
    session[name] = name

    return render_template('homepage.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

