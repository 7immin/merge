from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/travel') 
def travel():
    return render_template("travel.html")  # 'travel.html'렌더링

@app.route('/api/order-count', methods=['GET'])
def get_order_count():
    order_count = 4 # 예시로 주문 횟수를 4로 설정
    return jsonify({'orderCount': order_count})

if __name__ == '__main__':
    app.run(debug=True)
