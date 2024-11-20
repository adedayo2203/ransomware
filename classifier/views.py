from django.shortcuts import render
from .ml_models import predict_ransomware

def home(request):
    return render(request, 'classifier/home.html')

def classify(request):
    if request.method == 'POST':
        feature_names = ['Machine', 'DebugSize', 'DebugRVA', 'MajorImageVersion', 'MajorOSVersion',
                'ExportRVA', 'ExportSize', 'IatVRA', 'MajorLinkerVersion', 'MinorLinkerVersion',
                'NumberOfSections', 'SizeOfStackReserve', 'DllCharacteristics', 'ResourceSize', 'BitcoinAddresses']
        
        initial_classification = request.POST.get('classification_result') 
        
        features = []
        for f in feature_names:
            value = request.POST.get(f)
            try:
                features.append(float(value))
            except (TypeError, ValueError):
                # Handle the error, e.g., log it, set a default value, or return an error response
                features.append(0)  # or handle it in a way that makes sense for your application
        model_type = request.POST.get('model_type')
        result = predict_ransomware(features, model_type)
        return render(request, 'classifier/result.html', {'result': result, 
                                                          'initial_classification': initial_classification})
    return render(request, 'classifier/classify.html')