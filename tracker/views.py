import os
import json

import xml.etree.ElementTree as etree
from flask import Response, render_template, request, redirect
from flask_wtf import FlaskForm, file

from tracker.app import app, db
from tracker.models import Track


@app.route('/')
def index():
    tracks = {}
    for track in Track.query.all():
        tracks[track.track_id] = f'{track.name} {track.time}'
    return render_template('index.html', tracks=tracks)


@app.route('/track/<track_id>')
def track(track_id):
    return render_template('map.html', track=track_id)


@app.route('/track/xml/<track_name>')
def track_xml(track_name):
    track_path = os.path.join('activities', track_name)
    with open(track_path) as f:
        gpx = f.read()
    return Response(response=gpx)


@app.route('/track/json/<track_id>')
def track_json(track_id):
    track = Track.query.filter_by(track_id=track_id).first()
    return Response(response=json.dumps(track.track))


class UploadForm(FlaskForm):
    track = file.FileField('Track',
                           validators=[file.FileAllowed(('xml', 'gpx'))])


def add_track(track_id, content):
    root = etree.fromstring(content)
    data = root[1][2]
    name = root[1][0].text
    time = root[0][0].text

    json = []
    for item in data:
        json.append({
            'lat': item.attrib['lat'],
            'lon': item.attrib['lon'],
            'ele': item[0].text,
            'time': item[1].text,
        })

    track = Track(name=name, time=time, track_id=track_id, track=json)
    db.session.add(track)
    db.session.commit()


@app.route('/track/upload', methods=('GET', 'POST'))
def parse():
    form = UploadForm()
    if form.validate_on_submit():
        track = request.files.get('track')
        if track:
            track_id = track.filename.replace('.gpx', '')
            exists = Track.query.filter_by(track_id=track_id).first()
            if not exists:
                add_track(track_id, track.read())

            return redirect(f'/track/{track_id}')
        else:
            _, _, files = next(os.walk('activities'))

            for file in files:
                track_id = file.replace('.gpx', '')
                if Track.query.filter_by(track_id=track_id).first():
                    continue

                with open(f'activities/{file}') as f:
                    add_track(track_id, f.read())
            return redirect('/')
    else:
        return render_template('upload.html', form=form)
