from flask import Flask , render_template , jsonify
app = Flask(__name__)

JOBS = [
    {
        "title": "Software Engineer",
        "company": "Google",
        "location": "Mountain View, CA",
        "salary": "$150,000",
    },
    {
        "title": "Software Developer",
        "company": "Google",
        "location": "Mountain View, CA",
        "salary": "$150,000",
    },
    {
        "title": "Software Tester",
        "company": "Google",
        "location": "Mountain View, CA",
        "salary": "$150,000",
    },
    {
        "title": "Frontend Developer",
        "company": "Google",
        "location": "Mountain View, CA",
        "salary": "$150,000",
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, title="Home Page")

@app.route("/api/jobs")
def jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5000)