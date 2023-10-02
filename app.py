from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input values
        prev_rotation_distance = float(request.form.get('prev_rotation_distance'))
        initial_mark_distance = float(request.form.get('initial_mark_distance'))
        subsequent_mark_distance = float(request.form.get('subsequent_mark_distance'))
        requested_extrude = float(request.form.get('requested_extrude'))

        # Calculate the actual extrude distance
        actual_extrude_distance = initial_mark_distance - subsequent_mark_distance

        # Calculate the new rotation_distance
        new_rotation_distance = round(prev_rotation_distance * actual_extrude_distance / requested_extrude, 3)

        return render_template('index.html', result=new_rotation_distance)
    else:
        return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
