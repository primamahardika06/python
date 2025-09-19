from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    title = "Halaman Utama"
    return render_template('index.html', title = title)

@app.route("/about")
def about():
    title = "Halaman About"
    return render_template ('about.html', title=title)

@app.route("/usia", methods = ['GET', 'POST'])
def usia():
    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = 2025
        usia = tahun_sekarang - tahun_lahir
        # usia_sekarang = f'Umur kamu sekarang adalah {usia} tahun'
        return render_template ('usia.html', usia=usia)
    return render_template ('usia.html', usia=None)


if __name__ == "__main__":
    app.run(debug=True)
    
    
