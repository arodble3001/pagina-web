from flask import Flask, render_template, request
app= Flask ("Plantilla")

@app.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)