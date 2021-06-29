from sqlalchemy.dialects.postgresql import JSONB, TIMESTAMP

from tracker.app import db


class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.String())
    name = db.Column(db.String())
    track = db.Column(JSONB)
    time = db.Column(TIMESTAMP)
