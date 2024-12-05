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