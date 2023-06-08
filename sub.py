def registerOfflineSubscriber():
    """Just a durable client to trigger queuing"""
    client = paho.mqtt.client.Client("sub-qos1-offline", clean_session=False)
    client.connect("localhost", 1883)
    client.subscribe("test/publish/queueing/#", 1)
    client.loop()
    client.disconnect()
    
registerOfflineSubscriber
