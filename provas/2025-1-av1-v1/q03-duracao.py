segundos_totais = int(input("Digite a duração em segundos do evento esportivo: "))

h = segundos_totais // 3600
m = (segundos_totais % 3600) // 60
s = segundos_totais % 60

print(f"{h:02}:{m:02}:{s:02}")
