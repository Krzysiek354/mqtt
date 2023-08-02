import asyncio
from hbmqtt.broker import Broker

config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '192.168.2.10:1883',
        },
    },
    'sys_interval': 10,
    'auth': {
        'plugins': ['auth.anonymous'],
        'allow-anonymous': True,
    },
    'topic-check': {
        'enabled': False
    }
}

broker = Broker(config)

async def startBroker():
    await broker.start()

if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(startBroker())
    except Exception as e:
        print(f"Failed to start broker: {e}")
