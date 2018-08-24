import flask
from forms.post_from_sheets import main
app = flask.Flask(__name__)

@app.route("/")
def index():
    #do whatevr here...
    main()