from talkops import Extension, Image, Video
import random

def enable_alarm():
    extension.enable_alarm()
    return 'Done.'

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
        'Send a message',
        'Send a message',
        'Send a notification'
    ])
    .set_function_schemas([
        {
            "name": "enable_alarm",
            "description": "Enable alarm."
        },
        {
            "name": "receive_random_dice_message",
            "description": "Receive random dice result as message.",
        },
        {
            "name": "receive_random_dice_notification",
            "description": "Receive random dice result as notification.",
        },
        {
            "name": "receive_random_image",
            "description": "Receive random image."
        },
        {
            "name": "receive_random_video",
            "description": "Receive random video."
        }
    ])
    .set_functions([
        enable_alarm,
        receive_random_dice_message,
        receive_random_dice_notification,
        receive_random_image,
        receive_random_video,
    ])
    .start()
)
