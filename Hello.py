from flask import Flask,render_template,request,make_response
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
   resp=make_response(render_template('result.html',result=sum_1))
   resp.set_cookie('sum_1',str(sum_1))
   return resp

@app.route('/result2',methods = ['POST','GET'])
def result2():
   a=request.form.get('Another Number', type=int)
   sum_1=int(request.cookies.get('sum_1'))
   b=sum_1
   c=a+b
   return render_template("result2.html",result1=str(a))

if __name__ == '__main__':
   app.run(debug=True)
