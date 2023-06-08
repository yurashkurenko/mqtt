import os.path

# Замените /Users/gaston/python_certificates на тот путь,
# в которм вы сохранили свой файл сертификата центра авторизации,
# сертификат клиента и ключ клиента
certificates_path = "/Users/gaston/python_certificates"
ca_certificate = os.path.join(certificates_path, "ca.crt")
client_certificate = os.path.join(certificates_path, "board001.crt")
client_key = os.path.join(certificates_path, "board001.key")
# Замените 192.168.1.101 на IP или hostname для вашего Mosquitto
# или иного сервера MQTT
# Проверьте что IP или hostname соответствуют тому значению,
# которое вы применяете для обычного названия
mqtt_server_host = "192.168.1.101"
mqtt_server_port = 8883
mqtt_keepalive = 60
