from flask import Flask, request, render_template
import prediction

app = Flask(__name__)

@app.route('/')
def helloIndex():
	return render_template("index.html")

@app.route('/sub',methods=['POST'])
def submit():
	if request.method == "POST":
		v1=request.form["v1"]
		v2=request.form["v2"]
		v3=request.form["v3"]
		print(v1)
		result = prediction.get_prediction([v1,v2,v3])
		res = ""
		if result[0] == 0:
			res = "Not Fraud"
		else:
			res = "Fraud"

		
	return render_template("index.html",res=res)

if __name__=="__main__":
	app.run(debug=True)
