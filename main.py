from flask import Flask, render_template, url_for, request, jsonify
import zg2uni
import uni2zg
import win2uni
import uni2win

myapp=Flask(__name__)

@myapp.route("/")
def hello():
    return render_template("index.html")

@myapp.route("/convert", methods=["POST"])
def convert():
    myinput = request.form['myinput']
    myoutput = request.form['myoutput']
    source = request.form['source']
    output = "The Input is " + myinput +"\r\n" + "The Output is " +myoutput
    if myinput == "zawgyi" and myoutput == "unicode":
        output = zg2uni.convert(source)
    if myinput == "zawgyi" and myoutput == "winmyanmar":
        output = zg2uni.convert(uni2win.convert(source))
    if myinput == "unicode" and myoutput == "zawgyi":
        output = uni2zg.convert(source)
    if myinput == "unicode" and myoutput == "winmyanmar":
        output = uni2win.convert(source)
    if myinput == "winmyanmar" and myoutput == "zawgyi":
        output = uni2zg.convert(win2uni.convert(source))
    if myinput == "winmyanmar" and myoutput == "unicode":
        output = win2uni.convert(source)
    if myinput == myoutput:
        output = "Input is: " + myinput + "and Output is: " + \
                myoutput + ". There are both same.No conversion done!"
    return jsonify ({'output': output})

if __name__ == "__main__":
    myapp.run(debug=True)
