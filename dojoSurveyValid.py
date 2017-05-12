from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def landingPage():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/submit')

@app.route('/submit')
def submit():
    return render_template("submit.html", name=session['name'], location=session['location'], language=session['language'], comments=session['comments'])

app.run(debug = True)
