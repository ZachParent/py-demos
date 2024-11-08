# %%
from collections import Counter, defaultdict

# %%
# Consider that you are running operations at a recycling center.


# %%
# 1. Find the most common category
# You are given a list of categorized items to be thrown away.
# Determine which category has the most items.

def find_most_common_category(categories: list[str]) -> str:
    pass

def find_most_common_category(categories: list[str]) -> str:
    return max(Counter(categories).items(), key=lambda x: x[1])[0]

def find_most_common_category(categories: list[str]) -> str:
    category_counts = {}
    for category in categories:
        if category not in category_counts:
            category_counts[category] = 0
        category_counts[category] += 1
    max_count = 0
    max_category = None
    for category, count in category_counts.items():
        if count > max_count:
            max_count = count
            max_category = category
    return max_category

find_most_common_category(
    ["recyclable", "compostable", "landfill", "recyclable"]
)
# -> "recyclable"

# %%
# 2. Find the most common category, given items and a category dictionary
# Now, you are given a list of items and a dictionary that maps items to categories.
# Determine which category has the most items.

def find_most_common_category(items: list[str], category_dict: dict[str, str]) -> str:
    pass

def find_most_common_category(items: list[str], category_dict: dict[str, str]) -> str:
    return max(
        Counter(category_dict[item] for item in items).items(),
        key=lambda x: x[1]
    )[0]

def find_most_common_category(items: list[str], category_dict: dict[str, str]) -> str:
    category_counts = {}
    for item in items:
        category = category_dict[item]
        if category not in category_counts:
            category_counts[category] = 0
        category_counts[category] += 1
    max_count = 0
    max_category = None
    for category, count in category_counts.items():
        if count > max_count:
            max_count = count
            max_category = category
    return max_category

find_most_common_category(
    ["apple", "banana", "cardboard"],
    {"apple": "compostable", "banana": "compostable", "cardboard": "recyclable"},
)
# -> "compostable"

# %%
# 3. Determine the revenue for a given list of items
# You are given a list of items, a dictionary that maps items to categories, and a dictionary that maps categories to revenue.
# Determine the total revenue for the given list of items.

def determine_revenue(items: list[str], category_dict: dict[str, str], revenue_dict: dict[str, int]) -> int:
    pass

def determine_revenue(items: list[str], category_dict: dict[str, str], revenue_dict: dict[str, int]) -> int:
    return sum(
        revenue_dict[category_dict[item]]
        for item in items
    )

def determine_revenue(items: list[str], category_dict: dict[str, str], revenue_dict: dict[str, int]) -> int:
    total_revenue = 0
    for item in items:
        category = category_dict[item]
        total_revenue += revenue_dict[category]
    return total_revenue

determine_revenue(
    ["apple", "banana", "cardboard"],
    {"apple": "compostable", "banana": "compostable", "cardboard": "recyclable"},
    {"compostable": 1, "recyclable": 2},
)
# -> 4
# %%
# 4. Determine which category of items should be processed that maximizes revenue
# You are given a list of items, a dictionary that maps items to categories, and a dictionary that maps categories to revenue.
# Determine which category has the highest revenue.

def category_to_maximize_revenue(items: list[str], category_dict: dict[str, str], revenue_dict: dict[str, int]) -> tuple[str, int]:
    pass

def category_to_maximize_revenue(items: list[str], category_dict: dict[str, str], revenue_dict: dict[str, int]) -> tuple[str, int]:
    category, count = max(
        Counter(category_dict[item] for item in items).items(),
        key=lambda x: x[1] * revenue_dict[x[0]]
    )
    return category, count * revenue_dict[category]

def category_to_maximize_revenue(items: list[str], category_dict: dict[str, str], revenue_dict: dict[str, int]) -> tuple[str, int]:
    revenue_per_category = {}
    for item in items:
        category = category_dict[item]
        if category not in revenue_per_category:
            revenue_per_category[category] = 0
        revenue_per_category[category] += revenue_dict[category]
    
    max_revenue = 0
    max_category = None
    for category, revenue in revenue_per_category.items():
        if revenue > max_revenue:
            max_revenue = revenue
            max_category = category
    return max_category, max_revenue

category_to_maximize_revenue(
    ["apple", "banana", "cardboard"],
    {"apple": "compostable", "banana": "compostable", "cardboard": "recyclable"},
    {"compostable": 1, "recyclable": 3},
)
# -> ("recyclable", 3)
# %%
