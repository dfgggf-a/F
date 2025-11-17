from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Meow</title>
    <style>
        body {
            background-color: #fff7ec;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        img {
            width: 300px;
            border-radius: 15px;
            margin: 15px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
        }
        button {
            background-color: #ffb6c1;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #ffa0a0;
        }
        h2 {
            margin: 20px 0;
            color: #ff69b4;
        }
    </style>
</head>
<body>
    <h2>meowmeowmeowmeowmeow</h2>
    <h1>🐾 Random Cat Viewer 🐾</h1>

    <form method="POST">
        <button type="submit">Show Random Cat</button>
    </form>

    {% if cat_url %}
        <div>
            <img src="{{ cat_url }}" alt="Random Cat">
        </div>
    {% endif %}

    <h2>meowmeowmeowmeowmeow</h2>
</body>
</html>
"""

def get_random_cat_url():
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        return data[0]["url"]
    except Exception:
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    cat_url = None
    if request.method == "POST":
        cat_url = get_random_cat_url()
    return render_template_string(html, cat_url=cat_url)

#if __name__ == "__main__":
   # print("Flask cat site running!")
   # app.run(debug=True)

