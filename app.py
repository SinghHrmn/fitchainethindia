from flask import Flask
from openai import OpenAI

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def home():
    return 'Hey Hacker'

@app.route('/videos', methods=['POST'])
def add_metadata():
    # TODO: verify authentication
    # TODO: featch metadata
    # TODO: add extra metadata for videos
    # TODO: send back the unique id where the user needs to upload the video
    return f'Hey Hacker with {id}'

@app.route('/videos/<id>', methods=['PUT'])
def upload_video():
    # TODO: fetch videos data
    # mark the video as pending verification
    # verify metadata from video

    # Process the video using AI
    
    # Verify if the videos is of the user  <FACE verfication>
    # Verify what the video content is about

    # Verify if the videos lies in that category

    # yes Mark the videos as successful
    # no Mark the videos as failed
    return



@app.route('/videos/<id>', methods=['GET'])
def get_video(id):
    # Verify user identity
    # send back the video
    return 'Hey Hacker'

if __name__ == '__main__':
    app.run(debug=True)