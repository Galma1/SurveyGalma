from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def survey():
    HTML = """<!DOCTYPE html>
    <html>
    <head>
        <title>Private Primary School Survey - Khaunga</title>
    </head>
    <body>
        <h1>Welcome to the Questionnaire for the Upcoming Private Primary School in Khaunga</h1>
        <form action="/submit" method="post">
        
        <h3>Name of the School:</h3>
        <input type="text" name="school_name"><br><br>

        <h2>Viability of the School Business</h2>
        <p>1. Are you aware of the need for a private primary school in Khaunga?</p>
        <input type="radio" name="awareness" value="Yes"> Yes
        <input type="radio" name="awareness" value="No"> No<br><br>

        <p>2. Would you consider enrolling your child(ren) in a private primary school if one were available?</p>
        <input type="radio" name="enrollment" value="Yes"> Yes
        <input type="radio" name="enrollment" value="No"> No<br><br>

        <p>3. What factors would influence your decision to enroll your child(ren) in a private school?</p>
        <input type="checkbox" name="factors" value="Cost"> Cost
        <input type="checkbox" name="factors" value="Location"> Location
        <input type="checkbox" name="factors" value="Quality of Education"> Quality of Education
        <input type="checkbox" name="factors" value="School Facilities"> School Facilities
        <input type="checkbox" name="factors" value="Reputation"> Reputation
        <input type="checkbox" name="factors" value="Curriculum"> Curriculum<br><br>

        <h2>Location and Renovation</h2>
        <p>4. Do you think repurposing the former Qatar bar and restaurant is a suitable location for a school?</p>
        <input type="radio" name="location_suitable" value="Yes"> Yes
        <input type="radio" name="location_suitable" value="No"> No<br><br>
        <p>5. What renovations or improvements are necessary for the facility to become a functional school?</p>
        <textarea name="renovations_needed"></textarea><br><br>

        <h2>Grade Levels to Start With</h2>
        <p>6. Which grade levels should be offered initially?</p>
        <select name="initial_grade_levels">
            <option value="Playgroup">Playgroup</option>
            <option value="PP1">PP1</option>
            <option value="PP2">PP2</option>
            <option value="Grade 1-6">Grade 1-6</option>
        </select><br><br>
        <p>7. What factors should be considered when determining the initial grade levels to offer?</p>
        <textarea name="factors_for_grades"></textarea><br><br>

        <h2>Curriculum</h2>
        <p>8. Do you prefer a Kenyan CBC curriculum, an Islamic curriculum, or a combination of both?</p>
        <select name="curriculum_preference">
            <option value="Kenyan CBC">Kenyan CBC</option>
            <option value="Islamic">Islamic</option>
            <option value="Both">Combination of both</option>
        </select><br><br>
        <p>9. What benefits or challenges do you foresee with each curriculum option?</p>
        <textarea name="curriculum_challenges"></textarea><br><br>

        <h2>Religious Affiliation</h2>
        <p>10. Would you support attaching the school to the Khaunga mosque?</p>
        <input type="radio" name="religious_affiliation" value="Yes"> Yes
        <input type="radio" name="religious_affiliation" value="No"> No<br><br>
        <p>11. How do you think a religious affiliation would impact the school's reputation and enrollment?</p>
        <textarea name="religion_impact"></textarea><br><br>

        <h2>Differentiation from Public Schools</h2>
        <p>12. What improvements do you think the new school should have compared to public primary schools in the area?</p>
        <textarea name="improvements_vs_public"></textarea><br><br>
        <p>13. What specific aspects of quality education are lacking in existing primary schools in Khaunga?</p>
        <textarea name="lacking_aspects"></textarea><br><br>

        <h2>Leadership</h2>
        <p>14. What qualities are essential for effective school leadership?</p>
        <textarea name="leadership_qualities"></textarea><br><br>
        <p>15. Would you prefer a leadership structure similar to that of public schools or a different approach?</p>
        <input type="radio" name="leadership_structure" value="Similar"> Similar
        <input type="radio" name="leadership_structure" value="Different"> Different<br><br>

        <h2>Demographic Information</h2>
        <label>Age:</label>
        <input type="number" name="age"><br><br>
        <label>Gender:</label>
        <select name="gender">
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
        </select><br><br>
        <label>Occupation:</label>
        <input type="text" name="occupation"><br><br>
        <label>Education Level:</label>
        <input type="text" name="education_level"><br><br>
        <label>Relationship to Khaunga (resident, business owner, etc.):</label>
        <input type="text" name="relationship_to_khaunga"><br><br>

        <p>16. Any other thoughts, suggestions, or concerns regarding the establishment of a private primary school in Khaunga?</p>
        <textarea name="additional_comments"></textarea><br><br>

        <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """
    print(HTML)  # Debug: Print the HTML to be rendered
    return render_template_string(HTML)

@app.route('/submit', methods=['POST'])
def submit():
    response_data = request.form
    response_html = "<h1>Thank you for your participation!</h1>"
    response_html += "<h2>Submitted Data:</h2><ul>"
    for key, values in response_data.lists():  # Handle multiple values per key
        response_html += f"<li><strong>{key.replace('_', ' ').capitalize()}:</strong> {' '.join(values)}</li>"
    response_html += "</ul>"
    response_html += '<a href="/">Return to Survey</a>'
    return response_html

if __name__ == "__main__":
    app.run(debug=False)

