from flask import Blueprint, request, jsonify
from models.ticket import Ticket, db

ticket_bp = Blueprint('ticket_bp', __name__)

@ticket_bp.route('/add_ticket', methods=['POST'])
def add_ticket():
    data = request.json
    id = data.get('id')
    user_id = data.get('user_id')
    movie_id = data.get('movie_id')
    showtime_id = data.get('showtime_id')
    if not (id and user_id and movie_id and showtime_id):
        return jsonify({'success': False, 'message': 'All fields are required'}), 400

    ticket = Ticket(id=id, user_id=user_id, movie_id=movie_id, showtime_id=showtime_id)

    db.session.add(ticket)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Ticket added successfully'})

@ticket_bp.route('/get_tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    tickets_data = [ticket.to_dict() for ticket in tickets]
    return jsonify(tickets_data)

@ticket_bp.route('/get_ticket/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = Ticket.query.get(ticket_id)
    if not ticket:
        return jsonify({'success': False, 'message': 'Ticket not found'}), 404

    return jsonify(ticket.to_dict())

    