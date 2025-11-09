# -------- EMPLOYEE SALARY SORTING SYSTEM --------

# Function for Selection Sort
def selection_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        # swap the smallest with current element
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]

# Function for Bubble Sort
def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                # swap adjacent elements
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]

# Function to display top 5 highest salaries
def display_top_five(salaries):
    print("\nTop 5 Highest Salaries:")
    top_five = sorted(salaries, reverse=True)[:5]  # sort descending, take first 5
    for i, sal in enumerate(top_five, start=1):
        print(f"{i}. ₹{sal:.2f}")

# ---------------- MAIN PROGRAM ----------------
salaries = []

# Input employee salaries
n = int(input("Enter number of employees: "))
for i in range(n):
    sal = float(input(f"Enter salary of employee {i + 1}: "))
    salaries.append(sal)

print("\nOriginal Salaries:", salaries)

# --- Selection Sort ---
sel_sorted = salaries.copy()
selection_sort(sel_sorted)
print("\nSalaries sorted using Selection Sort:")
print(sel_sorted)
display_top_five(sel_sorted)

# --- Bubble Sort ---
bub_sorted = salaries.copy()
bubble_sort(bub_sorted)
print("\nSalaries sorted using Bubble Sort:")
print(bub_sorted)
display_top_five(bub_sorted)
