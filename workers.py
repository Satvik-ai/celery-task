from celery import Celery, Task

# celery_app = Celery()
# celery_app.config_from_object("celeryconfig")


def create_celery_app(app):
    class FlaskTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                self.run(*args, **kwargs)
    
    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object("celeryconfig")
    celery_app.set_default()
    return celery_app