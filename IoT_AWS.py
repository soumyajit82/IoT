import paho.mqtt.client as mq
import ssl

c=mq.Client()
cert=r"/Users/apple/Downloads/ca6728016c-certificate.pem.crt"
key=r"/Users/apple/Downloads/ca6728016c-private.pem.key"
rootca=r"/Users/apple/Downloads/VeriSign-Class3-Public-Primary-Certification-Authority-G5.pem"

c.tls_set(rootca,certfile=cert,keyfile=key,
	cert_reqs=ssl.CERT_REQUIRED,
	tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None)

c.connect('a26hx0mmuuders.iot.ap-south-1.amazonaws.com',8883)
def onc(c,userdata,flag,rc):
	print('Connection code with AWS is', rc)
	c.subscribe('mytopic/iot')

def onm(c,userdata,msg):
	m=msg.payload.decode()
	print(m)
	if m=='temp':
		data='{"temperature":45}'
		c.publish('mytopic/iot',data)

c.on_connect=onc
c.on_message=onm
c.loop_forever()

