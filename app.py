from flask import Flask, render_template
import random

app = Flask(__name__)

def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

@app.route('/')
def home():
    numbers = generate_lotto_numbers()
    return render_template('index.html', numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)
