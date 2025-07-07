
from flask import Flask
import os
from config.database import init_db
from routes.fitness_booking_api_routes import booking_bp

def create_app():
    app = Flask(__name__)

    db_path = os.path.join(os.getcwd(), 'fitness_booking.db')
    init_db(db_path)
    app.config['DATABASE'] = db_path

    app.register_blueprint(booking_bp)

    @app.route('/')
    def home():
        return "Fitness Class Booking API server is running!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
