from flask import Flask, render_template, request, jsonify
from logins import *
import os
from main import main
import time

app = Flask(__name__, 
            static_folder="../frontend/static",
            template_folder="../frontend/templates")

UPLOAD_FOLDER = './input_videos'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template("index.html")

def clear_upload_folder():
    folder = app.config['UPLOAD_FOLDER']
    
    # Check if the folder exists
    if os.path.exists(folder):
        # Remove all files in the directory
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)  # Remove the file
            except Exception as e:
                print(f"Error removing file {file_path}: {e}")


@app.route('/upload_video', methods=['POST'])
def upload_video():
    clear_upload_folder()
    # Check if the post request has the file part
    if 'video' not in request.files:
        return jsonify({'error': 'No file part in the request'})
    
    file = request.files['video']
    
    # If no file is selected
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    # Check if the file is allowed
    if file and allowed_file(file.filename):
        # Secure the filename and save it to the UPLOAD_FOLDER
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        tracknum = request.form.get('playerNumber')
        main(int(tracknum))
        return render_template('homepage2.html')
    
    
    return jsonify({'error': 'Invalid file type'})

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


if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(debug=True, port=8080)