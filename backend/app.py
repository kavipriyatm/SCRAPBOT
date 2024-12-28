from flask import Flask, request, jsonify
from scraper import scrape_static, scrape_dynamic

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the ScrapBot API!"

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.json
        url = data.get('url')
        scrape_type = data.get('type', 'static')

        if scrape_type == 'static':
            result = scrape_static(url)
        elif scrape_type == 'dynamic':
            result = scrape_dynamic(url)
        else:
            return jsonify({"error": "Invalid scrape type"}), 400

        return jsonify({"success": True, "data": result}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)