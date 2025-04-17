import weasyprint 
from flask import Flask, render_template, request, send_file
import os
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Extract the data from the form
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "address": request.form["address"],
            "website": request.form["website"],
            "dob": request.form["dob"],
            "gender": request.form["gender"],
            "summary": request.form["summary"],
            "experience": request.form["experience"],
            "education": request.form["education"],
            "skills": request.form["skills"],
            "languages": request.form["languages"],
            "certifications": request.form["certifications"]
        }
        
        # Render the HTML for the CV output page
        html_content = render_template("cv_output.html", data=data)
        
        # Convert HTML to PDF using WeasyPrint
        pdf_file = weasyprint.HTML(string=html_content).write_pdf()

        # Save the PDF in memory
        pdf_io = BytesIO(pdf_file)
        pdf_io.seek(0)
        
        return send_file(pdf_io, as_attachment=True, download_name="cv_output.pdf", mimetype="application/pdf")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
