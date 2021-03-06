from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
	return render_template("index.html")

#Create a new user
@app.route('/user/<name>')

def user(name):
	pizza = ["cheese", "red suace", "sausage", "mushroom"]
	return render_template("name.html", name=name, pizza=pizza)

#website for a new customer
@app.route('/newcustomer')
def newCustomer():
	return render_template("newcustomer.html")

#website for a returning customer
@app.route('/returningcustomer')
def returningCustomer
	return render_template("returningcustomer.html")
	
#Create invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#internal server error (Test)
@app.errorhandler(500)
def internal_server_error(e):
		return render_template("500.html"), 500