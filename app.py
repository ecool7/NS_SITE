from flask import Flask, render_template

app = Flask(__name__)
############ Блок гироскопов ######################
# Список гироскопов
GYROSCOPES = [
    {
        "name": "NS-GYR-100",
        "accuracy": "±0.1°",
        "application": "Aviation, military drones",
        "technology": "Fiber optic gyroscope",
        "image": "gyro1.png"
    },
    {
        "name": "NS-GYR-200",
        "accuracy": "±0.5°",
        "application": "Robotics, industrial automation",
        "technology": "Rotary laser gyroscope",
        "image": "gyro2.png"
    },
    {
        "name": "NS-GYR-300",
        "accuracy": "±1.0°",
        "application": "Marine vessels, autonomous vehicles",
        "technology": "MEMS-based",
        "image": "gyro3.png"
    },
    {
        "name": "NS-GYR-400",
        "accuracy": "±0.05°",
        "application": "Spacecraft, high-precision navigation",
        "technology": "Ring laser gyroscope",
        "image": "gyro4.png"
    },

    # Добавляй новые датчики сюда — и всё!
]

SENSORS_GYRO = [
    {
        "id": "NS-GYR-100",
        "name": "NS-GYR-100",
        "image": "gyro1.png",
        "description": "High-precision fiber optic gyroscope for aviation and military drones.",
        "specs": {
            "Accuracy": "±0.1°",
            "Application": "Aviation, military drones",
            "Technology": "Fiber optic gyroscope",
            "Operating Temp": "-40°C to +85°C",
            "Output": "Analog, digital",
            "Power": "5V DC"
        },
        "datasheet": "datasheets/NS-GYR-100.pdf"  # путь к PDF
    },
    {
        "id": "NS-GYR-200",
        "name": "NS-GYR-200",
        "image": "gyro2.png",
        "description": "Rotary laser gyroscope for robotics and industrial automation.",
        "specs": {
            "Accuracy": "±0.5°",
            "Application": "Robotics, industrial automation",
            "Technology": "Rotary laser gyroscope",
            "Operating Temp": "-30°C to +70°C",
            "Output": "Digital",
            "Power": "12V DC"
        },
        "datasheet": "datasheets/NS-GYR-200.pdf"
    },
    {
        "id": "NS-GYR-300",
        "name": "NS-GYR-300",
        "image": "gyro3.png",
        "description": "MEMS-based gyroscope for marine vessels and autonomous vehicles.",
        "specs": {
            "Accuracy": "±1.0°",
            "Application": "Marine vessels, autonomous vehicles",
            "Technology": "MEMS-based",
            "Operating Temp": "-20°C to +60°C",
            "Output": "I²C, SPI",
            "Power": "3.3V DC"
        },
        "datasheet": "datasheets/NS-GYR-300.pdf"
    },
    # Добавляй новые датчики сюда — и всё!
]



############ Блок АКСОВ #########

ACCEL = [
    {
        "id": "NSAEM1010",
        "name": "NSAEM1010",
        "range": "± 2-3",
        "application": "Aviation, robotics",
        "image": "NSAEM1010.png"
    },
    {
        "id": "NS-ACC-200",
        "name": "NS-ACC-200",
        "range": "±8g",
        "application": "Vibration analysis, industrial systems",
        "image": "accel2.png"
    },
{
        "id": "NS-ACC-300",
        "name": "NS-ACC-300",
        "range": "±50g",
        "application": "Structural monitoring, military vehicles",
        "image": "accel3.png"  # ← проверь имя!
    }
]

