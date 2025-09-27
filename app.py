
# from flask import Flask, render_template, request, flash, redirect, url_for
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import os
# from data.gyro_data import GYROSCOPES, SENSORS_GYRO
# from data.accel_data import ACCEL_SENSORS, ACCEL
# from data.imu_data import IMU_SENSORS, IMU



# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here_12345'  # для flash-сообщений


# def send_contact_form(name, email, message, sensor_name):
#     """Отправка email через Gmail"""
#     try:
#         import smtplib
#         from email.mime.text import MIMEText
#         from email.mime.multipart import MIMEMultipart
        
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login("ваш_email@gmail.com", "ваш_16_значный_пароль")
        
#         msg = MIMEMultipart()
#         msg['From'] = "ваш_email@gmail.com"
#         msg['To'] = "ваш_email@gmail.com"
#         msg['Subject'] = f"Новое сообщение по датчику {sensor_name}".encode('utf-8').decode('utf-8')
        
#         body = f"""
#         Новое сообщение с сайта Navigation Systems
        
#         Датчик: {sensor_name}
        
#         Имя: {name}
#         Email: {email}
#         Сообщение: {message}
#         """
        
#         # Альтернативный способ
#         text_part = MIMEText(body, 'plain', 'utf-8')
#         msg.attach(text_part)
        
#         server.send_message(msg)
#         server.quit()
        
#     except Exception as e:
#         print(f"Ошибка отправки: {e}")
#         raise


# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/products')
# def products():
#     return render_template('products.html')





# @app.route('/GYRO/gyroscope')
# def gyroscope():
#     return render_template('GYROS/gyroscope.html', gyroscope=GYROSCOPES)

# @app.route('/GYROS/gyroscope/<string:sensor_id>', methods=['GET', 'POST'])
# def sensor_detail(sensor_id):
#     sensor = next((s for s in SENSORS_GYRO if s["id"] == sensor_id), None)
#     if not sensor:
#         return "Sensor not found", 404
    
#     if request.method == 'POST':
#         # Получаем данные из формы
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')
        
#         try:
#             send_contact_form(name, email, message, sensor['name'])
#             flash('Сообщение успешно отправлено!', 'success')
#         except Exception as e:
#             flash(f'Error sending: {str(e)}', 'error')
        
#         return redirect(url_for('sensor_detail', sensor_id=sensor_id))
    
#     return render_template('/GYROS/gyroproduct.html', sensor=sensor)




# @app.route('/ACCEL/accelerometer')
# def accelerometer():
#     return render_template('/ACCEL/accelerometer.html', accelerometer=ACCEL)

# @app.route('/ACCEL/accelerometer/<string:sensor_id>', methods=['GET', 'POST'])
# def accelerometer_detail(sensor_id):
#     sensor = next((s for s in ACCEL_SENSORS if s["id"] == sensor_id), None)
#     if not sensor:
#         return "Sensor not found", 404
    
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')
        
#         try:
#             send_contact_form(name, email, message, sensor['name'])
#             flash('Сообщение успешно отправлено!', 'success')
#         except Exception as e:
#             flash(f'Error sending: {str(e)}', 'error')
        
#         return redirect(url_for('accelerometer_detail', sensor_id=sensor_id))
    
#     return render_template('/ACCEL/accelproduct.html', sensor=sensor)

# @app.route('/imu')
# def imu():
#     return render_template('IMU/imu.html', imus=IMU)

# @app.route('/imu/<string:sensor_id>', methods=['GET', 'POST'])
# def imu_detail(sensor_id):
#     sensor = next((s for s in IMU_SENSORS if s["id"] == sensor_id), None)
#     if not sensor:
#         return "Sensor not found", 404
    
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         message = request.form.get('message')
        
#         try:
#             send_contact_form(name, email, message, sensor['name'])
#             flash('Сообщение успешно отправлено!', 'success')
#         except Exception as e:
#             flash(f'Error sending: {str(e)}', 'error')
        
#         return redirect(url_for('imu_detail', sensor_id=sensor_id))
    
#     return render_template('IMU/IMUproduct.html', sensor=sensor)


