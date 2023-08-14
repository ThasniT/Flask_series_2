# import the Flask library
from flask import Flask, render_template, request
 
 
# Create the Flask instance and pass the Flask constructor the path of the correct module
app = Flask(__name__)
 
 
@app.route('/', methods=['GET', 'POST'])
def squarenumber():
 # If method is POST, get the number entered by user
 # Calculate the square of number and pass it to answermaths
    if request.method == 'POST':
        if(request.form['num'] == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            number = request.form['num']
            sq = int(number) * int(number)
            return render_template('answer.html',
                            squareofnum=sq, num=number)
    # If the method is GET,render the HTML page to the user
    if request.method == 'GET':
        return render_template("squarenum.html")
 
 
# Start with flask web app with debug as True only
# if this is the starting page
if(__name__ == "__main__"):
    app.run(debug=True)