ACCEL_SENSORS = [
    {
        "id": "NSAEM1010",
        "name": "NSAEM1010",
        "image": "NSAEM1010.png",
        "description": "ANALOG COLIBRYS",
        "specs": {
            "Measurement Range": "±2g",
            "Sensitivity": "1000 mV/g",
            "Frequency Response": "0.5 Hz to 2.5 kHz",
            "Noise Level": "25 µg/√Hz",
            "Application": "Aviation, robotics, vibration monitoring",
            "Interface": "Analog output",
            "Operating Temp": "-40°C to +85°C",
            "Power Supply": "5V DC"
        },
        "datasheet": "datasheets/NS-ACC-100.pdf"
    },
    {
        "id": "NS-ACC-200",
        "name": "NS-ACC-200",
        "image": "accel2.png",
        "description": "Digital MEMS-based accelerometer with I²C/SPI interface for industrial and navigation systems.",
        "specs": {
            "Measurement Range": "±8g",
            "Resolution": "16-bit",
            "Interface": "I²C, SPI",
            "Bandwidth": "1.6 kHz",
            "Shock Survival": "10,000g",
            "Application": "Industrial automation, inertial navigation",
            "Operating Temp": "-40°C to +105°C",
            "Power Supply": "3.3V DC"
        },
        "datasheet": "datasheets/NS-ACC-200.pdf"
    },
    {
        "id": "NS-ACC-300",
        "name": "NS-ACC-300",
        "image": "accel3.png",
        "description": "High-g shock accelerometer for impact detection and structural health monitoring.",
        "specs": {
            "Measurement Range": "±50g",
            "Output": "Analog (4-20mA)",
            "Frequency Response": "1 Hz to 10 kHz",
            "Accuracy": "±1%",
            "Application": "Structural monitoring, military vehicles",
            "Housing": "Stainless steel, IP67",
            "Operating Temp": "-55°C to +125°C",
            "Power Supply": "12-24V DC"
        },
        "datasheet": "datasheets/NS-ACC-300.pdf"
    }
]


# Список IMU (для списка на странице)
IMU = [
    {
        "id": "NS-IMU-100",
        "name": "NS-IMU-100",
        "type": "6-axis",
        "application": "Drones, robotics",
        "image": "imu1.png"
    },
    {
        "id": "NS-IMU-200",
        "name": "NS-IMU-200",
        "type": "9-axis",
        "application": "Autonomous vehicles",
        "image": "imu2.png"
    },
    {
        "id": "NS-IMU-300",
        "name": "NS-IMU-300",
        "type": "6-axis",
        "application": "Industrial automation",
        "image": "imu3.png"
    },
    {
        "id": "NS-IMU-400",
        "name": "NS-IMU-400",
        "type": "9-axis",
        "application": "Aviation, navigation",
        "image": "imu4.png"
    },
    {
        "id": "NS-IMU-500",
        "name": "NS-IMU-500",
        "type": "6-axis",
        "application": "Marine systems",
        "image": "imu5.png"
    },
    {
        "id": "NS-IMU-600",
        "name": "NS-IMU-600",
        "type": "9-axis",
        "application": "Spacecraft, high-precision",
        "image": "imu6.png"
    }
]

# Подробные данные для детальных страниц
# Список IMU (для списка на странице)
IMU = [
    {
        "id": "NS-IMU-100",
        "name": "NS-IMU-100",
        "type": "6-axis",
        "application": "Drones, robotics",
        "image": "imu1.png"
    },
    {
        "id": "NS-IMU-200",
        "name": "NS-IMU-200",
        "type": "9-axis",
        "application": "Autonomous vehicles",
        "image": "imu2.png"
    },
    {
        "id": "NS-IMU-300",
        "name": "NS-IMU-300",
        "type": "6-axis",
        "application": "Industrial automation",
        "image": "imu3.png"
    },
    {
        "id": "NS-IMU-400",
        "name": "NS-IMU-400",
        "type": "9-axis",
        "application": "Aviation, navigation",
        "image": "imu4.png"
    },
    {
        "id": "NS-IMU-500",
        "name": "NS-IMU-500",
        "type": "6-axis",
        "application": "Marine systems",
        "image": "imu5.png"
    },
    {
        "id": "NS-IMU-600",
        "name": "NS-IMU-600",
        "type": "9-axis",
        "application": "Spacecraft, high-precision",
        "image": "imu6.png"
    }
]

