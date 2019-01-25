app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launch():
    speech_text = 'Welcome to Felix. Your personal Assistant and friend. How can I help you?'
    #os.system("python Code.py")
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('ObjectIntent')
def Object_Intent():
    os.system("python camera_image.py")
    f=open('scene.txt','r')
    message=f.read()
    return statement(message)
    f.close()

@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
