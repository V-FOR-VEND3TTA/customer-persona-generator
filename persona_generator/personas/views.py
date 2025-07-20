from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import CustomerPersonaForm
from xhtml2pdf import pisa
from io import BytesIO

def home(request):
    if request.method == 'POST':
        form = CustomerPersonaForm(request.POST)
        if form.is_valid():
            # Process form data and generate PDF
            return generate_pdf(form.cleaned_data)
    else:
        form = CustomerPersonaForm()
    return render(request, 'personas/home.html', {'form': form})

def generate_pdf(data):
    template_path = 'personas/persona_template.html'
    context = data
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="customer_persona.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
