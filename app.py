from flask import Flask, render_template, request, jsonify


app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('index.html',result='')

@app.route('/math', methods=['POST'])
def math_operation():
    error_msg = ''
    if (request.method=='POST'):
        operation = request.form['operation']
        try :
            num1 = int(request.form['num1'])

            if operation=='square':
                r = num1**2
                result = 'Square of ' + str(num1) + ' is : ' + str(r)
            if operation=='cube':
                r = num1**3
                result = 'Cube Of ' + str(num1) + ' is : ' + str(r)
            if operation=='factorial':
                tmp = int(1)
                for i in list(range(num1,1,-1)):
                    tmp = tmp * i
                result = 'Factorial Of ' + str(num1) + ' is : ' + str(tmp)
        except Exception as e:
            #if type(num1)==str:
            result = 'Please enter Integer instead of String'
            print('In Except')
            return render_template('index.html')

        return render_template('results.html',result=result)

if __name__ == '__main__':
    app.run()



