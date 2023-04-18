from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

# form
#Post: to get data. data is not visible,seccured way to pass data.
#Here we are specifying that we are sending/passing data through POST method by using form
@app.route('/math',methods=['POST'])
def math_ops():
    if (request.method=='POST'):
        ops = request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        #We can perform anything after getting data even we can store in sql,etc
        if(ops=='add'):
            r=num1+num2
            result = f'The sum of {num1} and {num2} is {r}'
        elif(ops=='subtract'):
            r=num1-num2
            result = f'The difference of {num1} and {num2} is {r}'
        elif(ops=='multiply'):
            r=num1*num2
            result = f'The product of {num1} and {num2} is {r}'
        elif(ops=='divide'):
            r=num1/num2
            result = f'The division of {num1} and {num2} is {r}'
        else:
            result = "Choose correct operation"
        return render_template('results.html',result=result)


#Passing data through postman for testing API
@app.route('/postman_action',methods=['POST'])
def math_ops1():
    if (request.method=='POST'):
        ops = request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        if(ops=='add'):
            r=num1+num2
            result = f'The sum of {num1} and {num2} is {r}'
        elif(ops=='subtract'):
            r=num1-num2
            result = f'The difference of {num1} and {num2} is {r}'
        elif(ops=='multiply'):
            r=num1*num2
            result = f'The product of {num1} and {num2} is {r}'
        elif(ops=='divide'):
            r=num1/num2
            result = f'The division of {num1} and {num2} is {r}'
        else:
            result = "Choose correct operation"
        #Instead of getting result in html page we are getting result into same postman and converting result into json or string
        return jsonify(result)


if __name__=="__main__":
    app.run(port=1234,threaded=True) 