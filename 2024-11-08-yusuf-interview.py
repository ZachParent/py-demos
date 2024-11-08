# %%
# Consider that you are running operations at a recycling center.
# You are given a list of items to be thrown away.
# You need to classify them into three categories: recyclable, compostable, and landfill.
# Determine which category has the most items.


# %% 1.

def find_most_common_category(categories: list[str]) -> str:
    pass

def find_most_common_category(categories: list[str]) -> str:
    category_counts = {}
    for category in categories:
        category_counts[category] = category_counts.get(category, 0) + 1
    return max(category_counts, key=category_counts.get)

find_most_common_category(["recyclable", "compostable", "landfill", "recyclable"])



