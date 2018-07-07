from flask import Flask, request, render_template

from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

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

	return render_template("articles.html",articles=all_articles)




if __name__=='__main__':
	app.run(debug=True)