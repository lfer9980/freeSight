from dataclasses import dataclass
from app import db

@dataclass
class Chat(db.Model):

    __tablename__ = 'chat'

    id: str

    msg: str

    datetime: str

    id = db.Column(db.String(256),
                   primary_key=True)

    msg = db.Column(db.String,
                    nullable=False)

    datetime = db.Column(db.DateTime,
                         nullable=False)

    def __init__(self, id: str, msg: str, datetime) -> None:

        self.id = id
        self.msg = msg
        self.datetime = datetime

    def __repr__(self):

        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))


@dataclass
class Domo(db.Model):

    __tablename__ = 'domo'

    id: str

    led: str

    status: bool

    datetime: str

    id = db.Column(db.String(256),
                   primary_key=True)

    led = db.Column(db.String(256),
                    nullable=False)

    status = db.Column(db.Integer,
                       nullable=False)

    datetime = db.Column(db.DateTime,
                         nullable=False)

    def __init__(self, id: str, led: str, status: str, datetime) -> None:

        self.id = id
        self.led = led
        self.status = status
        self.datetime = datetime

    def __repr__(self):

        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
