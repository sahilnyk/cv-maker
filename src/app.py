from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')  # Renders the form page (index.html)

@app.route('/generate', methods=['POST'])
def generate_cv():
    # Get data from form submission
    data = request.form.to_dict()

    # Debugging: print data to terminal
    print("Form data received:", data)

    # Render the CV output page and pass the data to it
    return render_template('cv_output.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode to see any errors in the terminal
