from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def home(request):
    return render(request , 'pages/index.html')

def about(request):
    return render(request , 'pages/about/the_marg.html')

def explore_historic_routes(request):
    return render(request , 'pages/explore/historic_routes.html')
def explore_cultural_routes(request):
    return render(request , 'pages/explore/cultural_routes.html')
def explore_railway_routes(request):
    return render(request , 'pages/explore/railway_routes.html')
def explore_cultural_elements(request):
    return render(request , 'pages/explore/cultural_elements.html')

def identification_documentation_methodology(request):
    return render(request , 'pages/identification_documentation/methodology.html')
def identification_documentation_classification(request):
    return render(request , 'pages/identification_documentation/classification.html')
def identification_documentation_bhotiya(request):
    return render(request , 'pages/identification_documentation/bhotiya.html')
def identification_documentation_risk(request):
    return render(request , 'pages/identification_documentation/risk.html')

def conservation_preservation(request):
    return render(request , 'pages/conservation/preservation.html')
def conservation_rehabilitation(request):
    return render(request , 'pages/conservation/rehabilitation.html')
def conservation_restoration(request):
    return render(request , 'pages/conservation/restoration.html')
def conservation_reconstruction(request):
    return render(request , 'pages/conservation/reconstruction.html')

def management_safety(request):
    return render(request , 'pages/management/safety.html')
def management_liability(request):
    return render(request , 'pages/management/liability.html')
def management_policy(request):
    return render(request , 'pages/management/policy.html')
def management_heritage_bylaws(request):
    return render(request , 'pages/management/heritage_bylaws.html')
def management_stakeholders(request):
    return render(request , 'pages/management/stakeholders.html')