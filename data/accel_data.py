
ACCEL = [
    {
        "id": "NSAEM1010",
        "name": "NSAEM1010",
        "Bias": "< 0.1mg",
        "application": "Aviation, robotics",
        "image": "NSAEM1010.png"
    },
    {
        "id": "NSA4000D",
        "name": "NSA4000D",
        "Bias": "< 0.02mg",
        "application": "Industrial systems",
        "image": "NSA4000D.png"
    },
    {
        "id": "NSQAD",
        "name": "NSQAD",
        "Bias": "< 5mg",
        "application": "Structural monitoring",
        "image": "NSQAD.png"  
    },
        {
        "id": "NSA290",
        "name": "NSA290",
        "type": "3-axis accelerometer",
        "application": "Industrial sensors, vibration monitoring",
        "image": "nsa290.png"
    },

  {
        "id": "NSA1001-02",
        "name": "NSA1001-02",
        "type": "3-axis accelerometer",
        "application": "Medical devices, precision measurement",
        "image": "nsa1001-02.png"
    },
  
    {
        "id": "NSA1005-50",
        "name": "NSA1005-50",
        "type": "3-axis accelerometer",
        "application": "Automotive testing, structural analysis",
        "image": "nsa1005-50.png"
    },
    {
        "id": "NSA1009-1K",
        "name": "NSA1009-1K",
        "type": "3-axis accelerometer",
        "application": "Extreme shock testing, military systems",
        "image": "nsa1009-1k.png"
    },
        {
        "id": "NSQA11-03",
        "name": "NSQA11-03",
        "type": "3-axis accelerometer",
        "application": "High-precision measurement, scientific research",
        "image": "nsqa11-03.png"
    },
        {
        "id": "NSQA12-03",
        "name": "NSQA12-03",
        "type": "3-axis accelerometer",
        "application": "Industrial vibration monitoring, structural health",
        "image": "nsqa12-03.png"
    },
        {
        "id": "NSQA13-02",
        "name": "NSQA13-02",
        "type": "3-axis accelerometer",
        "application": "Industrial vibration monitoring, structural health",
        "image": "nsqa13-02.png"
    }


]

