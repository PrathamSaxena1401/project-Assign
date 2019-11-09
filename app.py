from flask import Flask,render_template,request,session
import mysql.connector


app = Flask(__name__)
app.secret_key="admin"

@app.route('/')
def hello_world():
    return render_template('login.html')
@app.route('/teacherreg')
def teacherreg():
    return render_template('teacherreg.html')
@app.route('/studentreg')
def studentreg():
    return render_template('studentreg.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/reg',methods=['POST'])
def regisstudents():

    conn=mysql.connector.connect(host='localhost', db='data',user='root',password='')
    fln=str(request.form["fln"])
    bch=str(request.form["bch"])
    pn=str(request.form["pn"])
    yr=str(request.form["yr"])
    sm=str(request.form["sm"])
    em=str(request.form["em"])
    pwd=str(request.form["pwd"])
    cur=conn.cursor()
    cur.execute("insert into students values('""','"+fln+"','"+bch+"','"+pn+"','"+yr+"','"+sm+"','"+em+"','"+pwd+"','false') ")
    conn.commit()
    return render_template('success.html')

@app.route('/regg',methods=['POST'])
def registeachers():

    conn=mysql.connector.connect(host='localhost', db='data',user='root',password='')
    fln=str(request.form["fln"])
    dj=str(request.form["dj"])
    cn=str(request.form["cn"])
    emm=str(request.form["em"])
    pwdd=str(request.form["pwd"])
    cur=conn.cursor()
    cur.execute("insert into teachers values('""','"+fln+"','"+dj+"','"+cn+"','"+emm+"','"+pwdd+"','false') ")
    conn.commit()
    return render_template('success.html')

@app.route('/login',methods=['POST'])
def logcode():
    emmm=str(request.form["em"])
    pwww=str(request.form["pwd"])
    conn=mysql.connector.connect(host='localhost', db='data', user='root', password='')
    cur=conn.cursor()
    cur.execute("select * from administrator where email='" +emmm+ "' and password='" +pwww+ "'")
    ar = cur.fetchone()
    session["user"]=emmm



    if (ar[2] == "admin"):
        return render_template('welcome_a.html', user=ar)
    elif (ar[2] == "teacher"):
        return render_template('welcome_t.html', user=ar)
    elif (ar[2] == "student"):
        return render_template('welcome_s.html', user=ar)

@app.route('/tslist')
def tslist():
    conn = mysql.connector.connect(host='localhost', db='data', user='root', password='')
    cur = conn.cursor()
    cur.execute("select * from teachers")
    ar = cur.fetchall()
    return render_template('teacherlist.html', data=ar)

@app.route('/sslist')
def sslist():
    conn = mysql.connector.connect(host='localhost', db='data', user='root', password='')
    cur = conn.cursor()
    cur.execute("select * from students")
    ar = cur.fetchall()
    return render_template('students.html', data=ar)


@app.route('/upd')
def accept():
    conn = mysql.connector.connect(host='localhost', db='data', user='root', password='')
    cur = conn.cursor()
    id = request.args.get('id')
    cur.execute("update teachers set status='true' where id=" + id)
    conn.commit()
    cur.execute("select * from teachers where id=" + id)
    ar1 = cur.fetchone()
    emmmm = str(ar1[4])
    pwddd = str(ar1[5])
    cur.execute("insert into administrator values('" + emmmm + "','" + pwddd + "','teacher')")
    conn.commit()

    cur.execute("select * from teachers")
    ar = cur.fetchall()
    return render_template('teacherlist.html')

@app.route('/upds')
def accepts():
    conn = mysql.connector.connect(host='localhost', db='data', user='root', password='')
    cur = conn.cursor()
    id = request.args.get('id')
    cur.execute("update students set status='true' where id=" + id)
    conn.commit()
    cur.execute("select * from students where id=" + id)
    ar1 = cur.fetchone()
    emmmmm = str(ar1[6])
    pwdddd = str(ar1[7])
    cur.execute("insert into administrator values('" + emmmmm + "','" + pwdddd + "','student')")
    conn.commit()

    cur.execute("select * from students")
    ar = cur.fetchall()
    return render_template('students.html',user=ar)

@app.route('/upddd')
def reject():
    conn = mysql.connector.connect(host='localhost', db='data', user='root', password='')
    cur = conn.cursor()
    id = request.args.get('id')
    cur.execute("update teachers set status='false' where id=" + id)
    conn.commit()
    cur.execute("select * from teachers")
    ar = cur.fetchall()
    return render_template('teacherlist.html')

@app.route('/updd')
def rejects():
    conn = mysql.connector.connect(host='localhost', db='data', user='root', password='')
    cur = conn.cursor()
    id = request.args.get('id')
    cur.execute("update students set status='true' where id=" + id)
    conn.commit()
    cur.execute("select * from students")
    ar = cur.fetchall()
    return render_template('students.html')

@app.route('/im' ,methods=['POST'])
def posts():
    conn= mysql.connector.connect(host='localhost', db='data', user='root', password='')
    bchh= str(request.form["bch"])
    img= str(request.form["image"])
    tx= str(request.form["text"])
    yrr= str(request.form["year"])
    semm= str(request.form["sem"])
    sbc= str(request.form["sbc"])
    dsm= str(request.form["dsm"])
    cur = conn.cursor()
    cur.execute(
        "insert into assignment values('""','""','" +bchh+ "','" +yrr+ "','" +semm+ "','" +sbc+ "','"+img+"','"+tx+"','"+dsm+"','""') ")
    conn.commit()
    return render_template('successs.html')
@app.route('/posts')
def ap():
     conn= mysql.connector.connect(host='localhost', db='data', user='root', password='')
     cur= conn.cursor()
     cur.execute("select * from assignment")
     ar= cur.fetchall()
     return render_template('welcome_s.html', data=ar)




if __name__ == '__main__':
     app.run()




