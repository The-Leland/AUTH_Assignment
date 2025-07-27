
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.padawan_routes import padawan_bp
from routes.master_routes import master_bp
from routes.temple_routes import temple_bp
from routes.species_routes import species_bp
from routes.lightsaber_routes import lightsaber_bp
from routes.crystal_routes import crystal_bp
from routes.course_routes import course_bp
from routes.enrollment_routes import enrollment_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(padawan_bp)
    app.register_blueprint(master_bp)
    app.register_blueprint(temple_bp)
    app.register_blueprint(species_bp)
    app.register_blueprint(lightsaber_bp)
    app.register_blueprint(crystal_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(enrollment_bp)

