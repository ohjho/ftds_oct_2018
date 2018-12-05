
from base64 import b64encode

import googleapiclient.discovery
from oauth2client.client import GoogleCredentials

# Change this values to match your project
IMAGE_FILE = "road_sign.jpg"


CREDENTIALS_FILE = "gcvcredentials.json"

# Connect to the Google Cloud-ML Service
credentials = GoogleCredentials.from_stream(CREDENTIALS_FILE)
service = googleapiclient.discovery.build('vision', 'v1', credentials=credentials)

# Read file and convert it to a base64 encoding
with open(IMAGE_FILE, "rb") as f:
    image_data = f.read()
    encoded_image_data = b64encode(image_data).decode('UTF-8')

# Create the request object for the Google Vision API
batch_request = [{
    'image': {
        'content': encoded_image_data
    },
    'features': [
        {
            'type': 'TEXT_DETECTION'
        }
    ]
}]
request = service.images().annotate(body={'requests': batch_request})

# Send the request to Google
response = request.execute()

# Check for errors
if 'error' in response:
    raise RuntimeError(response['error'])

# Print the results
extracted_texts = response['responses'][0]['textAnnotations']

# Print the first piece of text found in the image
extracted_text = extracted_texts[0]
print(extracted_text['description'])

# Print the location where the text was detected
print(extracted_text['boundingPoly'])