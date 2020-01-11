import requests

# This function will pass your numbers to the machine learning model
# and return the top result with the highest confidence
def classify(key, data):
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    response = requests.post(url, json={ "data" : data })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
