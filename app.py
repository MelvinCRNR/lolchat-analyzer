from flask import Flask, request, render_template, flash, redirect
from transformers import pipeline

sent_pipeline = pipeline("sentiment-analysis")

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    input_results = sent_pipeline(text)

    if input_results[0]['label'] == 'NEGATIVE' and input_results[0]['score'] > 0.50:
        flash('This message is potentially banishable.')
        return render_template('index.html', text=request.url)
    else:
        flash('This message is not potentially banishable.')
        return render_template('index.html', text=request.url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
