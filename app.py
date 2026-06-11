from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CI/CD Pipeline Successful</h1>
    <h3>GitHub -> Docker Hub -> AWS EC2</h3>
    <p>Developer: Saurabh Chaudhary</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
