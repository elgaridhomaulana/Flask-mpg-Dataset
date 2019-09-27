from flask import Flask, render_template
from data_mpg import mpg_data, ranking
from plots import hist_mpg, hist_hp

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data = mpg_data().head()
    return render_template('table_data.html', data=data)

@app.route('/plots')
def plots():
    data1 = hist_mpg()
    data2 = hist_hp()
    return render_template('plots.html', data=[data1,data2])

@app.route('/stats')
def stats():
    big_hp = ranking('horsepower')
    irit = ranking('mpg')
    return render_template('stats.html', data = [big_hp, irit])

if __name__ == '__main__':
    app.run(debug=True, port=5000)