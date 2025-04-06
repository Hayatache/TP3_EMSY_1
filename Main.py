#-----------------------------------------------------
# Importing libraries and modules
#-----------------------------------------------------
import datetime                                                             # Library for date and time related stuff
import math                                                                 # Library for math stuff
import csv                                                                  # Library for csv handling stuff
import smtplib                                                              # Library for sending emails

# These imports are for the SHT40 temperature and humidity sensor
from sensirion_i2c_driver import I2cConnection                              # Base I2C communication
from sensirion_i2c_sht.sht4x import Sht4xI2cDevice                          # SHT40 sensor specific driver
from sensirion_i2c_driver.linux_i2c_transceiver import LinuxI2cTransceiver  # Linux I2C interface

#-----------------------------------------------------
# Setting up the sensor
#-----------------------------------------------------
# Initialize the SHT40 sensor on I2C bus 2
sht40 = Sht4xI2cDevice(I2cConnection(LinuxI2cTransceiver('/dev/i2c-2')))

#-----------------------------------------------------
# Core functions
#-----------------------------------------------------
def read_sensor():
    """
    Reads temperature and humidity from the SHT40 sensor
    Returns: temperature and humidity objects with both values and units
    """
    try:
        t, rh = sht40.single_shot_measurement()
        # Note: t and rh are objects containing both values and units
        # Use t.degrees_celsius or rh.percent_rh to get just the values
    except Exception as ex:
        print("Error while recovering sensor values:", ex)
    else:
        return t, rh

    return 0  # Return 0 if something went wrong

def calculate_dew_point(temp, humidity):
    """
    Calculates dew point using the Magnus formula
    temp: temperature in Celsius
    humidity: relative humidity percentage
    Returns: dew point temperature in Celsius
    """
    dp = 0.0
    B_magnus_coefficient = 17.60
    Y_magnus_coefficient = 243.12
    dp = (Y_magnus_coefficient*(math.log(humidity/100)+((B_magnus_coefficient*temp)/(Y_magnus_coefficient+temp))))/(B_magnus_coefficient-(math.log(humidity/100)+((B_magnus_coefficient*temp)/(Y_magnus_coefficient+temp))))
    return dp

def Save_to_CSV(filename, date, time, temperature, humidity, dew_point):
    """
    Saves sensor readings to a CSV file
    filename: path to the CSV file
    date: current date
    time: current time
    temperature: temperature reading
    humidity: humidity reading
    dew_point: calculated dew point
    """
    try:
        with open(filename, 'a', newline='') as file:  # 'a' means append mode
            writer = csv.writer(file)
            writer.writerow([date, time, temperature, humidity, dew_point])
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

#-----------------------------------------------------
# Main script
#-----------------------------------------------------
if __name__ == "__main__":  # This ensures the code only runs when the file is executed directly
    print("TP3 EMSY")
    
    # Read sensor values
    temperature, humidity = read_sensor()
    
    # Calculate dew point
    dew_point = calculate_dew_point(temperature.degrees_celsius, humidity.percent_rh)
    print("Dew point:", dew_point)

    # Get current date and time
    now = datetime.datetime.now()
    current_date = now.strftime("%d.%m.%Y")  # Format: DD.MM.YYYY
    current_time = now.strftime("%H:%M")     # Format: HH:MM
    
    # Save readings to CSV file
    Save_to_CSV('/home/debian/temperature_data.csv', current_date, current_time, 
                temperature.degrees_celsius, humidity.percent_rh, dew_point)
    
    print("Time:", current_time)
    print("Date:", current_date)

#----------------------------------------------------------------------------------------------------------
# Email Alert System
#----------------------------------------------------------------------------------------------------------
__author__ = "Henri Mott / Benjamin Schafroth"
__version__ = "1.0"
__maintainer__ = "Henri Mott"
__email__ = "henrimott1@gmail.com"
__status__ = "Production"
__date__ = "Avril 2025"

def send_email(receiver, subject, message):
    """
    Sends an email alert using Gmail SMTP
    receiver: list of email addresses to send to
    subject: email subject line
    message: email body content
    """
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Enable TLS encryption
    server.login("henrimott1@gmail.com","vtia igpc upxo kpgq")
    sender = "henrimott1@gmail.com"

    # Set up email headers
    headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Disposition': 'inline',
        'Content-Transfer-Encoding': '8bit',
        'From': sender,
        'To':receiver,
        'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
        'X-Mailer': 'python',
        'Subject': subject
    }
    
    # Create email message
    msg = 'WHERE IS OMNI MAN!!!!!, Where is HE!!'
    for key, value in headers.items():
        msg += "%s: %s\n" % (key, value)
    msg += "\n%s\n" % (message)

    try:
        server.sendmail(headers['From'], headers['To'], msg.encode("utf8"))
        server.quit()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)

# Temperature alert system
temp_max = 28  # Maximum temperature threshold
if temperature.degrees_celsius > temp_max:
    print("Temperature alert triggered - sending email")
    subject = "TEMPERATURE WARNING"
    message = f"The temperature is at {temperature.degrees_celsius}°C, and the max temperature is {temp_max}°C!"
    send_email(["henrimott1@gmail.com"], subject, message)
else:
    print("Temperature is within normal range")

#----------------------------------------------------------------------------------------------------------
# Temperature Data Structure and CSV Handling
#----------------------------------------------------------------------------------------------------------
print("TP3- Linux RaspberryPi")

class Temp_Struct():
    """
    Class to store temperature and humidity readings with timestamp
    """
    def __init__(self):
        # def: Defines a new method/function in the class
        # __init__: Special constructor method that initializes a new instance of the class
        # self: References the instance being created, allowing access to its attributes
        # Gets current date and time
        from datetime import datetime
        now = datetime.now()
        self.date = now.strftime("%d.%m")    # Format: DD.MM
        self.heure = now.strftime("%H.%M")   # Format: HH.MM
        self.temp = 69                        # Default temperature
        self.humi = 70                        # Default humidity
        self.point_ros = 10                   # Default dew point
        print("Temperature structure created")

def write_temp_to_csv(temp_data, file_path='temperature_data.csv'):
    """
    Writes temperature data to a CSV file
    temp_data: Temp_Struct object containing the readings
    file_path: path to the CSV file
    """
    import csv
    print("Writing to CSV file...")

    with open(file_path, 'a', newline='') as file:
        # Create a CSV writer object to write data to the file
        writer = csv.writer(file)
        print("writing")

        # Write all temperature data fields as a single row to the CSV file
        # Format: [date, time, temperature, humidity, dew point]
        # Each field comes from the temp_data object passed to this function
        writer.writerow
        ([
            temp_data.date,
            temp_data.heure,
            temp_data.temp,
            temp_data.humi,
            temp_data.point_ros
        ])
        print("Data written successfully")

# Main execution
if __name__ == "__main__":
    # Create and save temperature data
    temp_data = Temp_Struct()
    write_temp_to_csv(temp_data)
    
    # Save current sensor readings
    Save_to_CSV('/home/debian/temperature_data.csv', current_date, current_time, 
                temperature.degrees_celsius, humidity.percent_rh, dew_point)

    print ("Heure", current_time)                           #affiche heure
    print ("Date", current_date)                            #affiche date
