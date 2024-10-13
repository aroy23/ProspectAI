from flask import Flask, render_template, request, jsonify
from logins import *
import os

app = Flask(__name__, 
            static_folder="../frontend/static",
            template_folder="../frontend/templates")

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/add_user')
# def add_user(username, email, password):
#     try:
#         db_add(username, email, password)
#     except sqlite3.IntegrityError as e:
#         if e == 'UNIQUE constraint failed: user_data.username':
#             return jsonify({'error': 'Username already in use!'})
#         elif e == 'UNIQUE constraint failed: user_data.email':
#             return jsonify({'error': 'Email already in use!'})

@app.route('/login_page', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        if db_login(username, password):
            return render_template('homepage.html')
        else:
            return render_template('login.html')
    except TypeError as e:
        return jsonify({'error': 'Enter both email and password!'})
    
@app.route('/signup_page', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        db_add(username, email, password)
        return render_template('login.html')
    except sqlite3.IntegrityError and TypeError as e:
        if e == 'UNIQUE constraint failed: user_data.email':
            return jsonify({'error': 'Email is already in use!'})
        elif e == 'UNIQUE constraint failed: user_data.username':
            return jsonify({'error': 'Username is already in use!'})
        else:
            return jsonify({'error': e})

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    return 0

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(debug=True, port=8080)