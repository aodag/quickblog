import sqlahelper
import sqlalchemy as sa
import sqlalchemy.orm as orm

DBSession = sqlahelper.get_session()
Base = sqlahelper.get_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    user_name = sa.Column(sa.Unicode(255), unique=True)
    _password = sa.Column('password', sa.String(255), nullable=False)
    
    def set_password(self, password):
        self._password = hashlib.sha1(password).hexdigest()

    password = property(fset=set_password)

    def validate_password(self, password):
        return self._password == hashlib.sha1(password).hexdigest()

class Blog(Base):
    __tablename__ = 'blogs'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(255), unique=True)
    title = sa.Column(sa.Unicode(255))
    description = sa.Column(sa.UnicodeText)

    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    user = orm.relationship('User', backref='blogs')

class Entry(Base):
    __tablename__ = 'entries'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(255), unique=True)
    title = sa.Column(sa.Unicode(255))
    content = sa.Column(sa.UnicodeText)

    blog_id = sa.Column(sa.Integer, sa.ForeignKey('blogs.id'))

    blog = orm.relationship('Blog', backref='entries')

class Comment(Base):
    __tablename__ = 'coments'
    id = sa.Column(sa.Integer, primary_key=True)
    content = sa.Column(sa.UnicodeText)

    entry_id = sa.Column(sa.Integer, sa.ForeignKey('entries.id'))

    entry = orm.relationship('Entry', backref='comments')

