from flask import Flask
import json
from function.cafeteria_crawl import seo_crawl

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/cafe/<cafeteria>/<day>', methods=['GET'])
def get_menu(cafeteria, day):
    return json.dumps(seo_crawl(cafeteria, day), ensure_ascii=False)

"""
cafeteria : inmoon, gyosoo, sky
day: today, tomorrow
"""

if __name__ == "__main__":
    app.run()