# # Настройки Gmail
# GMAIL_USER = "fb986580@gmail.com"
# GMAIL_PASSWORD = "efin eyrf xqiz vryr"

# def send_email(name, email, subject, message):
#     """Отправка письма через Gmail"""
#     try:
#         # Создаем соединение
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()  # Шифрование
#         server.login(GMAIL_USER, GMAIL_PASSWORD)
        
#         # Создаем письмо
#         msg = MIMEMultipart()
#         msg['From'] = GMAIL_USER
#         msg['To'] = GMAIL_USER  # Отправляется себе
#         msg['Subject'] = f"Сообщение с сайта: {subject}"
        
#         body = f"""
#         Новое сообщение с сайта Navigation Systems
        
#         Имя: {name}
#         Email: {email}
#         Тема: {subject}
        
#         Сообщение:
#         {message}
#         """
        
#         msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
#         # Отправляем
#         server.send_message(msg)
#         server.quit()
        
#         print(f"✅ Message send!: {name} - {subject}")
        
#     except Exception as e:
#         print(f"❌ Error: {e}")
#         raise

# @app.route('/contacts', methods=['GET', 'POST'])
# def contacts():
#     if request.method == 'POST':
#         # Получаем данные из формы
#         name = request.form.get('name')
#         email = request.form.get('email')
#         subject = request.form.get('subject')
#         message = request.form.get('message')
        
#         try:
#             # Отправляем письмо
#             send_email(name, email, subject, message)
#             flash('Сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.', 'success')
#         except Exception as e:
#             flash(f'Ошибка при отправке: {str(e)}', 'error')
        
#         return redirect(url_for('contacts'))
    
#     return render_template('contacts.html')


# if __name__ == '__main__':
#     app.run(debug=True)










from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from data.gyro_data import GYROSCOPES, SENSORS_GYRO
from data.accel_data import ACCEL_SENSORS, ACCEL
from data.imu_data import IMU_SENSORS, IMU
from data.news_data import NEWS

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_12345'  # для flash-сообщений

# Настройки Gmail
GMAIL_USER = "fb986580@gmail.com"
GMAIL_PASSWORD = "efin eyrf xqiz vryr"

def send_contact_form(name, email, message, sensor_name):
    """Send email through Gmail"""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = GMAIL_USER
        msg['Subject'] = f"New message about {sensor_name}"
        
        body = f"""
        New message from Navigation Systems website
        
        Sensor: {sensor_name}
        
        Name: {name}
        Email: {email}
        Message: {message}
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        server.send_message(msg)
        server.quit()
        
    except Exception as e:
        print(f"Error sending: {e}")
        raise

def send_email(name, email, subject, message):
    """Send email through Gmail"""
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        
        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = GMAIL_USER
        msg['Subject'] = f"Contact Form: {subject}"
        
        body = f"""
        New message from Navigation Systems website
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Message sent: {name} - {subject}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

@app.route('/')
def home():
    return render_template('index.html', news=NEWS)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        try:
            send_email(name, email, subject, message)
            flash('Message sent successfully! We will contact you soon.', 'success')
        except Exception as e:
            flash(f'Error sending message: {str(e)}', 'error')
        
        return redirect(url_for('contacts'))
    
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
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        try:
            send_contact_form(name, email, message, sensor['name'])
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Error sending: {str(e)}', 'error')
        
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
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        try:
            send_contact_form(name, email, message, sensor['name'])
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Error sending: {str(e)}', 'error')
        
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
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        try:
            send_contact_form(name, email, message, sensor['name'])
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Error sending: {str(e)}', 'error')
        
        return redirect(url_for('imu_detail', sensor_id=sensor_id))
    
    return render_template('IMU/IMUproduct.html', sensor=sensor)

@app.route('/news')
def news():
    return render_template('news.html', news=NEWS)

@app.route('/news/<string:news_id>')
def news_detail(news_id):
    news_item = next((n for n in NEWS if n["id"] == news_id), None)
    if not news_item:
        return "News not found", 404
    
    return render_template('news_detail.html', news_item=news_item)

if __name__ == '__main__':
    app.run(debug=True)