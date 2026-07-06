from flask import Flask, render_template, jsonify, url_for, redirect, request
import string
import random

# db is python file with custom functions
from db import read_data, write_data

app = Flask(__name__)
FILE = "data.json"

@app.route("/")
def home():
    generated_code = request.args.get('code')
    shortened_url = None
    
    if generated_code:
        shortened_url = f"http://127.0.0.1:5000/s/{generated_code}"
        
    return render_template('home.html', code=generated_code, shortened_url=shortened_url)

@app.route("/shorten", methods = ['POST'])
def shorten():
    long_url = request.form.get('original_url')
    
    if not long_url:
        return redirect(url_for('home'))
        
    data = read_data(FILE)

    letters_and_digits = string.ascii_letters + string.digits
    while True:
        generated_code = ''.join(random.choice(letters_and_digits) for i in range(6))
        if generated_code not in data:
            break
        
    data[generated_code] = {"URL" : long_url,
                            "Clicks" : 0}
    write_data(FILE,data)

    return redirect(url_for('home', code=generated_code))

@app.route("/s/<code>")
def orignalURL(code):
    data = read_data(FILE)
    if data.get(code):
        orignalURL = data.get(code).get("URL")
        data[code]["Clicks"] += 1
        write_data(FILE,data)
        return redirect(orignalURL)
    
    return render_template("error.html"), 404
    

@app.route("/dashboard")
def dashboard():
    json_data = read_data(FILE)
    return render_template('dashboard.html', data=json_data)

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/api/links")
def api_links():
    data = read_data(FILE)
    return jsonify(data), 200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)