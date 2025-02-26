'''import joblib
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        age = request.form['age']
        gender = request.form['Gender']
        symptoms = request.form['symptoms']
        
        # Predict the medicine based on the entered symptoms
        prediction = model.predict([symptoms])
        medicine = prediction[0]
        symptom_list = symptoms.split()
        if len(symptom_list) < 1 or len(symptom_list) > 3:
            return render_template('index.html', error="Please enter between 1 and 3 symptoms.")
    
        
        
        return render_template('results.html', gender=gender, age=age, symptoms=symptoms, medicine=medicine)
    
    return render_template('index.html')



# Emergency First Aid Pages (Ensure correct paths)
@app.route("/cpr")
def cpr():
    return render_template("first_aid/cpr.html")

@app.route("/electric_shock")
def electric_shock():
    return render_template("first_aid/electric_shocks.html")

@app.route("/fire_accidents")
def fire_accidents():
    return render_template("first_aid/fire_accidents.html")

@app.route("/snake_bites")
def snake_bites():
    return render_template("first_aid/snake_bites.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)'''
'''import joblib
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs
        try:
            age = int(request.form['age'])  # Convert to integer for validation
            gender = request.form['Gender']
            symptoms = request.form['symptoms'].strip()  # Remove leading/trailing spaces

            # Check if symptoms are empty
            if not symptoms:
                return render_template('index.html', error="Please enter symptoms.")
            
            # Split symptoms and check the count
            symptom_list = symptoms.split()
            if len(symptom_list) < 1 or len(symptom_list) > 3:
                return render_template('index.html', error="Please enter between 1 and 3 symptoms.")

            # Join symptoms into a single string for prediction
            symptom_string = " ".join(symptom_list)

            # Predict the medicine based on the entered symptoms
            prediction = model.predict([symptom_string])  # Pass the string, not a list
            medicine = prediction[0]

            return render_template('results.html', gender=gender, age=age, symptoms=symptoms, medicine=medicine)
        
        except ValueError:
            return render_template('index.html', error="Please enter valid data for age.")

    return render_template('index.html')
# Emergency First Aid Pages (Ensure correct paths)
@app.route("/cpr")
def cpr():
    return render_template("first_aid/cpr.html")

@app.route("/electric_shock")
def electric_shock():
    return render_template("first_aid/electric_shocks.html")

@app.route("/fire_accidents")
def fire_accidents():
    return render_template("first_aid/fire_accidents.html")

@app.route("/snake_bites")
def snake_bites():
    return render_template("first_aid/snake_bites.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)'''
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get user inputs
            age = int(request.form['age'])
            gender = request.form['Gender']
            symptoms = request.form['symptoms'].strip()
            
            # Validate symptoms input
            symptom_list = [sym.strip() for sym in symptoms.split() if sym.strip()]
            
            # Strict 1-3 symptoms validation
            if len(symptom_list) < 1 or len(symptom_list) > 3:
                return render_template('index.html', error="Please enter 1 to 3 symptoms.")
            
            # Pad symptoms if less than 3
            while len(symptom_list) < 3:
                symptom_list.append('')
            
            # Combine symptoms into a single string
            symptom_string = ' '.join(symptom_list[:3])
            
            # Predict medicine
            prediction = model.predict([symptom_string])
            medicine = prediction[0]
            
            return render_template('results.html', gender=gender, age=age, symptoms=symptoms, medicine=medicine)
        
        except ValueError:
            return render_template('index.html', error="Please enter valid data for age.")
    
    return render_template('index.html')

# Emergency First Aid Routes
@app.route("/cpr")
def cpr():
    return render_template("first_aid/cpr.html")

@app.route("/electric_shock")
def electric_shock():
    return render_template("first_aid/electric_shocks.html")

@app.route("/fire_accidents")
def fire_accidents():
    return render_template("first_aid/fire_accidents.html")

@app.route("/snake_bites")
def snake_bites():
    return render_template("first_aid/snake_bites.html")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)