from datetime import datetime

ahora = datetime.now()

fin_del_2023 = datetime(2023, 12, 31)

tiempo_falta = fin_del_2023-ahora

print(f"Los días que faltan son: {tiempo_falta.days}.")
