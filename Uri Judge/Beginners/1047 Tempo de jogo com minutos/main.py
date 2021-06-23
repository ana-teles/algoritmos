def calcularDuracao(horas_inicio, minutos_inicio, horas_fim, minutos_fim):
    minutos = minutos_fim - minutos_inicio
    horas = horas_fim - horas_inicio
    if(minutos < 0):
        horas -= 1
        minutos += 60
    if(horas < 0 or (horas == 0 and minutos == 0)):
        horas += 24
    return [horas, minutos]
    
    

h1, m1, h2, m2 = [int(x) for x in input().split()]

hora, minuto = calcularDuracao(h1, m1, h2, m2)

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")



