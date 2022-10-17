from flask import Flask, render_template
import functions

app = Flask(__name__)


@app.route("/")
def index():
    candidates = functions.get_candidates_all()
    render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    pass


@app.route("/candidate/<skill>")
def get_candidate_by_skills(skill):
    pass


@app.route("/search/<candidate_name>")
def get_candidate_by_skills(candidate_name):
    pass


app.run(debug=True)
