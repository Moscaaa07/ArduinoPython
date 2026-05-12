import serial
import time

porta_seriale = 'COM6'
soglia_notte = 450  # DA CALIBRARE

try:
    arduino = serial.Serial(porta_seriale, 9600, timeout=1)
    time.sleep(2)
    print("Connessione riuscita!")
except Exception as e:
    print(f"Errore di connessione: {e}")
    exit()

while True:
    try:
        linea = arduino.readline().decode('utf-8').strip()

        if linea and "," in linea:
            parti = linea.split(',')

            if len(parti) == 2:
                try:
                    movimento = int(parti[0])
                    luce = int(parti[1])
                except:
                    continue  # salta dati corrotti

                # LOGICA SEMPLIFICATA
                if movimento == 1 and luce < soglia_notte:
                    comando = '1'
                    stato = "LUCE ON"
                else:
                    comando = '0'
                    stato = "LUCE OFF"

                arduino.write(comando.encode())

                print(f"Movimento: {movimento} | Luce: {luce} -> {stato}")

    except Exception:
        continue

    time.sleep(0.1)