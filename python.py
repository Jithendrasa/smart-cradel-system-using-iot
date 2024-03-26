import RPi.GPIO as GPIO
import time
import requests

# Configure GPIO pins for sensors
CRY_SENSOR_PIN = 17
HUMIDITY_SENSOR_PIN = 18
TEMPERATURE_SENSOR_PIN = 27

# IoT Platform API Endpoint
API_ENDPOINT = "http://your_iot_platform_api_endpoint"

# Function to detect cry
def detect_cry():
    GPIO.setup(CRY_SENSOR_PIN, GPIO.IN)
    return GPIO.input(CRY_SENSOR_PIN)

# Function to read humidity
def read_humidity():
    GPIO.setup(HUMIDITY_SENSOR_PIN, GPIO.IN)
    # Implement logic to read humidity from sensor
    return 50  # Dummy value for testing

# Function to read temperature
def read_temperature():
    GPIO.setup(TEMPERATURE_SENSOR_PIN, GPIO.IN)
    # Implement logic to read temperature from sensor
    return 25  # Dummy value for testing

# Function to send data to IoT platform
def send_data_to_platform(cry_status, humidity, temperature):
    data = {
        "cry_status": cry_status,
        "humidity": humidity,
        "temperature": temperature
    }
    try:
        response = requests.post(API_ENDPOINT, json=data)
        if response.status_code == 200:
            print("Data sent successfully to IoT platform")
        else:
            print("Error sending data to IoT platform")
    except Exception as e:
        print("Error:", e)

def main():
    # Initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    try:
        while True:
            # Read sensor data
            cry_status = detect_cry()
            humidity = read_humidity()
            temperature = read_temperature()

            # Send data to IoT platform
            send_data_to_platform(cry_status, humidity, temperature)

            # Delay for 5 seconds before next reading
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
