import logging
from AlexaPy.AlexaClass import AlexaRequest
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    Alexa = AlexaRequest()
    msg = Alexa.handler(req)

    r = '''
    {
          "version": "1.0",
          "sessionAttributes": {
            "supportedHoroscopePeriods": {
              "daily": true,
              "weekly": false,
              "monthly": false
            }
          },
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "Uhuuuu so far so good!"
            },
            "card": {
              "type": "Simple",
              "title": "Television",
              "content": "Today will provide you a new learning opportunity.  Stick with it and the possibilities will be endless."
            },
            "reprompt": {
              "outputSpeech": {
                "type": "PlainText",
                "text": "Can I help you with anything else?"
              }
            },
            "shouldEndSession": false
          }
    }
    '''
    req_body = req.get_json()

    print(req_body)
    print(req.headers)

    return func.HttpResponse(
            msg
    )

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
