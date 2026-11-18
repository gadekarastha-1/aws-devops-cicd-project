from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS DevOps CI/CD Project</h1>
    <h2>Welcome!</h2>
    <p>My first automated deployment project.</p>
    <p>Application Status: Running Successfully</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    