# Подробные данные для детальных страниц
IMU_SENSORS = [
    {
        "id": "NS-IMU-100",
        "name": "NS-IMU-100",
        "image": "imu1.png",
        "description": "Compact 6-axis IMU with MEMS accelerometers and gyroscopes for drones and robotics.",
        "specs": {
            "Axes": "6 (3 Accel + 3 Gyro)",
            "Accuracy": "±0.5°",
            "Interface": "I²C, SPI",
            "Bandwidth": "1.2 kHz",
            "Operating Temp": "-40°C to +85°C",
            "Power": "3.3V DC",
            "Application": "Drones, robotics, stabilization"
        },
        "datasheet": "datasheets/NS-IMU-100.pdf"
    },
    {
        "id": "NS-IMU-200",
        "name": "NS-IMU-200",
        "image": "imu2.png",
        "description": "High-performance 9-axis IMU with integrated magnetometer for autonomous vehicles.",
        "specs": {
            "Axes": "9 (3 Accel + 3 Gyro + 3 Mag)",
            "Accuracy": "±0.3°",
            "Interface": "SPI, UART",
            "Update Rate": "1000 Hz",
            "Shock Survival": "10,000g",
            "Operating Temp": "-40°C to +105°C",
            "Power": "5V DC"
        },
        "datasheet": "datasheets/NS-IMU-200.pdf"
    },
    {
        "id": "NS-IMU-300",
        "name": "NS-IMU-300",
        "image": "imu3.png",
        "description": "Industrial-grade 6-axis IMU for automation and condition monitoring.",
        "specs": {
            "Axes": "6-axis",
            "Vibration Tolerance": "High",
            "Output": "Digital",
            "Calibration": "Factory calibrated",
            "Operating Temp": "-30°C to +85°C",
            "Housing": "Aluminum, IP67",
            "Application": "Industrial automation, robotics"
        },
        "datasheet": "datasheets/NS-IMU-300.pdf"
    },
    {
        "id": "NS-IMU-400",
        "name": "NS-IMU-400",
        "image": "imu4.png",
        "description": "High-accuracy 9-axis IMU for aviation and navigation systems.",
        "specs": {
            "Axes": "9-axis",
            "Accuracy": "±0.1°",
            "Bias Stability": "0.01°/hr",
            "Interface": "RS-422, Ethernet",
            "Operating Temp": "-55°C to +125°C",
            "Certification": "MIL-STD-810G",
            "Application": "Aviation, navigation, defense"
        },
        "datasheet": "datasheets/NS-IMU-400.pdf"
    },
    {
        "id": "NS-IMU-500",
        "name": "NS-IMU-500",
        "image": "imu5.png",
        "description": "Marine-optimized 6-axis IMU with corrosion-resistant housing.",
        "specs": {
            "Axes": "6-axis",
            "Water Resistance": "IP68",
            "Operating Temp": "-40°C to +85°C",
            "Output": "Analog + Digital",
            "Shock Rating": "5000g",
            "Housing": "Stainless steel",
            "Application": "Marine vessels, offshore systems"
        },
        "datasheet": "datasheets/NS-IMU-500.pdf"
    },
    {
        "id": "NS-IMU-600",
        "name": "NS-IMU-600",
        "image": "imu6.png",
        "description": "Ultra-high precision 9-axis IMU for spacecraft and high-precision navigation.",
        "specs": {
            "Axes": "9-axis",
            "Accuracy": "±0.01°",
            "Bias Repeatability": "0.001°/hr",
            "Interface": "SpaceWire, CAN",
            "Radiation Tolerance": "High",
            "Operating Temp": "-60°C to +150°C",
            "Application": "Spacecraft, satellite systems"
        },
        "datasheet": "datasheets/NS-IMU-600.pdf"
    }
]


############################конец блока датчиков########


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')



@app.route('/GYRO/gyroscope')
def gyroscope():
    return render_template('GYROS/gyroscope.html', gyroscope=GYROSCOPES)

@app.route('/GYROS/gyroscope/<string:sensor_id>')
def sensor_detail(sensor_id):
    sensor = next((s for s in SENSORS_GYRO if s["id"] == sensor_id), None)
    if not sensor:
        return "Sensor not found", 404
    return render_template('/GYROS/gyroproduct.html', sensor=sensor)




@app.route('/ACCEL/accelerometer')
def accelerometer():
    return render_template('/ACCEL/accelerometer.html', accelerometer=ACCEL)

@app.route('/ACCEL/accelerometer/<string:sensor_id>')
def accelerometer_detail(sensor_id):
    sensor = next((s for s in ACCEL_SENSORS if s["id"] == sensor_id), None)
    if not sensor:
        return "Sensor not found", 404
    return render_template('/ACCEL/accelproduct.html', sensor=sensor)



@app.route('/imu')
def imu():
    return render_template('IMU/imu.html', imus=IMU)

@app.route('/imu/<string:sensor_id>')
def imu_detail(sensor_id):
    sensor = next((s for s in IMU_SENSORS if s["id"] == sensor_id), None)
    if not sensor:
        return "Sensor not found", 404
    return render_template('IMU/IMUproduct.html', sensor=sensor)


if __name__ == '__main__':
    app.run(debug=True)