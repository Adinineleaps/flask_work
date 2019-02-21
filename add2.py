from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def Add():
   return render_template('Calci.html')

@app.route('/result',methods = ['POST','GET'])
def result():
   a= request.form.get('First Number',type=int)
   b= request.form.get('Second Number',type=int)
   sum_1=a+b
   return render_template('result.html',result=str(sum_1))

@app.route('/result2',methods = ['POST','GET'])
def result2():
   a=request.form.get('Another Number',type=int)
   b=request.args.get('result',type=int)
   return render_template("result2.html",result=str(b))

if __name__ == '__main__':
   app.run(debug=True)
