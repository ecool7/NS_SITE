GYROSCOPES = [
{
    "name": "NSGFZH",
    "range": "±400°/s",
    "application": "Aviation, military drones",
    "technology": "MEMS (Micro-Electro-Mechanical Systems)",
    "image": "NSGFZH.png"
},
{
    "name": "NSLG120",
    "range": "±400°/s",
    "application": "Space systems, satellite navigation",
    "technology": "laser gyroscope",
    "image": "NSLG120.png"
},
{
    "name": "NSLG90",
    "range": "±400°/s",
    "application": "UAVs, autonomous vehicles",
    "technology": "laser gyroscope",
    "image": "NSLG90.png"
},
{
    "name": "NSLG70",
    "range": "±400°/s",
    "application": "Small drones, robotics",
    "technology": "laser gyroscope",
    "image": "NSLG70.png"
},
{
    "name": "NSOG3-30",
    "range": "±500°/s",
    "application": "Missile guidance, precision targeting",
    "technology": "fiber optic gyroscope",
    "image": "NSOG3-30.png"
},
{
    "name": "NSLG40",
    "range": "±400°/s",
    "application": "Micro-drones, wearable devices",
    "technology": "laser gyroscope",
    "image": "NSLG40.png"
}
]

SENSORS_GYRO = [

  {
     "id": "NSLG40",
    "name": "NSLG40",
    "image": "NSLG40.png",
    "description": "Ultra-compact and lightweight gyroscope suitable for micro-drones and portable systems requiring high accuracy.",
    "specs": {
        "Range": "±400°/s",
        "Bias Stability": "≤0.007°/h",
        "Bias Repeatability": "≤0.007°/h",
        "Scale Factor Repeatability": "≤5 ppm",
        "Scale Factor Nonlinearity": "≤5 ppm",
        "Operating Temp": "-45°C to +70°C",
        "Vibration Resistance": "7g (20–2000 Hz)",
        "Dimensions": "67 x 59 x 18 mm",
        "Weight": "0.15 kg"
	},
        "datasheet": "datasheets/NS-GYR-100.pdf"
    },
  {
    "id": "NSGFZH",
    "name": "NSGFZH",
    "image": "NSGFZH.png",
    "description": "High-precision MEMS gyroscope for aviation and military applications, featuring low noise and high stability.",
    "specs": {
        "Range": "±400°/s",
        "Application": "Aviation, military drones, navigation systems",
        "Technology": "MEMS (Micro-Electro-Mechanical Systems)",
        "Operating Temp": "-40°C to +85°C",
        "Output": "Digital (SPI)",
        "Power": "5V DC",
        "Bias Instability": "<0.05 °/h",
        "Bias Stability (1σ)": "<1.5 °/h",
        "Repeatability of Bias": "<0.5 °/h",
        "Scale Factor at 25°C": "20000 LSB/(°/s)",
        "Scale Factor Repeatability": "<20 ppm",
        "Temperature Effect on Scale Factor": "<100 ppm (1σ)",
        "Scale Factor Nonlinearity": "<100 ppm",
        "Noise Density": "<0.025 °/√h",
	},
        "datasheet": "datasheets/NS-GYR-100.pdf"
    },

 {
   "id": "NSLG120",
    "name": "NSLG120",
    "image": "NSLG120.png",
    "description": "High-precision laser gyroscope for aviation and military applications with high stability and low noise.",
    "specs": {
        "Range": "±400°/s",
        "Bias Stability": "≤0.001°/h",
        "Repeatability of Bias": "≤0.0005°/h",
        "Scale Factor Repeatability": "≤1 ppm",
        "Nonlinearity of Scale Factor": "≤1 ppm",
        "Operating Temp": "-45°C to +70°C",
        "Vibration Resistance": "7g (20–2000 Hz)",
        "Dimensions": "149 x 132 x 31 mm",
        "Weight": "1.02 kg",
	},
        "datasheet": "datasheets/NS-GYR-100.pdf"
    },



 {
    "id": "NSLG90",
    "name": "NSLG90",
    "image": "NSLG90.png",
    "description": "Compact high-accuracy gyroscope suitable for UAVs and navigation systems requiring excellent bias stability.",
    "specs": {
        "Range": "±400°/s",
        "Bias Stability": "≤0.003°/h",
        "Repeatability of Bias": "≤0.002°/h",
        "Scale Factor Repeatability": "≤2 ppm",
        "Nonlinearity of Scale Factor": "≤2 ppm",
        "Operating Temp": "-45°C to +70°C",
        "Vibration Resistance": "7g (20–2000 Hz)",
        "Dimensions": "124 x 107 x 31 mm",
        "Weight": "0.68 kg"
	},
        "datasheet": "datasheets/NS-GYR-100.pdf"
    },

 
 {
     "id": "NSLG70",
    "name": "NSLG70",
    "image": "NSLG70.png",
    "description": "Compact and lightweight gyroscope ideal for small drones and portable navigation systems.",
    "specs": {
        "Range": "±400°/s",
        "Bias Stability": "≤0.005°/h",
        "Repeatability of Bias": "≤0.003°/h",
        "Scale Factor Repeatability": "≤4 ppm",
        "Nonlinearity of Scale Factor": "≤4 ppm",
        "Operating Temp": "-45°C to +70°C",
        "Vibration Resistance": "7g (20–2000 Hz)",
        "Dimensions": "98 x 82 x 26 mm",
        "Weight": "0.34 kg"
	},
        "datasheet": "datasheets/NS-GYR-100.pdf"
    },  

 {
    "id": "NSOG3-30",
    "name": "NSOG3-30",
    "image": "NSOG3-30.png",
    "description": "Compact and high-performance fiber optic gyroscope designed for aviation and military drones with fast startup and excellent bias stability.",
    "specs": {
        "Range": "±500°/s",
        "Startup Time": "3 seconds",
        "Bias Offset": "≤0.1°/h",
        "Bias Stability (Constant Temp)": "≤0.5°/h",
        "Bias Stability (Full Temp Range)": "≤1°/h",
        "Bias Repeatability": "≤0.3°/h",
        "Angle Random Walk": "≤0.02°/√h",
        "Scale Factor Repeatability": "≤20 ppm",
        "Scale Factor Nonlinearity": "≤20 ppm",
        "Operating Temp": "-45°C to +70°C",
        "Bandwidth": ">500 Hz",
        "Vibration Resistance": "7g (20–2000 Hz)",
        "Dimensions": "60 mm × 35 mm × 31 mm",
        "Weight": "Not specified"
	},
        "datasheet": "datasheets/NS-GYR-100.pdf"
    },  
]