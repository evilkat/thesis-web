from flask import Flask, flash, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#import pandas_highcharts
from flask import Markup




app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'this is a secret'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
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

@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'Pie_Chart', chart_height = 350):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

@app.route('/chart')
def chart():
	labels = ["January","February","March","April","May","June","July","August"]
	values = [10,9,8,7,6,4,7,8]
	colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
	return render_template('chart.html', set=zip(values, labels, colors))

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=80,passthrough_errors=True)