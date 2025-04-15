from django.shortcuts import render
import joblib

def home(request):
    return render(request,"index.html")

def formdata(request):
    if request.method == "POST":
        dic = {}
        hazard = float(request.POST.get('hazard'))
        exposure = float(request.POST.get('exposure'))
        housing = float(request.POST.get('housing'))
        poverty = float(request.POST.get('poverty'))
        vulnerability = float(request.POST.get('vulnerability'))
        model = joblib.load('earthquake_pred.pkl')
        result = model.predict([[hazard, exposure, housing, poverty, vulnerability]])
        dic['result'] = result[0]
    return render(request, "modelresponse.html", dic)
