from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/index')
def index_page1():
    return render_template('index1.html')

@app.route('/brand-business')
def brand_business():
    return render_template('brand-business.html')


@app.route('/consumer')
def consumer():
    return render_template('consumer.html')

@app.route('/social-impact')
def social_impact():
    return render_template('social-impact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/news')
def news():
  return render_template('news.html')
    
@app.route('/news2')
def news_page():
    return render_template('newspage2.html')
    