ACCEL_SENSORS = [
    {
        "id": "NSAEM1010",
        "name": "NSAEM1010",
        "image": "NSAEM1010.png",
        "description": "ANALOG COLIBRYS",
        "specs": {
            "Measurement Range": "±2g...±30g",
            "Bias": "< 0.01",
            "Frequency Response": "20 Hz to 2 kHz",
            "Noise Level": "30 µg/√Hz",
            "Application": "Aviation, robotics, vibration monitoring",
            "Interface": "Analog output",
            "Operating Temp": "-55°C to +125°C",
            "Power Supply": "5V DC"
        },
        "datasheet": "datasheets/NS-ACC-100.pdf"
    },
    {
        "id": "NSA4000D",
        "name": "NSA4000D",
        "image": "NSA4000D.png",
        "description": "Digital MEMS-based accelerometer with SPI interface for industrial and navigation systems.",
        "specs": {
            "Measurement Range": "±2g...±50g",
            "Bias": "< 0.02 mg",
            "Interface": "SPI",
            "Bandwidth": "300 Hz",
            "Application": "Industrial automation, inertial navigation",
            "Operating Temp": "-45°C to +85°C",
        },
        "datasheet": "datasheets/NS-ACC-200.pdf"
    },
    {
        "id": "NSQAD",
        "name": "NSQAD",
        "image": "NSQAD.png",
        "description": "Digital Q-FLEX accelerometer for structural health monitoring.",
        "specs": {
            "Measurement Range": "±30g...±70g",
            "Bias": "< 0.02 mg",
            "Output": "Digital",
            "Bandwidth": "100 Hz",
            "Application": "Structural monitoring, military vehicles",
            "Operating Temp": "-40°C to +85°C",
            "Power Supply": "12-15V DC"
        },
        "datasheet": "datasheets/NS-ACC-300.pdf"
    },
    {
        "id": "NSA290",
        "name": "NSA290",
        "image": "nsa290.png",
        "description": "Compact 3-axis MEMS accelerometer with high resolution and low power consumption, suitable for industrial applications and vibration monitoring.",
        "specs": {
            "Measurement Range": "±2g, ±4g, ±8g, ±16g",
            "Sensitivity": "4096 LSB/g (±2g), 2048 LSB/g (±4g), 1024 LSB/g (±8g), 512 LSB/g (±16g)",
            "Zero Output": "±70 mg",
            "Output Data Rate": "1–1000 Hz",
            "Interface": "I²C / SPI",
            "Supply Voltage": "1.62–3.6 V",
            "Operating Temp": "-40°C to +85°C",
            "Dimensions": "2×2×0.9 mm",
            "Shock Resistance": "1000g × 200 μs",
            "Power Consumption": "Not specified"
        },
        "datasheet": "datasheets/NSA290.pdf"
    },
        {
        "id": "NSA1001-02",
        "name": "NSA1001-02",
        "image": "nsa1001-02.png",
        "description": "Ultra-high-precision 3-axis MEMS accelerometer with low noise and excellent stability, ideal for medical and scientific applications.",
        "specs": {
            "Measurement Range": "±2g",
            "Sensitivity": "800±8 mV/g",
            "Zero Output": "2.5±0.05 V",
            "Bias Stability": "≤0.10 mg",
            "Repeatability": "≤0.10 mg",
            "Scale Factor Stability": "≤200 ppm",
            "Nonlinearity": "≤0.30%",
            "Output Data Rate": "1–50 Hz",
            "Bandwidth (3dB)": "800 Hz",
            "Temp Coefficient of Zero": "≤0.20 mg/°C",
            "Temp Coefficient of Sensitivity": "≤200 ppm/°C",
            "Operating Temp": "-55°C to +125°C",
            "Storage Temp": "-55°C to +125°C",
            "Supply Voltage": "5 V",
            "Dimensions": "6.2×6.2×2.5 mm"
        },
        "datasheet": "datasheets/NSA1001-02.pdf"
    },
        {
        "id": "NSA1005-50",
        "name": "NSA1005-50",
        "image": "nsa1005-50.png",
        "description": "High-performance 3-axis accelerometer with wide dynamic range for automotive and structural testing.",
        "specs": {
            "Measurement Range": "±50g",
            "Sensitivity": "40±1 mV/g",
            "Zero Output": "2.5±0.05 V",
            "Bias Stability": "≤2.5 mg",
            "Repeatability": "≤2.5 mg",
            "Scale Factor Stability": "≤300 ppm",
            "Nonlinearity": "≤0.50%",
            "Output Data Rate": "1–150 Hz",
            "Bandwidth (3dB)": "3000 Hz",
            "Temp Coefficient of Zero": "≤4.0 mg/°C",
            "Temp Coefficient of Sensitivity": "≤300 ppm/°C",
            "Operating Temp": "-55°C to +125°C",
            "Storage Temp": "-55°C to +125°C",
            "Supply Voltage": "5 V",
            "Dimensions": "6.2×6.2×2.5 mm"
        },
        "datasheet": "datasheets/NSA1005-50.pdf"
    },
        {
        "id": "NSA1009-1K",
        "name": "NSA1009-1K",
        "image": "nsa1009-1k.png",
        "description": "Ultra-high-g 3-axis accelerometer for military, aerospace, and shock testing applications.",
        "specs": {
            "Measurement Range": "±1000g",
            "Sensitivity": "2.0±0.3 mV/g",
            "Zero Output": "2.5±0.05 V",
            "Bias Stability": "≤50 mg",
            "Repeatability": "≤50 mg",
            "Scale Factor Stability": "≤500 ppm",
            "Nonlinearity": "≤1.0%",
            "Output Data Rate": "1–250 Hz",
            "Bandwidth (3dB)": "10000 Hz",
            "Temp Coefficient of Zero": "≤80 mg/°C",
            "Temp Coefficient of Sensitivity": "≤500 ppm/°C",
            "Operating Temp": "-55°C to +125°C",
            "Storage Temp": "-55°C to +125°C",
            "Supply Voltage": "5 V",
            "Dimensions": "9×9×2.5 mm"
        },
        "datasheet": "datasheets/NSA1009-1K.pdf"
    },
        {
        "id": "NSQA11-03",
        "name": "NSQA11-03",
        "image": "nsqa11-03.png",
        "description": "Ultra-high-sensitivity 3-axis MEMS accelerometer with low noise and excellent stability, designed for precision scientific measurements and laboratory applications.",
        "specs": {
            "Measurement Range": "±50g, ±60g, ±70g",
            "Noise Density": "≤20 mg/√Hz",
            "Zero Output": "±3mg",
            "Scale Factor": "1.0–1.30 mA/g",
            "Nonlinearity (2nd order)": "≤20 mg/g²",
            "Bias Stability (4h)": "≤10 mg",
            "Drift (Monthly)": "≤30 ppm",
            "Repeatability of Scale Factor": "≤20 mg/g²",
            "Temp Coefficient of Zero": "≤8.4 mg/°C",
            "Bandwidth": "20–2500 Hz",
            "Noise Floor": "6g (20–2000 Hz)",
            "Operating Temp": "-60°C to +120°C",
            "Supply Voltage": "12±1.5 V",
            "Temperature Sensor": "Optional",
            "Dimensions": "Φ25.4×30 mm"
        },
        "datasheet": "datasheets/NSQA11-03.pdf"
    },
     {
        "id": "NSQA12-03",
        "name": "NSQA12-03",
        "image": "nsqa12-03.png",
        "description": "High-performance 3-axis MEMS accelerometer with wide dynamic range and excellent stability, ideal for industrial vibration monitoring and structural analysis.",
        "specs": {
            "Measurement Range": "±70g, ±100g",
            "Noise Density": "≤56 μg/√Hz",
            "Zero Output": "±45 mg",
            "Scale Factor": "0.8–1.2 mA/g",
            "Nonlinearity (2nd order)": "≤20 mg/g²",
            "Bias Stability (4h)": "≤10 ppm",
            "Drift (Monthly)": "≤25 mg",
            "Repeatability of Scale Factor": "≤30 ppm",
            "Temp Coefficient of Zero": "≤30 mg/°C",
            "Temp Coefficient of Sensitivity": "≤50 ppm/°C",
            "Bandwidth": "100–2500 Hz",
            "Output": "100g, 8ms, 1/2in",
            "Operating Temp": "-65°C to +120°C",
            "Storage Temp": "-40°C to +120°C",
            "Supply Voltage": "12±1.5 V",
            "Temperature Sensor": "Optional",
            "Dimensions": "Φ25.4×30 mm"
        },
        "datasheet": "datasheets/NSQA12-03.pdf"
    },
    {
        "id": "NSQA13-02",
        "name": "NSQA13-02",
        "image": "nsqa13-02.png",
        "description": "High-performance 3-axis MEMS accelerometer with wide dynamic range and excellent stability, ideal for industrial vibration monitoring and structural analysis.",
        "specs": {
            "Measurement Range": "±60g",
            "Noise Density": "≤8 μg/√Hz",
            "Zero Output": "±15 mg",
            "Scale Factor": "1.0±0.2 mA/g",
            "Nonlinearity (2nd order)": "≤15 mg/g²",
            "Bias Stability (4h)": "≤20 ppm",
            "Drift (Monthly)": "≤50 mg",
            "Repeatability of Scale Factor": "≤50 ppm",
            "Temp Coefficient of Zero": "≤50 mg/°C",
            "Temp Coefficient of Sensitivity": "≤60 ppm/°C",
            "Bandwidth": "180–2500 Hz",
            "Output": "180g, 4.8ms, 1/2in",
            "Operating Temp": "-65°C to +85°C",
            "Storage Temp": "-40°C to +120°C",
            "Supply Voltage": "12±1.5 V",
            "Temperature Sensor": "Optional",
            "Dimensions": "Φ18.2×23 mm"
        },
        "datasheet": "datasheets/NSQA13-02.pdf"
    }

]