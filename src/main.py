from talkops import Extension, Image, Parameter, Video
import asyncio
import random

extension = (
  Extension()
  .set_name('Python Playground')
  .set_icon('https://talkops.app/images/extensions/playground-python.png')
  .set_category('utility')
  .set_demo(True)
  .set_features([
      'Enable the alarm',
      'Receive a random dice',
      'Receive a random dice asynchronously',
      'Receive a random dice as message',
      'Receive a random dice as notification',
      'Receive a random image',
      'Receive a random video'
  ])
)

color = (
    Parameter('COLOR')
    .set_description('The color used for test.')
    .set_type('select')
    .set_default_value('blue')
    .set_available_values(['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
)

email = (
    Parameter('EMAIL')
    .set_description('The email used for test.')
    .set_type('email')
    .set_default_value('john.doe@example.com')
)

def enable_alarm():
    extension.enable_alarm()
    return 'Done.'

def receive_random_dice():
    return str(random.randint(1, 6))

async def receive_random_dice_asynchronously():
    await asyncio.sleep(10)
    return str(random.randint(1, 6))

def receive_random_dice_message():
    extension.send_message(str(random.randint(1, 6)))
    return 'Done.'

def receive_random_dice_notification():
    extension.send_notification(str(random.randint(1, 6)))
    return 'Done.'

def receive_random_image():
    extension.send_medias([
        Image(f'https://picsum.photos/seed/{random.randint(1, 100)}/640/480')
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

def on_boot(language):
    print("on_boot")
    print(language)
    print(color.value)
    print(email.value)

def on_session(language):
    print("on_session")
    print(language)
    print(color.value)
    print(email.value)

def on_enable(language):
    print("on_enable")
    print(language)
    print(color.value)
    print(email.value)

def on_disable(language):
    print("on_disable")
    print(language)
    print(color.value)
    print(email.value)

def on_language(language):
    print("on_language")
    print(language)
    print(color.value)
    print(email.value)

(
  extension
  .set_parameters([color, email])
  .set_function_schemas([
      {
          "name": "enable_alarm",
          "description": "Enable the alarm."
      },
      {
          "name": "receive_random_dice",
          "description": "Receive a random dice.",
      },
      {
          "name": "receive_random_dice_asynchronously",
          "description": "Receive a random dice asynchronously.",
      },
      {
          "name": "receive_random_dice_message",
          "description": "Receive a random dice as message.",
      },
      {
          "name": "receive_random_dice_notification",
          "description": "Receive a random dice as notification.",
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
  .on('enable', on_enable)
  .on('boot', on_boot)
  .on('disable', on_disable)
  .on('language', on_language)
  .on('session', on_session)
  .start()
)
