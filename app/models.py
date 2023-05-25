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

    led_1: str

    led_2: str

    status_1: bool

    status_2: bool

    datetime: str

    id = db.Column(db.String(256),
                   primary_key=True)

    led_1 = db.Column(db.String(256),
                    nullable=False)
    
    led_2 = db.Column(db.String(256),
                    nullable=False)

    status_1 = db.Column(db.Integer,
                       nullable=False)
    
    status_2 = db.Column(db.Integer,
                       nullable=False)

    datetime = db.Column(db.DateTime,
                         nullable=False)

    def __init__(self, id: str, led_1: str, led_2: str, status_1: str, status_2: str, datetime) -> None:

        self.id = id
        self.led_1 = led_1
        self.led_2 = led_2
        self.status_1 = status_1
        self.status_2 = status_2
        self.datetime = datetime

    def __repr__(self):

        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
