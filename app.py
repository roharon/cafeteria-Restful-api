from flask import Flask
import json
from function.cafeteria_crawl import seo_crawl
from function.cafeteria_crawl import glo_crawl

app = Flask(__name__)

@app.route('/')
def main():
    return """
    <head>
    <title>HUFS Cafeteria API</title>
    </head>

    <body>
    <h1>HUFS Cafeteria API - Document.</h1>
    <hr>
    <h3>GET /cafe/&lt;cafeteria&gt;/&lt;day&gt;</h3>
    <p>&lt;cafeteria&gt; : 인문관 inmoon | 교수회관 gyosoo | 스카이라운지 sky</p>
    <p>&lt;cafeteria&gt; : 어문관 umoon | 후생관 hooseng | 후생관 교직원식당 faculty_member |기숙사식당 hufsdorm | 국제사회교육원 training_center</p>
    <p>&lt;day&gt; : 오늘 today | 내일 tomorrow</p>
    <br>

    <blockquote>
        <pre>
            <code>
///cafe/inmoon/today

{
  "food": [
  ],
  "price": [
  ],
  "cal": [
  ]
}
            </code>
        </pre>
    </blockquote>
    
    문의🖐 roharon@studentpartner.com
    <br>
    개발자 github 👉🏻 <a href="https://www.github.com/roharon">github.com/roharon</a>
    </body>
    """


@app.route('/cafe/<cafeteria>/<day>', methods=['GET'])
def get_menu(cafeteria, day):
    if cafeteria in ['inmoon', 'sky', 'gyosoo']:
        return json.dumps(seo_crawl(cafeteria, day), ensure_ascii=False)
    else:
        return json.dumps(glo_crawl(cafeteria, day), ensure_ascii=False)


"""
cafeteria : inmoon, gyosoo, sky
day: today, tomorrow
"""

if __name__ == "__main__":
    app.run(debug=True)
