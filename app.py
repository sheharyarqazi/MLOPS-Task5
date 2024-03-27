from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient('mongodb://localhost:27017')
db = client['mlops-task5']  # Specify your database name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Insert into MongoDB
        user_data = {'name': name, 'email': email}
        db.users.insert_one(user_data)
        
        return jsonify({'message': 'Data submitted successfully!'})
    else:
        return jsonify({'error': 'Method Not Allowed'}), 405

if __name__ == "__main__":
    app.run(debug=True)
