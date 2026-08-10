import statistics

def summarize_grades(grades):
    """Calculates the mean and standard deviation of a list of grades."""
    return {
        "mean": round(statistics.mean(grades), 2),
        "stdev": round(statistics.stdev(grades), 2)
    }

# Program execution
scores = [88, 92, 79, 95, 85, 90]
summary = summarize_grades(scores)
print("Grade Summary:", summary)