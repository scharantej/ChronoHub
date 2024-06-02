
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///watches.db'
db = SQLAlchemy(app)

# Define the Watch model
class Watch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))
    price = db.Column(db.Float, nullable=False)

# Create the home page route
@app.route('/')
def home():
    # Get all watches from the database
    watches = Watch.query.all()

    # Render the home page with the list of watches
    return render_template('index.html', watches=watches)

# Create the search route
@app.route('/watches/search', methods=['GET'])
def search():
    # Get the search term from the request
    term = request.args.get('term')

    # Search for watches that match the search term
    watches = Watch.query.filter(Watch.name.like('%' + term + '%')).all()

    # Render the search results page
    return render_template('index.html', watches=watches)

# Create the watch detail route
@app.route('/watches/<int:watch_id>')
def watch_detail(watch_id):
    # Get the watch with the specified ID
    watch = Watch.query.get_or_404(watch_id)

    # Render the watch detail page
    return render_template('watch-detail.html', watch=watch)

# Create the cart route
@app.route('/cart')
def cart():
    # Get the items in the cart
    items = []

    # Render the cart page
    return render_template('cart.html', items=items)

# Create the add to cart route
@app.route('/cart/add/<int:watch_id>', methods=['POST'])
def add_to_cart(watch_id):
    # Add the watch to the cart
    items.append(watch_id)

    # Redirect to the cart page
    return redirect(url_for('cart'))

# Create the remove from cart route
@app.route('/cart/remove/<int:watch_id>', methods=['POST'])
def remove_from_cart(watch_id):
    # Remove the watch from the cart
    items.remove(watch_id)

    # Redirect to the cart page
    return redirect(url_for('cart'))

# Create the checkout route
@app.route('/checkout')
def checkout():
    # Render the checkout page
    return render_template('checkout.html')

# Create the submit checkout route
@app.route('/checkout/submit', methods=['POST'])
def submit_checkout():
    # Process the checkout information
    flash('Your order has been placed!')

    # Redirect to the home page
    return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
