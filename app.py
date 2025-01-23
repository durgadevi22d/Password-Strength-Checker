from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to check password strength
def check_password_strength(password):
    score = 0
    if len(password) >= 8:  # Length check
        score += 1
    if any(char.isdigit() for char in password):  # Contains numbers
        score += 1
    if any(char.islower() for char in password):  # Contains lowercase
        score += 1
    if any(char.isupper() for char in password):  # Contains uppercase
        score += 1
    if any(char in "!@#$%^&*()_+" for char in password):  # Contains special chars
        score += 1

    if score == 5:
        return "Strong password!\n Good job!!"
    elif score >= 3:
        return "Moderate password, improve it."
    else:
        return "Weak password, consider making it stronger.\n Try to use Uppercase,Lowercase,Numbers,spcial characters"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_password():
    password = request.form.get('password')
    result = check_password_strength(password)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
