from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Defining the home page of our site
@app.route("/home")  
def home():
	return render_template("index.html")

@app.route("/pricing") 
def pricing():
	return render_template("pricing.html")

@app.route("/about")  
def about():
	return render_template("about.html")

@app.route("/")
def nothing():
	return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)