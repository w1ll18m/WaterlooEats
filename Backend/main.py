from src import create_app
from src.celery_config import make_celery

app = create_app()
celery = make_celery(app)

if __name__ == '__main__':
    app.run(debug=True)