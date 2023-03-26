import paho.mqtt.client as mqtt
import random
import time

# Configuração do cliente MQTT
broker_address = "irrigation.com"
broker_port = 1883
client = mqtt.Client("irrigation")
client.connect(broker_address, broker_port)

# Simulação dos valores de umidade do solo
def simular_leitura_sensor():
    return random.randint(0, 100) # Retorna um valor aleatório entre 0 e 100

# Envia os valores simulados para o broker MQTTX
def enviar_leitura_para_mqtt():
    valor_sensor = simular_leitura_sensor()
    mensagem = "Valor de umidade do solo: " + str(valor_sensor)
    client.publish("topico/sensor_umidade", mensagem)