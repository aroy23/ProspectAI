from flask import Flask, render_template

app = Flask(__name__, 
            static_folder="../frontend/assets/css",
            template_folder="../frontend/assets/js")

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)