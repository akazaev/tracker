from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from tracker.app import app, db
from tracker import models
from tracker.config import Config


app.config.from_object(Config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
