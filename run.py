#!/usr/bin/env python

import json
import paho.mqtt.publish as publish
import tellcore.telldus as td

with open('settings.json') as data_file:    
    settings = json.load(data_file)

def raw_event(data, controller_id, cid):
    string = "[RAW] {0} <- {1}".format(controller_id, data)
    values = dict(s.split(':') for s in data.split(';')[:-1])
    auth = {'username':settings["username"], 'password':settings["password"]} 
    publish.single(settings["prefix"]+"/receiveaddress/"+values['house']+"/"+values['unit'], values['method'], hostname=settings["hostname"], auth = auth)
    publish.single(settings["prefix"]+"/receiveall/", json.dumps(values), hostname=settings["hostname"], auth = auth)


try:
    import asyncio
    loop = asyncio.get_event_loop()
    dispatcher = td.AsyncioCallbackDispatcher(loop)
except ImportError:
    loop = None
    dispatcher = td.QueuedCallbackDispatcher()

core = td.TelldusCore(callback_dispatcher=dispatcher)
core.register_raw_device_event(raw_event)

try:
    if loop:
        loop.run_forever()
    else:
        import time
        while True:
            core.callback_dispatcher.process_pending_callbacks()
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
