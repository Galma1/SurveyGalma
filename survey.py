from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
load_dotenv()

load_dotenv()  # Load environment variables from a .env file

app = Flask(__name__)

# Configure SQLite database from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///survey.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the SurveyResponse model
class SurveyResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(100))
    awareness = db.Column(db.String(50))
    enrollment = db.Column(db.String(50))
    factors = db.Column(db.String(200))
    location_suitable = db.Column(db.String(50))
    renovations_needed = db.Column(db.Text)
    initial_grade_levels = db.Column(db.String(50))
    factors_for_grades = db.Column(db.Text)
    curriculum_preference = db.Column(db.String(50))
    curriculum_challenges = db.Column(db.Text)
    religious_affiliation = db.Column(db.String(50))
    religion_impact = db.Column(db.Text)
    improvements_vs_public = db.Column(db.Text)
    lacking_aspects = db.Column(db.Text)
    leadership_qualities = db.Column(db.Text)
    leadership_structure = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    occupation = db.Column(db.String(100))
    education_level = db.Column(db.String(100))
    relationship_to_khaunga = db.Column(db.String(100))
    additional_comments = db.Column(db.Text)

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Create a new survey response
    survey_response = SurveyResponse(
        school_name=request.form['school_name'],
        awareness=request.form['awareness'],
        enrollment=request.form['enrollment'],
        factors=",".join(request.form.getlist('factors')),  # Handle multiple checkboxes
        location_suitable=request.form['location_suitable'],
        renovations_needed=request.form['renovations_needed'],
        initial_grade_levels=request.form['initial_grade_levels'],
        factors_for_grades=request.form['factors_for_grades'],
        curriculum_preference=request.form['curriculum_preference'],
        curriculum_challenges=request.form['curriculum_challenges'],
        religious_affiliation=request.form['religious_affiliation'],
        religion_impact=request.form['religion_impact'],
        improvements_vs_public=request.form['improvements_vs_public'],
        lacking_aspects=request.form['lacking_aspects'],
        leadership_qualities=request.form['leadership_qualities'],
        leadership_structure=request.form['leadership_structure'],
        age=request.form['age'],
        gender=request.form['gender'],
        occupation=request.form['occupation'],
        education_level=request.form['education_level'],
        relationship_to_khaunga=request.form['relationship_to_khaunga'],
        additional_comments=request.form['additional_comments']
    )

    # Add and commit the response to the database
    db.session.add(survey_response)
    db.session.commit()

    # Display the submitted data
    response_html = "<h1>Thank you for your participation!</h1>"
    response_html += "<h2>Submitted Data:</h2><ul>"
    for key, value in request.form.items():
        response_html += f"<li><strong>{key.replace('_', ' ').capitalize()}:</strong> {value}</li>"
    response_html += "</ul>"
    response_html += '<a href="/">Return to Survey</a>'
    return response_html

if __name__ == "__main__":
    app.run(debug=True)
