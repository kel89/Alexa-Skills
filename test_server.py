from flask import Flask

app = Flask(__name__)

@app.route("/")
def base():
	return "Test passed!"

if __name__ == "__main__":
	app.run(port=5000)
