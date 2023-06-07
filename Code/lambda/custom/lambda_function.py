"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""


from __future__ import print_function
import random
import wave


# --------------- Helper Functions   ------------------

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, content, speech_output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + speech_output + "</speak>"
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': content
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }



def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def handle_launch_request(session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title      = "Welcome"
    card_content    = "Welcome to Morse Code Messenger! what message would you like me to translate"                      \


    speech_output   = "Welcome to Morse Code Messenger! Say translate and the word or message you want me to translate? "                      \


    reprompt_text   = "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))



def handle_message_intent(intent_name, session, event):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    morsecodedictionary = { "a":"dit dah",
                            "b":"dah dit dit dit",
                            "c":"dah dit dah dit",
                            "d":"dah dit dit,",
                            "e":"dit",
                            "f":"dit dit dah dit",
                            "g":"dah dah dit",
                            "h":"dit dit dit dit",
                            "i":"dit dit",
                            "j":"dit dah dah dah",
                            "k":"dah dit dah",
                            "l":"dit dah dit dit",
                            "m":"dah dah",
                            "n":"dah dit",
                            "o":"dah dah dah",
                            "p":"dit dah dah dit",
                            "q":"dah dah dit dah",
                            "r":"dit dah dit",
                            "s":"dit dit dit",
                            "t":"dah",
                            "u":"dit dit dah",
                            "v":"dit dit dit dah",
                            "w":"dit dah dah",
                            "x":"dah dit dit dah",
                            "y":"dah dit dah dah",
                            "z":"dah dah dit dit",
                            "0":"dah dah dah dah dah",
                            "1":"dit dah dah dah dah",
                            "2":"dit dit dah dah dah",
                            "3":"dit dit dit dah dah",
                            "4":"dit dit dit dit dah",
                            "5":"dit dit dit dit dit",
                            "6":"dah dit dit dit dit",
                            "7":"dah dah dit dit dit",
                            "8":"dah dah dah dit dit",
                            "9":"dah dah dah dah dit",
                            ".":"dit dah dit dah dit dah",
                            ",":"dah dah dit dit dah dah",
                            ":":"dah dah dah dit dit dit",
                            "?":"dit dit dah dah dit dit",
                            "'":"dit dah dahdah dah dit",
                            "-":"dah dit dit dit dit dah",
                            "/":"dah dit dit dah dit",
                            "(":"dah dit dah dah dit",
                            ")":"dah dit dah dah dit dah",
                            '"':"dit dah dit dit dah dit",
                            "@":"dit dah dah dit dah dit",
                            "=":"dah dit dit dit dah",
                            " ":"<break time='500ms'/>",}


    originalmessage = event['request']['intent']['slots']['message']['value']
    lowercasemessage = originalmessage.lower()
    messageinmorse = []
    count = 0
    if   5 >= len(originalmessage): 
        while count < len(originalmessage):
            letter = lowercasemessage[count]
            audioletter = '<audio src="https://s3.amazonaws.com/morsecode-audio/' + letter + '.mp3" />'
            messageinmorse.append(audioletter)
            count += 1
    while count < len(originalmessage):
        letter = lowercasemessage[count]
        audioletter = morsecodedictionary.get(letter)
        messageinmorse.append(audioletter)
        count += 1

    """
    infiles = messageinmorse
    outfile = "message.wav"
    data = []
    for infile in infiles:
        w=wave.open(infile,'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    output.writeframes(data[0][1])
    output.writeframes(data[1][1])
    output.close()
    """

    finalmessage = " <break time='100ms'/> ".join([str(x) for x in messageinmorse])

    print(originalmessage)
    print(len(originalmessage))

    session_attributes = {}
    card_title      = "Message in Morse Code"
    card_content    = originalmessage
    
    speech_output   = finalmessage
    
    reprompt_text   =  "Go ahead and ask me, if you need help just ask! "                                  \

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

 
def handle_help_intent(intent_name, session):

    session_attributes = {}
    card_title      = "Help"
    card_content    = "I can say a message in Morse Code for you, till me what you would like me to translate."

    speech_output   = "I can say a message in Morse Code for you, till me what you would like me to translate. To help, say translate and then the word"

    reprompt_text   = "Say ' Translate Hello World' so I can translate that for you! "

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def handle_end_intent():

    session_attributes = {}
    card_title      = "Goodbye"
    card_content    = "Goodbye, come for another translation"

    speech_output   = "Goodbye, come for another translation"

    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return handle_launch_request(session)


def on_intent(intent_request, session, event):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "messageIntent" :
        return handle_message_intent(intent_name, session, event)
    elif intent_name == "AMAZON.HelpIntent" or intent_name == "AMAZON.FallbackIntent" :
        return handle_help_intent(intent_name,session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_end_intent()
    else:
        print("what the what is " + intent_name)
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] !=
             "amzn1.ask.skill.9ff6c853-b197-482a-8700-e2cce44372b0"):
         raise ValueError("Invalid Application ID")
    

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'], event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
