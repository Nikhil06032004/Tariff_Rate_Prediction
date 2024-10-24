from flask import Flask, request, jsonify, render_template
import pickle

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Extract input data
    year = data['year']
    wttons = data['wttons']
    labour = data['labour']
    toll = data['toll']
    distance = data['distance']
    fuelcost = data['fuelcost']
    miscellaneous = data['miscellaneous']
    road = data['road']
    demand = data['demand']
    
    # Convert input data to required format
    road_1 = 1 if road == 'sh' else 0
    demand_2 = 1 if demand == 'low' or demand == 'high' else 0
    
    # Create input array for the model
    input_data = [year, wttons, labour, toll, distance, fuelcost, miscellaneous, road_1, demand_2]
    
    # Make prediction
    prediction = model.predict([input_data])
    
    # Return prediction as JSON
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)