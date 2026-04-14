from flask import Flask, render_template, request

app = Flask(__name__)

# route é o caminho do site dps do domínio do site

@app.route("/", methods=['GET', 'POST'])
def length():
    result = None
    destiny_unit = ""

    if request.method == "POST":
        
        value = float(request.form.get('value'))
        origin = request.form.get('origin_unit')
        destiny = request.form.get('destiny_unit')
        
        
        if origin == "m":
            base_meters = value
        elif origin == "ft":
            base_meters = value * 0.3048
        
        if destiny == "m":
            result = base_meters
        elif destiny == "ft":
            result = base_meters / 0.3048
        
        destiny_unit = destiny
    
  
    return render_template("length.html", page='length', result=result, destiny=destiny_unit)



@app.route("/weight", methods=['GET', 'POST'])
def weight():
    result = None
    destiny_unit = ""

    if request.method == "POST":
        
        value = float(request.form.get('value'))
        origin = request.form.get('origin_unit')
        destiny = request.form.get('destiny_unit')
        
        
        if origin == "kg":
            base_kg = value
        elif origin == "lb":
            base_kg = value / 2.20462
        
        if destiny == "kg":
            result = base_kg
        elif destiny == "lb":
            result = base_kg * 2.20462
        
        destiny_unit = destiny
    
    return render_template("weight.html", page='weight', result=result, destiny=destiny_unit)




@app.route("/temperature", methods=['GET', 'POST'])
def temperature():
    result = None
    destiny_unit = ""

    if request.method == "POST":
        
        value = float(request.form.get('value'))
        origin = request.form.get('origin_unit')
        destiny = request.form.get('destiny_unit')
        
        
        if origin == "f":
            base_fahrenheit = value
        elif origin == "c":
            base_fahrenheit = (value * 9/5) + 32
        
        if destiny == "f":
            result = base_fahrenheit 
        elif destiny == "c":
            result = (base_fahrenheit - 32) * (5/9)
        
        destiny_unit = destiny
    
    return render_template("temperature.html", page='temperature', result=result, destiny=destiny_unit)


if __name__ == "__main__":
    app.run(debug=True)