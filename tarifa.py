def calcular_tarifa(tipo_vehiculo, distancia_km):
    if not isinstance(distancia_km, (int, float)):
        raise TypeError("La distancia debe ser un número.")

    tarifas = {
        "moto": 800,
        "carro": 1500,
        "camioneta": 2500
    }

    if tipo_vehiculo not in tarifas:
        raise ValueError("Tipo de vehículo no válido. Debe ser 'moto', 'carro' o 'camioneta'.")

    if distancia_km < 0:
        raise ValueError("La distancia no puede ser negativa.")

    tarifa_bruta = distancia_km * tarifas[tipo_vehiculo]
    impuesto_transporte = tarifa_bruta * 0.08
    tarifa_neta = tarifa_bruta + impuesto_transporte

    return tarifa_neta
