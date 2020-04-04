# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import psycopg2 as pg
import pandas as pd
import pickle
import numpy as np
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)
        arduino.setDTR(False)
        time.sleep(1)
        arduino.flushInput()
        arduino.setDTR(True)
    except (ImportError, serial.SerialException):
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
            print(line.decode('ascii', errors='replace'), end='')

        except KeyboardInterrupt:
            print("Exiting")
            return(line = arduino.readline())
            



if __name__ == '__main__':
    app.run()

