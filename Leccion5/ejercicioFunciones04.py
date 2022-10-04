# Ejercicio 4: Calculadora de impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado. (IVA)
# formula: pago_total = pago_sin_impuestos + pago_sin_impuesto * (impuesto/100)
# Proporciones el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

def calcImpuestos(pago):
    pagoSinImpuesto = pago
    pagoTotal = pagoSinImpuesto * 1.21
    print(f'''
    Pago sin impuesto: {pago}
    Valor del impuesto: 21%
    Pago con impuesto: {pagoTotal}''')

calcImpuestos(float(input('Digite el pago sin impuesto: ')))