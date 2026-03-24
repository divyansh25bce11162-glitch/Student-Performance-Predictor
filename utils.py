def marks_to_gpa(marks):
    if marks >= 90:
        return 10, "S"
    elif marks >= 80:
        return 9, "A"
    elif marks >= 70:
        return 8, "B"
    elif marks >= 60:
        return 7, "C"
    elif marks >= 50:
        return 6, "D"
    else:
        return 0, "F"

def give_suggestions(attendance, study_hours, assignments, predicted_marks):
    suggestions = []

    if attendance < 75:
        suggestions.append("Increase attendance above 75%")

    if study_hours < 2:
        suggestions.append("Study at least 2–3 hours daily")

    if assignments < 60:
        suggestions.append("Improve assignment performance")

    if predicted_marks < 60:
        suggestions.append("You are at risk. Focus on fundamentals and revise regularly")

    if predicted_marks > 85:
        suggestions.append("Excellent performance! Maintain consistency")

    return suggestions
