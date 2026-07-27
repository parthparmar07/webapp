from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Azure App Service</title>
        <style>
            body{
                background:#111827;
                color:white;
                font-family:Arial;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                text-align:center;
            }
            h1{color:#38bdf8;}
        </style>
    </head>
    <body>
        <div>
            <h1>Azure App Service</h1>
            <h2>Experiment 2 - CI/CD</h2>
            <p>Deployed using GitHub Actions</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()