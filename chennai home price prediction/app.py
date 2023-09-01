from flask import Flask, render_template, request
import numpy as np
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pickle', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        loc = str(request.form['location'])
        square_feet = int(request.form['square_feet'])
        No_of_Bedrooms = float(request.form['No_of_Bedrooms'])
        No_of_Bathrooms = int(request.form['No_of_Bathrooms'])
        Total_Rooms = int(request.form['Total_Rooms'])
        Parking_facility = int(request.form['Parking_facility'])
        Date_of_build = float(request.form['Date_of_build'])
        distance_from_main_road= float(request.form['distance_from_main_road'])
        l=['Adyar','Anna Nagar','Chrompet','KK Nagar','Karapakkam','T Nagar','Velachery']
        loc=l.index(loc)
        
        l=[0,0,0,0,0,0,0]
        l[loc]=1
        print(l)
        
        values = np.array([l+[square_feet,No_of_Bedrooms,No_of_Bathrooms,Total_Rooms,Parking_facility,Date_of_build,distance_from_main_road]])
        print(values)
        prediction = model.predict(values)
        p=prediction[0]
        
        pr=str(int(p))
        pr=pr[0]+pr[1]+','+pr[2:]
        return render_template('result.html', prediction=pr)


if __name__ == "__main__":
    app.run(debug=True)

