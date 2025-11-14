# Simple Ayurvedic Dosha Calculator
# Vata – Pitta – Kapha quiz (very simplified, for educational use only)

def ask_question(q_number, question, options):
    """
    Ask one multiple-choice question.
    options: dict like { "a": ("description", "Vata"), "b": (...), "c": (...) }
    Returns the dosha string: "Vata", "Pitta", or "Kapha"
    """
    print(f"\n{q_number}. {question}")
    for key, (desc, _) in options.items():
        print(f"  {key}) {desc}")
    
    while True:
        answer = input("Your choice (a/b/c): ").strip().lower()
        if answer in options:
            return options[answer][1]
        else:
            print("Invalid choice. Please enter a, b, or c.")


def main():
    print("=======================================")
    print("     Ayurvedic Dosha Quiz (Simple)     ")
    print("=======================================")
    print("Answer honestly based on your natural, long-term tendencies,")
    print("not just how you feel today.\n")

    # Score dictionary
    scores = {"Vata": 0, "Pitta": 0, "Kapha": 0}

    # Questions (very simplified model)
    questions = [
        (
            "Body frame & weight tendency",
            {
                "a": ("Light, thin, finds it hard to gain weight", "Vata"),
                "b": ("Medium build, gains and loses weight easily", "Pitta"),
                "c": ("Broad, strong, tends to gain weight easily", "Kapha"),
            },
        ),
        (
            "Skin type",
            {
                "a": ("Dry, rough, cool to touch", "Vata"),
                "b": ("Warm, reddish, may have acne or moles", "Pitta"),
                "c": ("Soft, oily, thick, cool and pale", "Kapha"),
            },
        ),
        (
            "Appetite & digestion",
            {
                "a": ("Irregular appetite, sometimes forgets to eat", "Vata"),
                "b": ("Strong appetite, gets irritated if meals are delayed", "Pitta"),
                "c": ("Slow but steady appetite, can skip meals easily", "Kapha"),
            },
        ),
        (
            "Energy pattern",
            {
                "a": ("Energy comes in bursts, then sudden tiredness", "Vata"),
                "b": ("Consistent, intense energy; likes to stay active", "Pitta"),
                "c": ("Slow to get started but has good stamina", "Kapha"),
            },
        ),
        (
            "Climate preference",
            {
                "a": ("Prefers warm climate, dislikes cold and wind", "Vata"),
                "b": ("Prefers cool climate, dislikes heat", "Pitta"),
                "c": ("Handles most climates well but dislikes damp/cold", "Kapha"),
            },
        ),
        (
            "Sleep pattern",
            {
                "a": ("Light sleeper, wakes up easily", "Vata"),
                "b": ("Moderate sleeper, 6–8 hours usually", "Pitta"),
                "c": ("Deep sleeper, finds it easy to sleep long", "Kapha"),
            },
        ),
        (
            "Mind & thoughts",
            {
                "a": ("Fast thinker, creative, but may be anxious", "Vata"),
                "b": ("Sharp, focused, can be critical or perfectionist", "Pitta"),
                "c": ("Calm, steady, sometimes slow to process", "Kapha"),
            },
        ),
        (
            "Emotional tendency under stress",
            {
                "a": ("Fear, worry, overthinking", "Vata"),
                "b": ("Anger, irritation, frustration", "Pitta"),
                "c": ("Withdrawal, sadness, emotional eating or sleeping", "Kapha"),
            },
        ),
        (
            "Speech style",
            {
                "a": ("Fast, animated, sometimes jumps topics", "Vata"),
                "b": ("Clear, direct, sometimes sharp or intense", "Pitta"),
                "c": ("Slow, calm, soothing tone", "Kapha"),
            },
        ),
        (
            "General body temperature",
            {
                "a": ("Usually feels cold; hands and feet are cool", "Vata"),
                "b": ("Usually feels warm or hot", "Pitta"),
                "c": ("Neutral or slightly cool, but not extreme", "Kapha"),
            },
        ),
        (
            "Physical activity preference",
            {
                "a": ("Likes variety, movement, change in routine", "Vata"),
                "b": ("Competitive, driven, likes challenges", "Pitta"),
                "c": ("Prefers slow, steady, comfortable pace", "Kapha"),
            },
        ),
        (
            "Memory style",
            {
                "a": ("Learns fast but forgets fast", "Vata"),
                "b": ("Learns fast, remembers details clearly", "Pitta"),
                "c": ("Learns slowly but remembers for a long time", "Kapha"),
            },
        ),
    ]

    # Ask all questions
    for i, (q_text, opts) in enumerate(questions, start=1):
        dosha = ask_question(i, q_text, opts)
        scores[dosha] += 1

    # Calculate result
    total = sum(scores.values())
    print("\n=======================================")
    print("               RESULT                  ")
    print("=======================================")
    print(f"Vata  score: {scores['Vata']} / {total}")
    print(f"Pitta score: {scores['Pitta']} / {total}")
    print(f"Kapha score: {scores['Kapha']} / {total}")

    # Percentages
    print("\nApproximate distribution:")
    for dosha, score in scores.items():
        percent = (score / total) * 100 if total > 0 else 0
        print(f"  {dosha}: {percent:.1f}%")

    # Find dominant dosha(s)
    max_score = max(scores.values())
    dominant = [d for d, s in scores.items() if s == max_score]

    print("\nYour dominant dosha type:")
    if len(dominant) == 1:
        print(f"  ➤ Primarily {dominant[0]} dosha")
    else:
        combo = " + ".join(dominant)
        print(f"  ➤ Dual/combined constitution: {combo}")

    print("\n(Disclaimer: This is a simplified educational quiz,")
    print(" not a professional Ayurvedic diagnosis.)")


if __name__ == "__main__":
    main()
