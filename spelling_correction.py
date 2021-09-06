from flask import Flask, render_template, request
from textblob import TextBlob

# initialse the application
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit' , methods = ["POST"])
def form_data():
   input_text = request.form.get('input_text')
   g = TextBlob(input_text)
   corrected_text = g.correct()

   
   return render_template('predict.html' , corrected_data = f' {corrected_text}')
#    return render_template('predict.html' , sentence_data = f'Number of sentences are {sentence_length}')
if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host = '0.0.0.0',port = 8080)

