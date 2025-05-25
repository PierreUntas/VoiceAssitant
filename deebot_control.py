# deebot_control.py

import aiohttp
import asyncio
import time
import logging
from threading import Thread
from config import DEEBOT_EMAIL, DEEBOT_PASSWORD, DEEBOT_COUNTRY

from deebot_client.api_client import ApiClient
from deebot_client.authentication import Authenticator, create_rest_config
from deebot_client.commands.json.clean import Clean, CleanAction
from deebot_client.commands.json.charge import Charge
from deebot_client.mqtt_client import MqttClient, create_mqtt_config
from deebot_client.device import Device
from deebot_client.util import md5

def launch_deebot_cleaning():
    def _main():
        async def main():
            device_id = md5(str(time.time()))
            password_hash = md5(DEEBOT_PASSWORD)
            async with aiohttp.ClientSession() as session:
                logging.basicConfig(level=logging.INFO)
                rest_config = create_rest_config(session, device_id=device_id, alpha_2_country=DEEBOT_COUNTRY)
                authenticator = Authenticator(rest_config, DEEBOT_EMAIL, password_hash)
                api_client = ApiClient(authenticator)
                devices_ = await api_client.get_devices()
                device_info = devices_.mqtt[0]
                bot = Device(device_info, authenticator)
                mqtt_config = create_mqtt_config(device_id=device_id, country=DEEBOT_COUNTRY)
                mqtt = MqttClient(mqtt_config, authenticator)
                await bot.initialize(mqtt)
                await bot.execute_command(Clean(CleanAction.START))
                await mqtt.disconnect()
        asyncio.run(main())
    Thread(target=_main).start()

def send_deebot_to_base():
    def _main():
        async def main():
            device_id = md5(str(time.time()))
            password_hash = md5(DEEBOT_PASSWORD)
            async with aiohttp.ClientSession() as session:
                logging.basicConfig(level=logging.INFO)
                rest_config = create_rest_config(session, device_id=device_id, alpha_2_country=DEEBOT_COUNTRY)
                authenticator = Authenticator(rest_config, DEEBOT_EMAIL, password_hash)
                api_client = ApiClient(authenticator)
                devices_ = await api_client.get_devices()
                device_info = devices_.mqtt[0]
                bot = Device(device_info, authenticator)
                mqtt_config = create_mqtt_config(device_id=device_id, country=DEEBOT_COUNTRY)
                mqtt = MqttClient(mqtt_config, authenticator)
                await bot.initialize(mqtt)
                await bot.execute_command(Charge())
                await mqtt.disconnect()
        asyncio.run(main())
    Thread(target=_main).start()
