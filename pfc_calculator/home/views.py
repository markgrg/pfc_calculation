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

    else:
        res = 0
        imt = 0
        imt_res = 'Вы что-то не указали'
        return render(request, 'pfc_calculator/result.html', {'res': res, 'imt': imt, 'imt_res': imt_res})

    hight = int(hight)/100
    imt = int(weight)/(hight*hight)
    if 0 < imt < 19:
        imt_res = 'Дифицит массы тела'
    elif 19.1 < imt < 25:
        imt_res = 'Вес в норме'
    
    elif imt > 25.01:
        imt_res = 'Избыточный вес'

    return render(request, 'pfc_calculator/result.html', {'res': res, 'imt': imt, 'imt_res': imt_res})
