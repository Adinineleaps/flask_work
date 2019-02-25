from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'

db=SQLAlchemy(app)

class Records(db.Model):
   	name = db.Column(db.String(100),primary_key=True, nullable=False)
   	dob = db.Column(db.String(50))
	 
	def __repr__(self):
        	return "<Record: {}>".format(self.name)

class New(db.Model):
   	edu = db.Column(db.String(100),primary_key=True, nullable=False)
   	course = db.Column(db.String(50))
	 
	def __repr__(self):
        	return "<New: {}>".format(self.edu)

@app.route('/',methods=['POST','GET'])
def page1():
    return render_template('page1.html')

@app.route('/page2',methods=['POST','GET'])
def page2():
	if request.form:
		record1=Records(name=request.form.get('username'),dob=request.form.get('dob'))
		db.session.add(record1)
		db.session.commit()
	records = Records.query.all()
    	return render_template('page2.html',records=records)

@app.route('/page3a',methods=['POST','GET'])
def page3a():
	#if request.form:
		#new=New(edu=request.form.get('colg_name'),course=request.form.get('course'))
		#db.session.add(new) 
		#db.session.commit()
    	return render_template('page3a.html')


@app.route('/page3b',methods=['POST','GET'])
def page3b():
    return render_template('page3b.html')


@app.route('/page4a',methods=['POST','GET'])
def page4a():
	if request.form:
		new=New(edu=request.form.get('colg_name'),course=request.form.get('course'))
		db.session.add(new) 
	db.session.commit()
	news = New.query.all()
	record=Records.query.all()
	return render_template('page4a.html',news=news,records=record )
















if __name__ == '__main__':
   app.run(debug=True)
