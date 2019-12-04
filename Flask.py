from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
	{ 
		"name": "My Wonderfull Store",
		"items": [
			{
			"name": "My Item",
			"price": 15.99
			}
		]

	}
]

@app.route('/')
def home():
	return render_template("index.html")

# POST Store Data {name}
@app.route("/store", methods=['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
	"name": request_data["name"],
	"items": []
	}
	stores.append(new_store)
	return jsonify(new_store)

# Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	for store in stores:
		if store["name"] == name:
			return jsonify(store)
		return jsonify({'Message': 'Store not found'})

# Get /Store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})

@app.route("/store/<string:name>/item", methods=['POST'])
def create_itme_in_store(name):
	for store in stores:
		request_data = request.get_json()
		if store["name"] == name:
			new_item = {
			"name": request_data["name"],
			"price": request_data["price"]
			}
			store["items"].append(new_item)
			return jsonify(new_item)
		return jsonify({"message": 'Store not found' })

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify({"items": store["items"]})
		return jsonify({"message": 'Store not found' })



app.run(port=5000, debug=True)