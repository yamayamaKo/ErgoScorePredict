from bottle import route, run, request, template, static_file, url
import ergoscore_learn
import os

#元のスコアを表示するstringを返す関数
def make_response(input_min,input_sec,input_minsec,event):
    if(event=="twenty"):
        return str(input_min)

    response = ""
    if(input_sec<10):
        response += str(input_min) + ":0" + str(input_sec) + "." + str(input_minsec)
    else:
        response += str(input_min) + ":" + str(input_sec) + "." + str(input_minsec)
    return response
    
@route("/static/<filepath:path>",name="static_file")
def static(filepath):
    return static_file(filepath,root="./static")

@route("/pred")
def hello():
    return template("index.html", input_text="", text="")

@route("/pred", method="POST")
def do_predict():
    own = request.forms.event
    pred = request.forms.pred
    input_min = int(request.forms.input_min)
    input_sec = int(request.forms.input_sec)
    input_minsec = int(request.forms.input_minsec)
    input_text = make_response(input_min,input_sec,input_minsec,own)
    response_text = ergoscore_learn.predict(own,pred,input_min,input_sec,input_minsec)

    return template("index",input_text=input_text,text=response_text)

#サーバを立ち上げる    
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
#run(host="localhost",port=8080,debug=True)