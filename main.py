from flask import Flask, request, render_template,json,jsonify

from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS






app=Flask(__name__)

CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rohith@localhost:5432/newdb'
app.config['SECRET_KEY'] = 'nrkjngy789y78%^&&&'

db=SQLAlchemy(app)



@app.route('/')
def index():
	return "Hello world"



class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String())
	text = db.Column(db.String())
	author = db.Column(db.String())
	subject = db.Column(db.String())


	def __init__(self,title,text,author,subject):
		self.title=title
		self.text=text
		self.author = author
		self.subject= subject


@app.route('/blog',methods=['POST','GET'])
def post_blog():
	if request.method=='POST':
		title_name=request.form['title']
		text_name=request.form['text']

		
		#return redirect(url_for('post_suc',title=title_name,text=text_name))
	return render_template('blog.html')

@app.route('/success',methods=['POST'])
def post_suc():
	title=request.form['title']
	text = request.form['text']
	author = request.form['author']
	subject= request.form['subject']
	post=Post(title,text,author,subject)
	db.session.add(post)
	db.session.commit()
	print("_____________")
	print(post.title)
	print("_________")
	return render_template("success.html",title=title,text=text,author=author,subject=subject)

@app.route('/articles',methods=['GET'])
def articles():
	all_articles=Post.query.all()

	print(all_articles)

	return render_template("articles.html",articles=all_articles)
@app.route('/authors/<author_name>',methods=['GET'])
def authors(author_name):
	author_con=Post.query.filter(Post.author ==author_name).all()
	print(author_con)

	return render_template("articles.html",articles=author_con)


@app.route('/api/<subject>')
def api_call(subject):
	articles=Post.query.filter(Post.subject==subject).all()

	output=[]

	for article in articles:
		art_dict={}
		art_dict['title']=article.title
		art_dict['text']=article.text
		art_dict['author']=article.author
		art_dict['subject']=article.subject
		output.append(art_dict)

	return jsonify(output)

	



if __name__=='__main__':
	app.run(debug=True)