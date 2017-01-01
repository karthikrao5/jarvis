# makes api calls to google cloud API

import argparse
import base64
import json
import subprocess as sp

from googleapiclient import discovery
import httplib2 # make http calls in python with this
from oauth2client.client import GoogleCredentials

# api KEY: AIzaSyDCWSOvOgM5h3b4J03D2jCJ6cgsTGGN6c0

api_version = "v1beta1"

DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')
# print DISCOVERY_URL


# Application default credentials provided by env variable
# GOOGLE_APPLICATION_CREDENTIALS
def get_speech_service():
	credentials = GoogleCredentials.get_application_default().create_scoped(
		['https://www.googleapis.com/auth/cloud-platform'])
	http = httplib2.Http()
	credentials.authorize(http)
	return discovery.build('speech', api_version, http=http, discoveryServiceUrl=DISCOVERY_URL)


def main(speech_file):

	# file has to be 1 channel, flac, 44100 samplerate and
	# -sample_fmt s16

	with open(speech_file,'rb') as speech:
		# encode the readbinary file in base64
		speech_content = base64.b64encode(speech.read())

	service = get_speech_service()

	service_request = service.speech().syncrecognize(
		body={
			'config': {
				'encoding': 'FLAC',
				'sampleRate': 44100
			},
			'audio': {
				'content': speech_content.decode('UTF-8')
			}
		})

	response = service_request.execute()
	result = response['results'][0]
	transcript = result['alternatives'][0]['transcript']
	print (transcript)
	return transcript


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'speech_file', help='Full path of audio file to be recognized')
    args = parser.parse_args()
    main(args.speech_file)
    # [END run_application]
