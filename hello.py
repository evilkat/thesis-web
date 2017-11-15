from flask import Flask, flash, redirect, render_template, request, session, abort
from wtforms import Form, TextField, TextArea, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'this is a secret'

class ReusableForm(Form):
	cname = TextField('Company Name: ',validators=[validators.required()])

@app.route("/")
def index():
	return "Index"

@app.route("/hello")
def hello():
	return "hello"

@app.route("/tweet",methods=['Get','POST'])
def tweet():
	form = ReusableForm(request.form)
	print(form.errors)

	if request.method == 'POST':
		name=request.form[cname]
		print(name)

		if form.validate():
			flash('Hello ' + name)
	return "tweet"

@app.route("/tweet/<string:name>/")
def gettweetname(name):
	return render_template('test.html',name=name) 

if __name__=="__main__":
	app.run(host='0.0.0.0',port=80)