from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index_page():
    return render_template('index.html',title='Home')

@app.route('/index1')
def index_page1():
    return render_template('index1.html')

@app.route('/brand-business')
def brand_business():
    return render_template('brand-business.html',title='Brand-Business')


@app.route('/consumer')
def consumer():
    return render_template('consumer.html',title='Consumer')

@app.route('/social-impact')
def social_impact():
    return render_template('social-impact.html',title='Social-Impact')

@app.route('/blog')
def blog():
    return render_template('blog.html',title='Blog')

@app.route('/news')
def news():
  return render_template('news.html',title='News')
    
@app.route('/news2')
def news_page():
    return render_template('newspage2.html',title='News')
    