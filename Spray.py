import Jetson.GPIO as GPIO
import time

# 設定腳位位置
output_pin = 21

def main():
    
    # 設置為BCM模式
    GPIO.setmode(GPIO.BCM) 
    
    # 將腳位設定為輸出，並預設為輸出高電位
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            # 每隔3秒鐘切換開關
            time.sleep(3)
            print("Outputting {} to pin {}".format(curr_value, output_pin))
            GPIO.output(output_pin, curr_value)
            curr_value ^= GPIO.HIGH
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
