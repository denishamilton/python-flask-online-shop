from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/haushaltsgeraete')
def haushaltsgeraete():
    return render_template('haushaltsgeraete.html', title='Haushaltsgeraete')

@app.route('/pc_laptops')
def pc_laptops():
    return render_template('pc_laptops.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html', title='Kontakt')

@app.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html', title='Impressum')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html', title='Datenschutz')

if __name__ == '__main__':
    app.run(debug=True)