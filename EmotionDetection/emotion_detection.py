import requests                 # Import the requests library to handle HTTP requests
import json
def emotion_detector(text_to_analyse):
    # URL of emotion
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }     
    # Custom header specifying the model ID for the emotion analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json = myobj, headers=header) 
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting emotion with the highest score from the response
    emotion_score = formatted_response['emotionPredictions'][0]['emotion']
    # Find dominant emotion, which is the emotion with the highest score
    dominant_emotion = max(emotion_score, key=emotion_score.get)
    
    # Construct the output dictionary
    output = emotion_score.copy()                    # Copy the original emotion scores
    output['dominat_emotion'] = dominant_emotion      # Add the dominant emotion = 
    return output

