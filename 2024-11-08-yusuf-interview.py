# %%
from collections import Counter

# %%
# Consider that you are running operations at a recycling center.
# You are given a list of items to be thrown away.
# You need to classify them into three categories: recyclable, compostable, and landfill.
# Determine which category has the most items.


# %%
# 1.

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
# 2.

def find_most_common_category(items: list[str], category_dict: dict[str, str]) -> str:
    pass

def find_most_common_category(items: list[str], category_dict: dict[str, str]) -> str:
    return max(Counter(category_dict[item] for item in items).items(), key=lambda x: x[1])[0]

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
# 3.

def determine_revenue(items: list[str], category_dict: dict[str, str], revenue_dict: dict[str, int]) -> int:
    pass

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
