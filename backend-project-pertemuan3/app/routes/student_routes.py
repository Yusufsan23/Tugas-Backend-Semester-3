from flask import Blueprint, request, jsonify
from app.repositories.student_repo import StudentRepository
from app.services.student_service import StudentService

student_bp = Blueprint("students", __name__, url_prefix="/api/v1/students")
repo = StudentRepository()
service = StudentService(repo)


@student_bp.route("", methods=["GET"])
def list_students():
    major_query = request.args.get("major")
    resp, status_code = service.fetch_students(major_query)
    return jsonify(resp), status_code


@student_bp.route("/<int:student_id>", methods=["GET"])
def find_student(student_id):
    resp, status_code = service.get_student_details(student_id)
    return jsonify(resp), status_code

@student_bp.route("", methods=["POST"])
def create_student():
    data = request.get_json() if request.is_json else None
    resp, status_code = service.add_new_student(data)
    return jsonify(resp), status_code

@student_bp.route("/<int:student_id>", methods=["PUT"])
def modify_student(student_id):
    data = request.get_json() if request.is_json else {}
    resp, status_code = service.update_student(student_id, data)
    return jsonify(resp), status_code


@student_bp.route("/<int:student_id>", methods=["DELETE"])
def remove_student(student_id):
    resp, status_code = service.delete_student(student_id)
    return jsonify(resp), status_code
