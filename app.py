from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "pertemuan4"

# Konfigurasi Koneksi Database MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'database_new'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('mahasiswa'))
    return render_template('login.html')


@app.route('/mahasiswa')
def mahasiswa():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM mahasiswa ''')
    mahasiswa = cursor.fetchall()
    cursor.close()

    return render_template('mahasiswa.html', mahasiswa=mahasiswa)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/mahasiswa/tambah', methods=['GET', 'POST'])
def tambahmahasiswa():
    if request.method == 'GET':
        return render_template('mahasiswa/add.html')
    else:
        nama = request.form['nama']
        npm = request.form['npm']
        jurusan = request.form['jurusan']

        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO mahasiswa(nama,npm,jurusan) VALUES(%s,%s,%s) ''', (nama, npm, jurusan))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('mahasiswa'))


@app.route('/mahasiswa/edit/<int:npm>', methods=['GET', 'POST'])
def editmahasiswa(npm):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute('''
        SELECT *
        FROM mahasiswa
        WHERE npm = %s
        ''', (npm, ))
        mahasiswa = cursor.fetchone()
        cursor.close()

        return render_template('mahasiswa/edit.html', mahasiswa=mahasiswa)

    else:
        nama = request.form['nama']
        jurusan = request.form['jurusan']

        cursor = mysql.connection.cursor()
        cursor.execute('''
        UPDATE mahasiswa
        SET
            nama = %s,
            jurusan = %s
        WHERE
            npm = %s
        ''', (nama, jurusan, npm))

        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('mahasiswa'))
    
@app.route('/mahasiswa/delete/<int:npm>', methods=['GET'])
def deletemahasiswa(npm) :
    if request.method == 'GET' :
        cursor = mysql.connection.cursor()
        cursor.execute(''' 
        DELETE
        FROM mahasiswa
        WHERE npm=%s
        ''', (npm, ))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('mahasiswa'))
   

if __name__ == '__main__':
    app.run(debug=True, port='3000')
