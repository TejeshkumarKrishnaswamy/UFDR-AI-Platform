def calculate_crime_score(suspicious_count, night_activity, secret_meetings, repeated_location, risky_search):

    score = 0

    # suspicious chats
    score += suspicious_count * 5

    # late night activity
    if night_activity:
        score += 15

    # secret meeting detected
    if secret_meetings:
        score += 20

    # repeated location visits
    if repeated_location:
        score += 20

    # illegal search activity
    if risky_search:
        score += 20

    if score > 100:
        score = 100

    return score
