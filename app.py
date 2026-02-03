from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        her_name="Nidhi Medikonda",
        message="You are the reason I smile at my phone like a goof."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

