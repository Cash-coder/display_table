from flask import Flask, render_template

app = Flask(__name__)

headings = ('Name', 'Role', 'Salary', 'checkbox', 'Picture')
data = (
    ('Rolf', 'SOftware Engineer !!', '42K', 'http://1tfu7b1m4mm33k2ocvwvp010.wpengine.netdna-cdn.com/wp-content/uploads/2015/11/What-is-content-intelligence.jpg'),
    ('Kovak', 'Relaxer', '420K', 'https://thelabrynthoflife.files.wordpress.com/2014/06/power-of-intelligence.jpg'),
    ('Vako', 'Feeling good expert', '42M', 'https://ecvo8ubt6cq.exactdn.com/wp-content/uploads/2021/07/f97acb41-5694-4b4b-94b3-af590226f170.jpg'),
)

@app.route("/")
def table():
    return render_template('tables.html', headings=headings, data=data)
    # return 'Now is working!'

# to retrieve checked box
# if request.method == "POST":
    # selected_contacts = request.form.getlist("contacts")

#https://coderwall.com/p/pkthoa/read-checkbox-in-flask