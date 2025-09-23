IMU = [
 {
        "id": "NSI313",
        "name": "NSI313",
        "type": "6-axis",
        "application": "Industrial automation, robotics",
        "image": "nsi313.png"
    },
    {
        "id": "NSI312",
        "name": "NSI312",
        "type": "6-axis",
        "application": "Drones, navigation systems",
        "image": "nsi312.png"
    },
    {
        "id": "NSI325",
        "name": "NSI325",
        "type": "6-axis",
        "application": "Military, aerospace applications",
        "image": "nsi325.png"
    },
        {
        "id": "NSI6F1",
        "name": "NSI6F1",
        "type": "6-axis",
        "application": "Industrial automation, robotics",
        "image": "nsi6f1.png"
    },
    {
        "id": "NSI6F1A",
        "name": "NSI6F1A",
        "type": "6-axis",
        "application": "Precision navigation, drones",
        "image": "nsi6f1a.png"
    },
        {
        "id": "NSI9F1",
        "name": "NSI9F1",
        "type": "6-axis",
        "application": "Military drones, precision navigation",
        "image": "nsi9ft.png"
    },
    {
        "id": "NSI9F2",
        "name": "NSI9F2",
        "type": "6-axis",
        "application": "High-accuracy inertial systems, aerospace",
        "image": "nsi9f2.png"
    }

]

