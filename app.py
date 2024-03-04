from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html')

@app.route('/market')
def market():
    items = [
        {'id':1234, 'name':'Iphone', 'barcode':75679893, 'price':750},
        {'id':1345, 'name':'Ipad', 'barcode':89814283, 'price':500},    
        {'id':1456, 'name':'Macbook', 'barcode':32354674, 'price':1200},    
        {'id':1567, 'name':'Speaker', 'barcode':91929394, 'price':250},    
    ]
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)