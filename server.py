from bottle import route, run, request, template
import ergoscore_learn
import os

@route("/pred")
def hello():
    return template("index.html", text="")

@route("/pred", method="POST")
def do_predict():
    own = request.forms.event
    pred = request.forms.pred
    input_min = int(request.forms.input_min)
    input_sec = int(request.forms.input_sec)
    input_minsec = int(request.forms.input_minsec)
    response_text = ergoscore_learn.predict(own,pred,input_min,input_sec,input_minsec)

    return template("index",text=response_text)
    
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
#run(host="localhost",port=8080,debug=True)