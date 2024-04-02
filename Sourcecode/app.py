from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/employeePredict", methods=['POST', 'GET'])
def employeePredict():
    if request.method == 'POST':
        print("...................................................")
        age = int(request.form['age'])
        dfh = int(request.form['dfh'])
        mi = int(request.form['MonthlyIncome'])
        hr = int(request.form['HourlyRate'])
        mr = int(request.form['MonthlyRate'])
        dr = int(request.form['DailyRate'])
        ycm = int(request.form['ycm'])
        ycr = int(request.form['ycr'])
        yac = int(request.form['yac'])
        psh = int(request.form['psh'])
        ncw = int(request.form['ncw'])
        twy = int(request.form['twy'])
        ov = int(request.form['OverTime'])  # Changed to int since it's numeric
        ef = int(request.form['EducationField'])  # Changed to int since it's numeric
        jr = int(request.form['JobRole'])  # Changed to int since it's numeric
        rs = int(request.form['RelationshipSatisfaction'])  # Added RelationshipSatisfaction
        es = int(request.form['EnvironmentSatisfaction'])  
        btr = request.form['BusinessTravel']  # Added BusinessTravel
        ysp = int(request.form['YearsSinceLastPromotion'])  # Added YearsSinceLastPromotion
        pr = int(request.form['PerformanceRating'])  # Added PerformanceRating
        wlb = int(request.form['WorkLifeBalance'])  # Added WorkLifeBalance
        ttl = int(request.form['TrainingTimesLastYear'])  # Added TrainingTimesLastYear
        js = int(request.form['JobSatisfaction'])  # Added JobSatisfaction
        sol = int(request.form['StockOptionLevel'])
        dep = request.form['Department']
        edu = request.form['Education']

        x = [dr, dfh, ef, hr, jr, mi, mr, ncw, ov, psh, twy, yac, ycr, ycm, age, rs, es, btr, ysp, dep, pr, wlb, ttl, js, sol,edu]

        print(x)
        result = model.predict([x])[0]
        print(result)
        
        if result == 1:
            return render_template('index.html', res="Employee discontinued.")
        else:
            return render_template('index.html', res="Employee continued")

    else:
        return render_template('index.html', res="")

if __name__ == "__main__":
    app.run(debug=True,port=5000)
