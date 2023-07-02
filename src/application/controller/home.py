from src import app, db

class Home:

    @staticmethod
    @app.route('/', methods=['GET'])
    def home():
        db.create_all()
        return 'Welcome Jira Dashboard'