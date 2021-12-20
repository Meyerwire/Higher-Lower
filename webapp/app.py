from flask import Flask , render_template
from random import randint

richtige_zahl = randint(0,9)


app = Flask(__name__)
@app.route('/')
def zahlErraten():
    return render_template('index.html')

@app.route('/<int:nutzer_zahl>')
def richtig(nutzer_zahl):
    if nutzer_zahl > 9 or nutzer_zahl < 0:
        return render_template('cheat.html')
    elif nutzer_zahl == richtige_zahl:
        return render_template('right.html')
    elif nutzer_zahl > richtige_zahl:
        return render_template('lower-html')
    elif nutzer_zahl < richtige_zahl:
        return render_template('higher.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')