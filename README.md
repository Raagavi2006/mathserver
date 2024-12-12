# Ex.05 Design a Website for Server Side Processing
# Date:09.11.2024
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
math.html
<html>
<head>
    <title>Lamp Filament Power Calculator</title>
    <link rel="stylesheet" href="styles.css">
    <script>
        function calculatePower() {
            const voltage = parseFloat(document.getElementById("voltage").value);
            const resistance = parseFloat(document.getElementById("resistance").value);

            if (isNaN(voltage) || isNaN(resistance) || resistance <= 0) {
                document.getElementById("result").textContent = "Please enter valid numbers!";
                return;
            }

            const power = Math.pow(voltage, 2) / resistance;
            document.getElementById("result").textContent = `Power: ${power.toFixed(2)} Watts`;
        }
    </script>
</head>
<body>
    <style>
        body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
    color: #333;
}

.container {
    max-width: 500px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    text-align: center;
}

h1 {
    color: #444;
    margin-bottom: 20px;
}

form {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

label {
    font-weight: bold;
    text-align: left;
}

input {
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px 20px;
    font-size: 1rem;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.result {
    margin-top: 20px;
    font-size: 1.2rem;
    color: #007bff;
}

    </style>
    <div class="container">
        <h1>Power Calculator</h1>
        <p>Calculate the power of a lamp filament in an incandescent bulb.</p>
        
        <form onsubmit="event.preventDefault(); calculatePower();">
            <label for="voltage">Voltage (V):</label>
            <input type="number" id="voltage" placeholder="Enter voltage" required>

            <label for="resistance">Resistance (Ω):</label>
            <input type="number" id="resistance" placeholder="Enter resistance" required>

            <button type="submit">Calculate</button>
        </form>

        <div id="result" class="result"></div>
    </div>
</body>
</html>

views.py
from django.shortcuts import render
def EnergyCalc(request):
    context = {
        'power': "0", 
        'intensity': "0", 
        'resistance': "0"
    }
    
    if request.method == 'POST':
        print("POST method is used")
        
        intensity = request.POST.get('intensity', '0')
        resistance = request.POST.get('resistance', '0')
        
        print('Request:', request)
        print('Intensity:', intensity)
        print('Resistance:', resistance)
        
        try:
            intensity = float(intensity)  
            resistance = float(resistance) 
            power = (intensity ** 2) * resistance
            
           
            context['power'] = round(power, 2) 
            context['intensity'] = round(intensity, 2)
            context['resistance'] = round(resistance, 2)
            
            print(f'Calculated Power: {power}')
        except ValueError as e:
            
            print(f'Error in calculation: {e}')
            context['power'] = "Invalid input. Please enter valid numbers."
    return render(request, 'mathapp/math.html', context)

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [

 path('admin/', admin.site.urls), 
path('', views.EnergyCalc, name="EnergyCalc"), 
]
```
# SERVER SIDE PROCESSING:

![alt text](<WEB 5.png>)

# HOMEPAGE:

![Screenshot 2024-12-12 081704](https://github.com/user-attachments/assets/0b4b7aa3-669e-4d44-a03a-1a5eafca8231)

# RESULT:
The program for performing server side processing is completed successfully.
