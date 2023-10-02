from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            motor_steps = float(request.form['motor_steps'])
            microstepping = float(request.form['microstepping'])
            belt_pitch = float(request.form['belt_pitch'])
            pulley_tooth = float(request.form['pulley_tooth'])
            
            # Calculate steps per mm
            result = (motor_steps * microstepping) / (belt_pitch * pulley_tooth)
        except ValueError:
            result = "Invalid Input"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
