# -*- coding: utf-8 -*-
import pandas
import psycopg2

# Connect to an existing database
conn = psycopg2.connect(dbname="sensortem", user="sensor", password="12345")


# Open a cursor to perform database operations, Posicion para los registros. 
cur = conn.cursor()

import time

try:
    import serial
    arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)

    # Nota: provocamos un reseteo manual de la placa para leer desde
    # el principio, ver http://stackoverflow.com/a/21082531/554319
    arduino.setDTR(False)
    time.sleep(1)
    arduino.flushInput()
    arduino.setDTR(True)

except (ImportError, serial.SerialException):
    # No hay módulo serial o placa Arduino disponibles
    import io

    class FakeArduino(io.RawIOBase):
        """Clase para representar un "falso Arduino"
        """
        def readline(self):
            time.sleep(0.1)
            return b'sensor = 0\toutput = 0\r\n'

    arduino = FakeArduino()


# Con la sentencia with el arduino se cierra automáticamente, ver
# http://docs.python.org/3/reference/datamodel.html#context-managers
with arduino:
    while True:
        try:
            
            # En Python 3 esta función devuelve un objeto bytes, ver
            # http://docs.python.org/3/library/stdtypes.html#typebytes
            line = arduino.readline()
            # Con errors='replace' se evitan problemas con bytes erróneos, ver
            # http://docs.python.org/3/library/stdtypes.html#bytes.decode
            # Con end='' se evita un doble salto de línea
            #print(line.decode('ascii', errors='replace'), end='')
            df = pandas.read_csv(line.decode("utf-8"))
            
            for index, row in df.iterrows():
                tm = row['Temperatura']
                hm = row['Humedad']
                print(tm, hm)
                campos = "temperatura, humedad"
                cur.execute("INSERT INTO datosensor (" + campos + ") Values (%s, %s)",
                (tm, hm))
                conn.commit()

        except KeyboardInterrupt:
            print("Exiting")
            break


