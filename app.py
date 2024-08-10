from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    feedback = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'number': False,
        'special': False
    }
    if len(password) >= 8:
        feedback['length'] = True
    if any(char.isupper() for char in password):
        feedback['uppercase'] = True
    if any(char.islower() for char in password):
        feedback['lowercase'] = True
    if any(char.isdigit() for char in password):
        feedback['number'] = True
    if any(char in '!@#$%^&*()-_+=<>?/[]{}|`~' for char in password):
        feedback['special'] = True

    score = sum(feedback.values())
    strength = 'Weak'
    if score == 5:
        strength = 'Very Strong'
    elif score == 4:
        strength = 'Strong'
    elif score == 3:
        strength = 'Moderate'
    elif score == 2:
        strength = 'Weak'
    
    return strength, feedback

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = ''
    feedback = {}
    if request.method == 'POST':
        password = request.form['password']
        strength, feedback = check_password_strength(password)
    return render_template('index.html', strength=strength, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
