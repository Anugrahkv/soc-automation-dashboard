from django.shortcuts import render
from .utils import query_abuseipdb, query_virustotal

def dashboard_view(request):
    context = {}
    if request.method == "POST":
        # .strip() removes any accidental spaces the user pastes
        ioc_input = request.POST.get('ioc_input').strip() 
        
        # Auto-Routing Logic: IPs contain dots, Hashes do not.
        if '.' in ioc_input:
            result = query_abuseipdb(ioc_input)
        else:
            result = query_virustotal(ioc_input)
            
        context['result'] = result
        context['searched_ioc'] = ioc_input

    return render(request, 'automation/dashboard.html', context)