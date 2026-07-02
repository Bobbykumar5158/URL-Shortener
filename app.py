from flask import Flask , render_template ,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/api/links")
def api_links():
    return jsonify({"data":{"key":"val"}}) # only for example will modify after

if __name__ == "__main__":
    app.run(debug = True)