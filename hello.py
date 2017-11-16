from flask import Flask, flash, render_template, request, session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField,DateField
#import pandas_highcharts
from flask import Markup
from model import dataformatview


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'this is a secret'

class ReusableForm(Form):
    name = TextField('Company Name:', validators=[validators.required()])
    date_stock = DateField('Date:', validators=[validators.required()],format='%Y-%b-%d')
 
@app.route('/index',methods = ['GET','POST']) 
@app.route("/", methods=['GET', 'POST'])
def hello(chartID = 'chart_id',chart_type = ''):
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        
 
        if form.validate():
            flash('Hello ' + name)
        else:
            flash('Error: All the form fields are required. ')
   
 
    return render_template('test.html', form=form)

@app.route('/chart',methods=['GET','POST'])
def chart(chartID = 'chart_id',chart_type = ''):
	form = ReusableForm(request.form)
	#print (form.errors)
	
	if request.method == 'POST':
		name=request.form['name']
		date_stock = request.form['date_stock']
		print(date_stock)
		if form.validate():
			val = 1
			labels = ["Positive","Neutral","Negative"]
			values = dataformatview.getValuesList(name,date_stock)
			colors = [ "#46BFBD", "#FDB45C","#F7464A" ,]
			return render_template('chart.html', val=val,set=zip(values, labels, colors),cname=name,datestock=date_stock,form=form,pos=values[0],neut=values[1],neg=values[2])		
		else:
			val = 2
			#flash('Error: All the form fields are required. ')
			return render_template('chart.html', val=val, form=form)
	else:
		val = 0
		return render_template('chart.html', val=val,form=form)

	#return render_template('chart.html', set=zip(values, labels, colors),cname='Apple',form=form)

if __name__ == "__main__":
    app.run(debug=True,passthrough_errors=True)