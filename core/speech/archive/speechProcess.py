from googleapiclient import discovery
import httplib2 # make http calls in python with this
from oauth2client.client import GoogleCredentials


api_version = "v1beta1"

DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')

# Application default credentials provided by env variable
# GOOGLE_APPLICATION_CREDENTIALS
def get_speech_service():
	credentials = GoogleCredentials.get_application_default().create_scoped(
		['https://www.googleapis.com/auth/cloud-platform'])
	http = httplib2.Http()
	credentials.authorize(http)
	return discovery.build('speech', api_version, http=http, discoveryServiceUrl=DISCOVERY_URL)