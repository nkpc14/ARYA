# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 23:06:55 2018

@author: Nitish Kumar
"""

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio,key="21cb10e82de52e42df5eab8cc9083dc9298a8f10"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = {
  "type": "service_account",
  "project_id": "arya---artificia-1535617034767",
  "private_key_id": "21cb10e82de52e42df5eab8cc9083dc9298a8f10",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQChaA7pkvptDrmN\nmSrQDB4bX6zsNvgi0IzwBy/kHILCQxrq29MUvFFGoNKUfUSw9nDB0U2txjPSTTFF\nSGNGns7D5AGKQnIAQGmzwqFt2oxEBZJZubQJ+QMlquxpRtdxDhd/vR1bmpLiuUS7\nzuecuhIKmvFRJn5Y8S2X+ldAfhhghOq1G1UEcHC3WtQkkKnL+cLtbFs/sPM679zD\nC23hkSfEwQ1cqQ/XDI+9OrggmItvMUL9eXc3DiF5F8NnjV5VeMsy8CG+xyurf/It\ne8CYEW9crEQnZTfAETbjaHsAFCDVtWm9K6sZQmWWzDOMWjxjFdeNCRuoa4tv7Hnd\nmYnaTc+rAgMBAAECggEAAWjzzGWMy3wX8d03KwcYEjwlOhEG3OL+gDBH4lG/cKv+\nZbPS5bj5askH3eU0PumANak66Pw0wq8K8aR+vYSwoLRysP8AmPD3G2tlVpzUodl8\nnE0LfhTPSrpyAz9rrWCmouaHhZ/VjaZ5q7xUeKGFe9M7rW5NJ0DAGbZFodoYI2uy\nRepekddlNh4VFVhQhOvxyEV3xxKSceA/yc90Zn4B8E0XACiUpZpFWeaMecrsbnb+\n3HE6RLTAgPFT2g4q8qdD+nIkeSSs1mYdYLG3V9wdM6gj9tSN3KkR2ilF6mZgkzXB\nbJ5pmlXFLMEP4e/Bsxji9K3bKj9Lx3poFHt4PPsg3QKBgQDOTBtwTZE6yam3LhjL\ncFJD6yfYyjCkVU3AFxyFOZL3UDagNC0LPlsMnag6N7N9WXbN2XQfpcBVQSY8769o\nBuplYDI7j+ey41SJuH1l4AqO9uUEU4WUSszJ9cXwQBx2Z3MHsQbg5pUyDDtpAOu1\n2a35BRLaJvG8Ac2JXw8t7wbc5QKBgQDISzMZm9WStXEURo5JkjlnNnlAtUn4ZPzP\n9O98PkfHO/ZH7sOmnE61zKskGedqBsfzRJ+9/0vqUJzhS12gFavZ/Z2EIH9XNjFS\nLzHC356pDU+UWq9CU/v6zH0rbVXN8Of/Dq0TMru6y/gGPcl2R9upEOCjY09Rbnwl\niFsVvJvBTwKBgAi3XH1tOZKjTKFpuDB4SXGHMQLO4ClBVWylTVYvrY73e6dfLPwJ\noW0yCBaVnebQ7d0ar/ZaWXsAqq3ubpnVmPe5jcXIecCsLDk5a0rvoWKS+fAp2z39\nvxNVaAyTmOBD1K9hgmnkNC+OJsB0AoGHdftMhJRlCtent9hzBMArFj4lAoGAErKi\ndJONnoJ9qezkP438+dul+hpya1PSHf+5k5mkzb6VQSXS8ezJlEMk/tvENKupYtZX\nKz938MnRu15zwQwE3PbGC52VBakzdX6eYJjLkPCDK1BD6Cc68LDCRpmQVwdUQQU3\ntwEXcVq1Lq/57KbMpL3EmrwcnXd483AFQMQ4rhUCgYBuJG/nsGs9takOOV9sgO3g\nKC0fHN6SjXlJ0JdTtCJMmnnUFAX+6Tv1jp6mcNMsRrkRO+rLefkxc+ymCLR+jmlB\ntYyTI5K4NfzNBU8NOmcGaOYumJJzFFwLS5MX8jOHOdAGebotf3ZNIJpgLo0aO4Je\nAyJRaBOigU+C0DKSqlFPXw==\n-----END PRIVATE KEY-----\n",
  "client_email": "starting-account-obawb7lc0rwd@arya---artificia-1535617034767.iam.gserviceaccount.com",
  "client_id": "117085597049154295494",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/starting-account-obawb7lc0rwd%40arya---artificia-1535617034767.iam.gserviceaccount.com"
}

try:
    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))
