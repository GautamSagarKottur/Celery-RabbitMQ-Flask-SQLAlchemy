from factory import create_app
import tasks

app = create_app()

from flask import request, render_template

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/insertData', methods = ['POST', 'GET'])
def insertData():
    if request.method == 'POST':        
        text = request.form['Path']
        tasks.insert.delay(text)
        return 'Async request sent to insert filenames in Results table!'

if __name__ == '__main__':
    app.run(debug=True)

