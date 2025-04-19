from flask import Flask, render_template, request, send_file
import weasyprint
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
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
        html_content = render_template("cv_output.html", data=data)
        pdf = weasyprint.HTML(string=html_content).write_pdf()

        pdf_io = BytesIO(pdf)
        pdf_io.seek(0)

        return send_file(pdf_io, as_attachment=True, download_name="cv_output.pdf", mimetype="application/pdf")
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
