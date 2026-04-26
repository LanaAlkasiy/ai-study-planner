from datetime import datetime, timedelta

def get_difficulty_hours(difficulty):
    difficulty = difficulty.lower()
    if difficulty == "hard":
        return 3
    elif difficulty == "medium":
        return 2
    else:
        return 1

def main():
    print("AI Study Planner")
    print("----------------")

    exam_date_input = input("Enter your exam date (YYYY-MM-DD): ")
    exam_date = datetime.strptime(exam_date_input, "%Y-%m-%d").date()
    today = datetime.today().date()

    days_left = (exam_date - today).days

    if days_left <= 0:
        print("Exam date must be in the future.")
        return

    topics = []

    number_of_topics = int(input("How many topics do you need to study? "))

    for i in range(number_of_topics):
        print(f"\nTopic {i + 1}")
        name = input("Topic name: ")
        difficulty = input("Difficulty (easy/medium/hard): ")

        hours = get_difficulty_hours(difficulty)

        topics.append({
            "name": name,
            "difficulty": difficulty,
            "hours": hours
        })

    total_hours = sum(topic["hours"] for topic in topics)

    print("\nYour Study Plan")
    print("---------------")
    print(f"Days left: {days_left}")
    print(f"Estimated total study hours: {total_hours}")

    for index, topic in enumerate(topics):
        study_day = today + timedelta(days=index % days_left)
        print(f"\n{study_day}: Study {topic['name']} ({topic['difficulty']}) for {topic['hours']} hour(s)")

    print("\nSmart Tip:")
    hardest_topics = [topic["name"] for topic in topics if topic["difficulty"].lower() == "hard"]

    if hardest_topics:
        print("Start early with:", ", ".join(hardest_topics))
    else:
        print("Your topics look manageable. Review consistently.")

if __name__ == "__main__":
    main()