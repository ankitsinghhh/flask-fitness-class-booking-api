from flask import Blueprint, request, jsonify, current_app
from config.database import get_connection
from datetime import datetime
import pytz

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route('/classes', methods=['GET'])
def get_classes():
    timezone = request.args.get('timezone', 'Asia/Kolkata')
    tz = pytz.timezone(timezone)

    conn = get_connection(current_app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, datetime, instructor, available_slots FROM classes')
    classes = cursor.fetchall()
    result = []
    for cls in classes:
        cls_datetime = datetime.fromisoformat(cls[2]).astimezone(tz)
        result.append({
            'id': cls[0],
            'name': cls[1],
            'datetime': cls_datetime.isoformat(),
            'instructor': cls[3],
            'available_slots': cls[4]
        })
    conn.close()
    return jsonify(result)

@booking_bp.route('/book', methods=['POST'])
def book_class():
    data = request.get_json()
    required_fields = ['class_id', 'client_name', 'client_email']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    conn = get_connection(current_app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('SELECT available_slots FROM classes WHERE id = ?', (data['class_id'],))
    class_info = cursor.fetchone()

    if not class_info:
        conn.close()
        return jsonify({'error': 'Class not found'}), 404
    if class_info[0] <= 0:
        conn.close()
        return jsonify({'error': 'No slots available'}), 400

    booked_at = datetime.now(pytz.timezone('Asia/Kolkata')).isoformat()
    cursor.execute('''
        INSERT INTO bookings (class_id, client_name, client_email, booked_at)
        VALUES (?, ?, ?, ?)
    ''', (data['class_id'], data['client_name'], data['client_email'], booked_at))
    cursor.execute('''
        UPDATE classes SET available_slots = available_slots - 1 WHERE id = ?
    ''', (data['class_id'],))

    conn.commit()
    conn.close()
    return jsonify({'message': 'Booking successful'}), 201

@booking_bp.route('/bookings', methods=['GET'])
def get_bookings():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email is required'}), 400

    conn = get_connection(current_app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('''
        SELECT b.id, b.class_id, c.name, c.datetime, b.client_name, b.client_email, b.booked_at
        FROM bookings b
        JOIN classes c ON b.class_id = c.id
        WHERE b.client_email = ?
    ''', (email,))
    bookings = cursor.fetchall()
    result = []
    for b in bookings:
        result.append({
            'booking_id': b[0],
            'class_id': b[1],
            'class_name': b[2],
            'class_datetime': b[3],
            'client_name': b[4],
            'client_email': b[5],
            'booked_at': b[6]
        })
    conn.close()
    return jsonify(result)