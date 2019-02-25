from flask import Flask, render_template,request

import matplotlib.pyplot as plt
import quandl
import io
import base64
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def page1():
    return render_template('plot.html')

@app.route('/show',methods=['POST','GET'])
def show():
    name=request.form.get('comp',type=str)
    data=quandl.get(name, start_date="2017-12-31", end_date="2018-12-31", authtoken="i8-Cu-sh5vgP2VpC_fX7")
    data.Close.plot()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return '<img src="data:image/png;base64,{}">'.format(plot_url)


if __name__ == '__main__':
    app.debug = True
    app.run()