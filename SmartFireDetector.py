import adafruit_dht
import board
import digitalio
import time
import subprocess

# DHT11 센서 설정
dhtDevice = adafruit_dht.DHT11(board.D4)

# LED 핀 설정
green_led = digitalio.DigitalInOut(board.D17)
green_led.direction = digitalio.Direction.OUTPUT

red_led1 = digitalio.DigitalInOut(board.D27)
red_led1.direction = digitalio.Direction.OUTPUT

red_led2 = digitalio.DigitalInOut(board.D22)
red_led2.direction = digitalio.Direction.OUTPUT

# HC-SR501 핀 설정
pir_sensor = digitalio.DigitalInOut(board.D23)
pir_sensor.direction = digitalio.Direction.INPUT

# 불꽃 감지 센서 핀 설정
flame_sensor = digitalio.DigitalInOut(board.D24)
flame_sensor.direction = digitalio.Direction.INPUT

def take_picture():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    file_name = f"/home/pi/picture_{timestamp}.jpg"
    subprocess.run(["libcamera-still", "-o", file_name])
    print(f"Picture taken and saved as {file_name}")

try:
    while True:
        try:
            # 온도와 습도 읽기
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity

            if humidity is not None and temperature is not None:
                print(f"Temp: {temperature:.1f}C  Humidity: {humidity:.1f}%")

                if temperature > 30:
                    # 온도가 30도를 초과하면 빨간색 LED 켜고, 녹색 LED 끔
                    print("Warning: High temperature detected!")
                    red_led1.value = True
                    green_led.value = False

                    # PIR 센서로 인체 감지
                    if pir_sensor.value:
                        print("Person detected! Initiate evacuation!")
                        take_picture()
                    else:
                        print("No person detected.")
                else:
                    # 온도가 30도 이하이면 녹색 LED 켜고, 빨간색 LED 끔
                    red_led1.value = False
                    green_led.value = True

                # 불꽃 감지
                flame_detected = not flame_sensor.value  # LOW가 불꽃 감지를 의미하는 경우
                print(f"Flame sensor value: {flame_detected}")

                if flame_detected:
                    print("Fire detected!")
                    red_led1.value = True
                    red_led2.value = True
                else:
                    red_led2.value = False
            else:
                print("Failed to retrieve data from humidity sensor")
        except RuntimeError as error:
            # 읽기 오류 발생 시 메시지 출력
            print(error.args[0])
        
        time.sleep(2)
except KeyboardInterrupt:
    print("Program stopped")
    red_led1.value = False  # 프로그램 중지 시 모든 LED 끄기
    red_led2.value = False
    green_led.value = False
