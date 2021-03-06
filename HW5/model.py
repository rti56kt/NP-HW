import sys
sys.path.append('/home/ubuntu/.local/lib/python3.6/site-packages')
import peewee as pw

db = pw.MySQLDatabase("NPHW5", host="nphw5.cv3oldlhafib.us-east-1.rds.amazonaws.com", port=3306, user="nctunphw5", passwd="nctunphw5")


class BaseModel(pw.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = pw.CharField(unique=True)
    password = pw.CharField()


class Invitation(BaseModel):
    inviter = pw.ForeignKeyField(User, on_delete='CASCADE')
    invitee = pw.ForeignKeyField(User, on_delete='CASCADE')


class Friend(BaseModel):
    user = pw.ForeignKeyField(User, on_delete='CASCADE')
    friend = pw.ForeignKeyField(User, on_delete='CASCADE')


class Post(BaseModel):
    user = pw.ForeignKeyField(User, on_delete='CASCADE')
    message = pw.CharField()


class Serverpool(BaseModel):
    instanceid = pw.CharField(unique=True)
    serverip = pw.CharField(unique=True)


class Servermap(BaseModel):
    user = pw.ForeignKeyField(User, on_delete='CASCADE')
    serverdistributed = pw.ForeignKeyField(Serverpool, on_delete='CASCADE')


class Token(BaseModel):
    token = pw.CharField(unique=True)
    owner = pw.ForeignKeyField(User, on_delete='CASCADE')


class Topic(BaseModel):
    topicname = pw.CharField(unique=True)


class Subscribe(BaseModel):
    user = pw.ForeignKeyField(User, on_delete='CASCADE')
    topic = pw.ForeignKeyField(Topic, on_delete='CASCADE')

if __name__ == '__main__':
    db.connect()
    db.create_tables([User, Invitation, Friend, Post, Serverpool, Servermap, Token, Topic, Subscribe])
