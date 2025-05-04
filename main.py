from talkops import Extension, Image, Video
import asyncio
import random

def enable_alarm():
    extension.enable_alarm()
    return 'Done.'

def receive_random_dice():
    return str(random.randint(1, 6))

async def receive_random_dice_asynchronously():
    await asyncio.sleep(2)
    return str(random.randint(1, 6))

def receive_random_dice_message():
    extension.send_message(str(random.randint(1, 6)))
    return 'Done.'

def receive_random_dice_notification():
    extension.send_notification(str(random.randint(1, 6)))
    return 'Done.'

def receive_random_image():
    extension.send_medias([
        Image('https://picsum.photos/640/480')
    ])
    return 'Done.'

def receive_random_video():
    extension.send_medias([
        Video(random.choice([
          'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4',
          'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4',
          'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4',
          'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4'
        ]))
    ])
    return 'Done.'

extension = (
    Extension()
    .set_name('Playground Python')
    .set_icon('https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-512.png')
    .set_category('utility')
    .set_demo(True)
    .set_features([
        'Enable alarm',
        'Receive random dice',
        'Receive random dice asynchronously',
        'Receive random dice as message',
        'Receive random dice as notification',
        'Receive random image',
        'Receive random video'
    ])
    .set_function_schemas([
        {
            "name": "enable_alarm",
            "description": "Enable alarm."
        },
        {
            "name": "receive_random_dice",
            "description": "Receive random dice.",
        },
        {
            "name": "receive_random_dice_asynchronously",
            "description": "Receive random dice asynchronously.",
        },
        {
            "name": "receive_random_dice_message",
            "description": "Receive random dice as message.",
        },
        {
            "name": "receive_random_dice_notification",
            "description": "Receive random dice as notification.",
        },
        {
            "name": "receive_random_image",
            "description": "Receive a random image."
        },
        {
            "name": "receive_random_video",
            "description": "Receive a random video."
        }
    ])
    .set_functions([
        enable_alarm,
        receive_random_dice,
        receive_random_dice_asynchronously,
        receive_random_dice_message,
        receive_random_dice_notification,
        receive_random_image,
        receive_random_video,
    ])
    .start()
)

print('test')
