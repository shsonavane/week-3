import seaborn as sns
import pandas as pd


# update/add code below ...
# Exercise 1: Recursive Fibonacci

def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)

    Returns:
        int: The nth Fibonacci number
    """
    # Base cases: stop recursion
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case: sum of previous two Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)



# Test Cases


print("Fibonacci Tests:")
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(2))   # 1
print(fibonacci(3))   # 2
print(fibonacci(4))   # 3
print(fibonacci(5))   # 5
print(fibonacci(6))   # 8
print(fibonacci(7))   # 13
print(fibonacci(8))   # 21
print(fibonacci(9))   # 34


#-----------------------------------------


# Exercise 2: Decimal to Binary

def to_binary(n: int) -> str:
    """
    Convert a non-negative integer into its binary representation using recursion.

    Args:
        n (int): A non-negative integer

    Returns:
        str: Binary representation of n
    """
    # Base case: 0 or 1 (lowest binary digits)
    if n < 2:
        return str(n)

    # Recursive case: binary of n//2 followed by remainder
    return to_binary(n // 2) + str(n % 2)



# Test Cases


print("Binary Conversion Tests:")
print(to_binary(0))    # 0
print(to_binary(1))    # 1
print(to_binary(2))    # 10
print(to_binary(5))    # 101
print(to_binary(12))   # 1100
print(to_binary(19))   # 10011


#----------------------------------------


# Exercise 3

# Load dataset
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)



def task_1():
    """
    Return a list of column names sorted by missing values.
    Tie-breaker: alphabetical order if missing counts are equal.
    """

    # Fix messy 'gender' column
    if "gender" in df_bellevue.columns:
        df_bellevue["gender"] = df_bellevue["gender"].str.strip().str.capitalize()
        print("Note: Cleaned 'gender' column (removed spaces, capitalized values).")

    # Count missing values per column
    missing_counts = df_bellevue.isnull().sum()

    # Sort by (missing count, column name)
    sorted_columns = (
        missing_counts.sort_values(kind="mergesort")
        .sort_index()
        .index.tolist()
    )

    # Correct tie-breaking: sort by (missing, colname)
    sorted_columns = sorted(missing_counts.index, key=lambda col: (missing_counts[col], col))

    return sorted_columns


def task_2():
    """
    Return a DataFrame with two columns:
    - 'year': each year in the dataset
    - 'total_admissions': number of admissions per year
    """

    if "date_in" not in df_bellevue.columns:
        print("Warning: 'date_in' column missing in dataset.")
        return pd.DataFrame()

    # Extract year from date_in
    df_bellevue["year"] = pd.to_datetime(df_bellevue["date_in"], errors="coerce").dt.year

    # Group by year and count rows
    admissions_per_year = (
        df_bellevue.groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )

    return admissions_per_year



def task_3():
    """
    Return a Series with:
    - Index: gender
    - Values: average age for that gender
    """

    if "age" not in df_bellevue.columns or "gender" not in df_bellevue.columns:
        print("Warning: 'age' or 'gender' column missing.")
        return pd.Series()

    # Clean gender column again just in case
    df_bellevue["gender"] = df_bellevue["gender"].str.strip().str.capitalize()

    avg_age_by_gender = df_bellevue.groupby("gender")["age"].mean()

    return avg_age_by_gender


def task_4():
    """
    Return a list of the 5 most common professions in order of prevalence.
    """

    if "profession" not in df_bellevue.columns:
        print("Warning: 'profession' column missing in dataset.")
        return []

    top_5_professions = (
        df_bellevue["profession"]
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return top_5_professions



# Test Outputs

print("Task 1 Output (sorted columns):")
print(task_1(), "\n")

print("Task 2 Output (admissions per year):")
print(task_2().head(), "\n")

print("Task 3 Output (average age by gender):")
print(task_3(), "\n")

print("Task 4 Output (top 5 professions):")
print(task_4())
