
from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from data.gyro_data import GYROSCOPES, SENSORS_GYRO
from data.accel_data import ACCEL_SENSORS, ACCEL
from data.imu_data import IMU_SENSORS, IMU



app = Flask(__name__)
app.secret_key = 'your_secret_key_here_12345'  # для flash-сообщений


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')




@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        # Обрабатываем форму
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Отправляем email (или сохраняем в БД)
        print(f"Сообщение от {name}: {message}")
        
        flash('Сообщение отправлено!', 'success')
        return redirect(url_for('contacts'))
    
    # Если GET — показываем страницу
    return render_template('contacts.html')





@app.route('/GYRO/gyroscope')
def gyroscope():
    return render_template('GYROS/gyroscope.html', gyroscope=GYROSCOPES)

@app.route('/GYROS/gyroscope/<string:sensor_id>', methods=['GET', 'POST'])
def sensor_detail(sensor_id):
    sensor = next((s for s in SENSORS_GYRO if s["id"] == sensor_id), None)
    if not sensor:
        return "Sensor not found", 404
    
    if request.method == 'POST':
        handle_contact_form(request.form, sensor['name'])
        flash('Сообщение успешно отправлено!', 'success')
        return redirect(url_for('sensor_detail', sensor_id=sensor_id))
    
    return render_template('/GYROS/gyroproduct.html', sensor=sensor)

@app.route('/ACCEL/accelerometer')
def accelerometer():
    return render_template('/ACCEL/accelerometer.html', accelerometer=ACCEL)

@app.route('/ACCEL/accelerometer/<string:sensor_id>', methods=['GET', 'POST'])
def accelerometer_detail(sensor_id):
    sensor = next((s for s in ACCEL_SENSORS if s["id"] == sensor_id), None)
    if not sensor:
        return "Sensor not found", 404
    
    if request.method == 'POST':
        handle_contact_form(request.form, sensor['name'])
        flash('Сообщение успешно отправлено!', 'success')
        return redirect(url_for('accelerometer_detail', sensor_id=sensor_id))
    
    return render_template('/ACCEL/accelproduct.html', sensor=sensor)

@app.route('/imu')
def imu():
    return render_template('IMU/imu.html', imus=IMU)

@app.route('/imu/<string:sensor_id>', methods=['GET', 'POST'])
def imu_detail(sensor_id):
    sensor = next((s for s in IMU_SENSORS if s["id"] == sensor_id), None)
    if not sensor:
        return "Sensor not found", 404
    
    if request.method == 'POST':
        handle_contact_form(request.form, sensor['name'])
        flash('Сообщение успешно отправлено!', 'success')
        return redirect(url_for('imu_detail', sensor_id=sensor_id))
    
    return render_template('IMU/IMUproduct.html', sensor=sensor)




def send_contact_email(name, email, subject, message):
    """Отправка email через Gmail"""
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "c72235531@gmail.com"        # ← ваш Gmail
        sender_password = "Radiant2025"   # ← 16-значный пароль
        recipient_email = "c72235531@gmail.com"     # ← куда отправлять
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Contact Form: {subject}"
        
        body = f"""
        Новое сообщение с сайта Navigation Systems
        
        Имя: {name}
        Email: {email}
        Тема: {subject}
        
        Сообщение:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        
    except Exception as e:
        print(f"Ошибка отправки email: {e}")
        raise




if __name__ == '__main__':
    app.run(debug=True)