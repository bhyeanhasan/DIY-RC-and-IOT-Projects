import json
import time
import board
import random
import asyncio
import websockets
import busio as io
from time import sleep
import adafruit_mlx90614
from datetime import datetime

link = 'ws://192.168.0.105:8000/ws/temperature/'
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)


async def main():
    try:
        async with websockets.connect(link) as websocket:
            print("Connected ... ")
            while 1:
                try:
                    ambientTemp = "{:.2f}".format(mlx.ambient_temperature * (9.0 / 5.0) + 32)
                    targetTemp = "{:.2f}".format(mlx.object_temperature * (9.0 / 5.0) + 32)
                    data = json.dumps({
                        'temperature': str(targetTemp),
                        'time': str(datetime.now())
                    }))
                    await websocket.send(data)
                    print('data updated')
                    time.sleep(5)  # wait and then do it again
                except Exception as e:
                    print(e)
    except:
        print("Connection Error")


asyncio.get_event_loop().run_until_complete(main())
