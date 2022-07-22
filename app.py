from flask import Flask, render_template

app = Flask(__name__)

headings = ('Name', 'Role', 'Salary', 'checkbox')
data = (
    ('Rolf', 'SOftware Engineer !!', '42K'),
    ('Kovak', 'Relaxer', '420K'),
    ('Vako', 'Feeling good expert', '42M'),
)

@app.route("/")
def table():
    return render_template('tables.html', headings=headings, data=data)
    # return 'Now is working!'

# to retrieve checked box
# if request.method == "POST":
    # selected_contacts = request.form.getlist("contacts")

#https://coderwall.com/p/pkthoa/read-checkbox-in-flask