import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from twilio.rest import Client

# Replace these values with your Twilio account SID, auth token, and WhatsApp API key
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
api_key = 'your_api_key'

# Replace these values with the phone number you want to send the message from and the WhatsApp phone number you want to send the message to
from_number = 'twilio number +10000000'
to_number = 'whatsup number +100000000'

# Create a Twilio client
client = Client(account_sid, auth_token)

class FileCreatedEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        message = client.messages.create(
            from_=from_number,
            body='A file was created: ' + event.src_path,
            to=to_number,
            api_key=api_key
        )

event_handler = FileCreatedEventHandler()
observer = Observer()
observer.schedule(event_handler, '/path/to/directory', recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
