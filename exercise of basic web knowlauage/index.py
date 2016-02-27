from flask import Flask, render_template,request
from sqlalchemy import Column, String,create_engine,Integer,Text#from sqlalchemy import create_engine, Column, Integer, Text, String
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base#database#from sqlalchemy.ext.declarative import declarative_base

from wtforms import Form,StringField,SubmitField

app = Flask(__name__)#app = Flask(__name__)



engine = create_engine("sqlite:///adc.db", echo=True)
#engine = create_engine("sqlite:///flask-blog.db", echo=True)

#DBSession=sessionmaker(bind=engine)
Session = sessionmaker(bind=engine)
#session=DBSession()#creat session
session = Session()
#Base=declarative_base()
Base = declarative_base()

#class Post(Base):
    #__tablename__='post'

    #id=Column(String,primary_key=True)
    #tittle=Column(String(20))
    #body=Column(Text)

#class Post(Base):
    #__tablename__ = "posts"

    #id = Column(Integer,primary_key=True)
    #title = Column(String)
    #body = Column(Text)
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
#Base.metadata.create_all(engine)#create database
Base.metadata.create_all(engine)


class BlogForm(Form):
    name=StringField('name')
    body=StringField('body')
    submit=SubmitField('submit')



@app.route("/",methods=['GET','POST'])
def index():
    form = BlogForm(request.form)
    if form.validate():
        post=Post(title=form.name.data, body=form.body.data)
        session.add(post)
        session.commit()	#flask-sqlalchemy db.sesion.add ,User.query(table).filter
         
    return render_template('form.html',form=form)

@app.route("/posts/<int:post_id>")#from database take some datas
def show_post(post_id):
    post=session.query(Post).filter(Post.id==post_id).first()#missiong query(post)
    post = session.query(Post).filter(Post.id == post_id).first()
    if post:
        return render_template('show_post.html', post=post)
    else:
        return 'post NOT Found'

@app.route('/posts/')
def store_post():
    posts=session.query(Post).order_by(Post.id)
    return render_template('store.html',posts=posts)



if __name__=='__main__':
    app.run(debug=True, host='127.0.0.4')

