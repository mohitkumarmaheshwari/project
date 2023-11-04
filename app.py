#2. Create a Flask app that consumes data from external APIs and displays it to users.
#Try to find an public API which will give you a data and based on that call it and deploy it on cloud platform
# Import required libraries
import requests
from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        user_id = request.form['user_id']
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        response = requests.get(url)
        if response.status_code == 200:
            user_data = response.json()
        else:
            user_data = None
    return render_template('index.html', user_data=user_data)

# Run the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5000)
