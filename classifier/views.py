from django.shortcuts import render
from .ml_models import predict_ransomware

def home(request):
    return render(request, 'classifier/home.html')

def classify(request):
    if request.method == 'POST':
        feature_names = ['machine', 'debug_size', 'debug_rva', 'major_image_version', 'major_os_version',
                         'export_rva', 'export_size', 'iat_vra', 'major_linker_version', 'minor_linker_version',
                         'number_of_sections', 'size_of_stack_reserve', 'dll_characteristics', 'resource_size', 'bitcoin_addresses']
        
        features = [float(request.POST.get(f, 0)) for f in feature_names]
        model_type = request.POST.get('model_type')
        result = predict_ransomware(features, model_type)
        return render(request, 'classifier/result.html', {'result': result})
    return render(request, 'classifier/classify.html')