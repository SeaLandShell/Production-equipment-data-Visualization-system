from flask import render_template
from flask import request
from flask import Flask

app = Flask(__name__,
            template_folder="../../frontend/dist",
            static_folder="../../frontend/dist/assets")
from wordcloud import *
import io
import base64

app.debug=True
# 本打算给系统弄一个词云展示的界面，以体现系统前后端联调的功能，但是网络不同域缘故，aJax未实施。
# def get_word_cloud(text):

# 主页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)


