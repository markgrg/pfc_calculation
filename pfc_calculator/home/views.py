from django.shortcuts import render

def index(request):
    return render(request, 'pfc_calculator/index.html')

def about(request):
    return render(request, 'pfc_calculator/about.html')

def result(request):
    age = request.GET['age']
    gender = request.GET['gender']
    hight = request.GET['hight']
    weight = request.GET['weight']

    #data = {'age': age, 'gender': gender, 'hight': hight, 'weight': weight}
    
    if gender == 'male':
        res = 10*int(hight)+6.25*int(weight)-5*int(age)+5

    elif gender == 'female':
        res = 10*int(hight)+6.25*int(weight)-5*int(age)-161

    return render(request, 'pfc_calculator/result.html', {'res': res})
