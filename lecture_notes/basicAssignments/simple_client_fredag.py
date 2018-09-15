import requests

# Mapper http
# Sender request blok til denne server
# Får et response objekt tilbage
response = requests.get('http://10.50.137.116:5000')

# Tekst besked, der kommer tilbage fra serveren.
response.text

# response content er en sequence af bytes.
response.content

response_two = req
