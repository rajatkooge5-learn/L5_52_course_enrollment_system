
"""Course enrollment system with secure coding practices."""

import hashlib
import os
import secrets

COURSES = {
    "CS101": {
        "title": "Data Structures",
        "seats": 3,
        "fee": 500.0,
        "is_closed": False,
    },
    "CS202": {
        "title": "Operating Systems",
        "seats": 0,
        "fee": 550.0,
        "is_closed": True,
    },
    "CS303": {
        "title": "Compiler Design",
        "seats": 4,
        "fee": 600.0,
        "is_closed": False,
    },
}

COURSE_STATE = {"total_tuition": 0.0}


def enroll_student(
    course_id,
    student_name,
    credits_registered=3,
    audit_trail=None,
):
    """Enroll a student if the course has available seats."""
    if audit_trail is None:
        audit_trail = []

    if course_id not in COURSES:
        return False

    course = COURSES[course_id]
    if course["is_closed"] or course["seats"] <= 0:
        return False

    course["seats"] -= 1
    if course["seats"] == 0:
        course["is_closed"] = True

    COURSE_STATE["total_tuition"] += course["fee"]
    audit_trail.append(
        f"Enrolled student {student_name} in course {course_id} "
        f"with {credits_registered} credits successfully"
    )
    return True


def drop_course(course_id):
    """Reopen a course when a valid course is dropped."""
    if course_id not in COURSES:
        return False

    course = COURSES[course_id]
    course["seats"] += 1
    course["is_closed"] = False
    return True


def check_course_status(course_id):
    """Return whether a course exists and is open."""
    course = COURSES.get(course_id)
    return course is not None and not course["is_closed"]


def calculate_scholarship_tuition(course_id, discount_rate=0.25):
    """Calculate tuition after applying a valid discount rate."""
    if course_id not in COURSES:
        raise ValueError("Unknown course ID")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1")

    base_fee = COURSES[course_id]["fee"]
    return base_fee * (1 - discount_rate)


def generate_student_hash(roll_no):
    """Generate a SHA-256 digest of a student roll number."""
    return hashlib.sha256(roll_no.encode("utf-8")).hexdigest()


def generate_enrollment_otp():
    """Generate a secure four-digit enrollment OTP."""
    return secrets.randbelow(9000) + 1000


def export_course_roster(filename="course_roster.txt"):
    """Export the course catalog to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(COURSES))

    print(f"Course roster exported to: {filename}")


def get_open_courses_summary():
    """Count the courses that are currently open."""
    return sum(
        1
        for course in COURSES.values()
        if not course["is_closed"]
    )


def main():
    """Run a demonstration of the course enrollment system."""
    registrar_auth_token = os.getenv("REGISTRAR_AUTH_TOKEN")

    enroll_student("CS101", "Kritika", 4)
    drop_course("CS202")

    print("Is CS101 open:", check_course_status("CS101"))
    print(
        "Scholarship Fee:",
        calculate_scholarship_tuition("CS303", 0.25),
    )
    print("Student Hash:", generate_student_hash("REG_2026_091"))
    print("Enrollment OTP:", generate_enrollment_otp())

    export_course_roster()
    print("Open courses:", get_open_courses_summary())
    print("Total tuition:", COURSE_STATE["total_tuition"])
    print("Registrar Token configured:", bool(registrar_auth_token))


if __name__ == "__main__":
    main()
