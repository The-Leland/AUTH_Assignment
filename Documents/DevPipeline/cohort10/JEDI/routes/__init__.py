


from .auth_routes import auth_bp
from .user_routes import user_bp
from .temple_routes import temple_bp
from .padawan_routes import padawan_bp
from .master_routes import master_bp
from .lightsaber_routes import lightsaber_bp
from .crystal_routes import crystal_bp
from .species_routes import species_bp
from .course_routes import course_bp
from .enrollment_routes import enrollment_bp

all_blueprints = [
    auth_bp,
    user_bp,
    temple_bp,
    padawan_bp,
    master_bp,
    lightsaber_bp,
    crystal_bp,
    species_bp,
    course_bp,
    enrollment_bp
]
