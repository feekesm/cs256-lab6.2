def parse_course_record(course_string):
    clean_course = course_string.upper()
    clean_course = clean_course.strip()
    clean_course = clean_course.split(",")

    parsed_course = {
        "code": clean_course[0].strip(),
        "title": clean_course[1].strip(),
        "credits": int(clean_course[2].strip()),
        "status": clean_course[3].strip()
    }

    return parsed_course

def get_gen_ed_category(course_code, gen_ed_mapping):

    for category in gen_ed_mapping:
        if course_code in gen_ed_mapping[category]:
            return category

    return "uncategorized"

def bin_student_courses(transcript, gen_ed_mapping):

    returned_bins = {}

    for category in gen_ed_mapping:
        returned_bins[category] = []

    returned_bins["uncategorized"] = []

    for course in transcript:

        parsed_course = parse_course_record(course)

        category = get_gen_ed_category(
            parsed_course["code"],
            gen_ed_mapping
        )

        returned_bins[category].append(parsed_course)

    return returned_bins

def audit_credits(student_bins):

    audit = {}

    for bin in student_bins:

        total_credits = 0

        for course in student_bins[bin]:

            if course["status"] == "COMPLETE":
                total_credits += course["credits"]

        audit[bin] = total_credits

    return audit

def main():

    # General Education course mapping
    gen_ed_categories = {
        "CE": [],
        "CI": [],
        "EDI": [],
        "IA": [],
        "NL": [],
        "PL": []
    }

    # Student transcript
    transcript = [
        "MTH-112, Pre-Calculus, 4, COMPLETE",
        "COMM-482, Communication, 3, COMPLETE",
        "PHL-201, Philosophy, 4, INCOMPLETE"
    ]

    # Organize student courses into categories
    student_final_bins = bin_student_courses(
        transcript,
        gen_ed_categories
    )

    print(student_final_bins)

    # Calculate completed credits
    credit_totals = audit_credits(student_final_bins)

    print(credit_totals)


main()