# Working with Lists and Averages

scores = []

print("Enter student scores (type 'done' to finish):")

while True:
    entry = input("Score: ")
    if entry.lower() == "done":
        break
    try:
        score = float(entry)
        scores.append(score)
    except ValueError:
        print("Please enter a number.")

if scores:
    print("All scores:", scores)
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))
    print("Average score:", sum(scores) / len(scores))
else:
    print("No scores entered.")