# Подробные данные для детальных страниц
IMU_SENSORS = [
    {
        "id": "NSI313",
        "name": "NSI313",
        "image": "nsi313.png",
        "description": "High-performance 6-axis IMU with MEMS gyroscope and accelerometer, designed for industrial and robotic applications with high stability and accuracy.",
        "specs": {
            "Axes": "6 (3 Accel + 3 Gyro)",
            "Gyro Range": "±450°/s",
            "Accel Range": "±16 g",
            "Bias Stability (Gyro)": "≤10 °/h",
            "Bias Drift (Gyro)": "≤2.5 °/h",
            "Scale Factor Nonlinearity (Gyro)": "≤150 ppm",
            "Orthogonality Error": "±0.05°",
            "Null Offset Repeatability": "≤10 °/h",
            "Noise Density": "≥-150 dB",
            "Null Drift (Temp)": "≤150 °/h",
            "Acceleration Effect": "–",
            "Data Rate": "921600 bps",
            "Update Rate": "200–400 Hz",
            "Operating Temp": "-40°C to +85°C",
            "Dimensions": "25.5×22.4×9.7 mm",
            "Power": "5±0.3 V"
        },
        "datasheet": "datasheets/NS313.pdf"
    },
    {
        "id": "NSI312",
        "name": "NSI312",
        "image": "nsi312.png",
        "description": "Compact 6-axis IMU with excellent performance for drones and navigation systems, featuring low noise and high reliability.",
        "specs": {
            "Axes": "6 (3 Accel + 3 Gyro)",
            "Gyro Range": "±500°/s",
            "Accel Range": "±16 g",
            "Bias Stability (Gyro)": "10 °/h",
            "Bias Drift (Gyro)": "2 °/h",
            "Scale Factor Nonlinearity (Gyro)": "180 ppm",
            "Orthogonality Error": "±0.05°",
            "Null Offset Repeatability": "≥150 °/h",
            "Noise Density": "≥-150 dB",
            "Null Drift (Temp)": "≤100 °/h",
            "Acceleration Effect": "8 %/g",
            "Data Rate": "921600 bps",
            "Update Rate": "200–400 Hz",
            "Operating Temp": "-40°C to +85°C",
            "Dimensions": "22.4×22.4×9.0 mm",
            "Power": "5±0.3 V"
        },
        "datasheet": "datasheets/NS312.pdf"
    },
    {
        "id": "NSI325",
        "name": "NSI325",
        "image": "nsi325.png",
        "description": "Robust 6-axis IMU designed for harsh environments, suitable for military and aerospace applications with high vibration resistance and temperature stability.",
        "specs": {
            "Axes": "6 (3 Accel + 3 Gyro)",
            "Gyro Range": "±480°/s",
            "Accel Range": "±16 g",
            "Bias Stability (Gyro)": "≤8 °/h",
            "Bias Drift (Gyro)": "≤2.5 °/h",
            "Scale Factor Nonlinearity (Gyro)": "≤150 ppm",
            "Orthogonality Error": "±0.7°",
            "Null Offset Repeatability": "≤5 °/h",
            "Noise Density": "≥-150 dB",
            "Null Drift (Temp)": "≤100 °/h",
            "Acceleration Effect": "8 %/g",
            "Data Rate": "921600 bps",
            "Update Rate": "200–400 Hz",
            "Operating Temp": "-40°C to +85°C",
            "Dimensions": "24.0×22.4×9.0 mm",
            "Power": "5±0.1 V"
        },
        "datasheet": "datasheets/NS325.pdf"
    },
            {
        "id": "NSI6F1",
        "name": "NSI6F1",
        "image": "nsi6f1.png",
        "description": "High-precision 6-axis IMU with MEMS gyroscope and accelerometer, designed for industrial and robotic applications requiring high stability and low noise.",
        "specs": {
            "Axes": "6 (3 Accel + 3 Gyro)",
            "Gyro Range": "±400°/s",
            "Accel Range": "±10 g",
            "Bias Stability (Gyro)": "<3 °/h",
            "Bias Drift (Gyro)": "≤0.3 °/h",
            "Scale Factor Nonlinearity (Gyro)": "≤0.02% of range",
            "Orthogonality Error": "±0.05°",
            "Null Repeatability": "1 °/h",
            "Noise Density": "0.1 °/√h",
            "Temperature Effect on Bias": "±0.15 °/h/°C",
            "Acceleration Effect": "1 %/g",
            "Data Rate": "RS422",
            "Update Rate": "200 Hz",
            "Operating Temp": "-45°C to +85°C",
            "Power": "5±0.5 V"
        },
        "datasheet": "datasheets/NSI6F1.pdf"
    },
    {
        "id": "NSI6F1A",
        "name": "NSI6F1A",
        "image": "nsi6f1a.png",
        "description": "Enhanced version of NSI6F1 with improved bias stability and temperature performance, ideal for precision navigation and drone stabilization systems.",
        "specs": {
            "Axes": "6 (3 Accel + 3 Gyro)",
            "Gyro Range": "±400°/s",
            "Accel Range": "±10 g",
            "Bias Stability (Gyro)": "<1 °/h",
            "Bias Drift (Gyro)": "≤0.1 °/h",
            "Scale Factor Nonlinearity (Gyro)": "≤0.02% of range",
            "Orthogonality Error": "±0.05°",
            "Null Repeatability": "0.5 °/h",
            "Noise Density": "0.05 °/√h",
            "Temperature Effect on Bias": "±0.1 °/h/°C",
            "Acceleration Effect": "1 %/g",
            "Data Rate": "RS422",
            "Update Rate": "200 Hz",
            "Operating Temp": "-45°C to +85°C",
            "Power": "5±0.5 V"
        },
        "datasheet": "datasheets/NSI6F1A.pdf"},
            {
        "id": "NSI9F1",
        "name": "NSI9F1",
        "image": "nsi9f1.png",
        "description": "High-performance 6-axis IMU with MEMS gyroscope and accelerometer, designed for military and aerospace applications requiring high stability and low noise.",
        "specs": {
            "Axes": "6 (3 Accel + 3 Gyro)",
            "Gyro Range": "±1000°/s",
            "Accel Range": "±10 g",
            "Bias Stability (Gyro)": "≤0.6 °/h",
            "Bias Drift (Gyro)": "≤0.3 °/h",
            "Scale Factor Nonlinearity": "≤0.02% of range",
            "Orthogonality Error": "≤0.05°",
            "Null Repeatability": "≤0.04 °/h",
            "Noise Density": "0.05 °/√h",
            "Temperature Effect on Bias": "±0.1 °/h/°C",
            "Data Rate": "RS422",
            "Update Rate": "200 Hz",
            "Operating Temp": "-45°C to +85°C",
            "Power": "5±0.5 V",
            "Dimensions": "47×44×15 mm"
        },
        "datasheet": "datasheets/NSI9FT.pdf"
    },
    {
        "id": "NSI9F2",
        "name": "NSI9F2",
        "image": "nsi9f2.png",
        "description": "Ultra-precise 6-axis IMU with enhanced bias stability and temperature performance, ideal for high-end inertial navigation and autonomous platforms.",
        "specs": {
            "Axes": "6 (3 Accel + 3 Gyro)",
            "Gyro Range": "±400°/s",
            "Accel Range": "±10 g",
            "Bias Stability (Gyro)": "≤0.1 °/h",
            "Bias Drift (Gyro)": "≤0.03 °/h",
            "Scale Factor Nonlinearity": "≤0.02% of range",
            "Orthogonality Error": "≤0.05°",
            "Null Repeatability": "≤0.004 °/h",
            "Noise Density": "0.02 °/√h",
            "Temperature Effect on Bias": "±0.02 °/h/°C",
            "Data Rate": "RS422",
            "Update Rate": "1000 Hz",
            "Operating Temp": "-45°C to +85°C",
            "Power": "5±0.5 V",
            "Dimensions": "47×44×15 mm"
        },
        "datasheet": "datasheets/NSI9F2.pdf"
    }

];