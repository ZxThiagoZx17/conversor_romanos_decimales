from django.shortcuts import render
from .utils import RomanNumerals

# Create your views here.
def converter_view(request):
    result_decimal = None
    result_roman = None
    
    if request.method == 'POST':
        roman_number = request.POST.get('roman_number', '')
        decimal_number = request.POST.get('decimal_number', '')

        # Convertir de romano a decimal
        if roman_number:
            result_decimal = RomanNumerals.from_roman(roman_number)

        # Convertir de decimal a romano
        if decimal_number:
            result_roman = RomanNumerals.to_roman(int(decimal_number))

    return render(request, 'conversor/convertidor.html', {
        'result_decimal': result_decimal,
        'result_roman': result_roman,
    })