def add_categories(listOfCategories: list[str]):
    '''
    adds the categories of causes that could lead to the problem.
    '''

    causes = {s: None for s in listOfCategories}

    return causes

def update_causes(causes: dict, new_cause_pairs: list[dict[str, str]]) -> dict:
    '''
    adds new causes, subcauses, or categories to the causes dictionary
    '''
    for pair in new_cause_pairs:
        causes.update(pair)
    return causes

gemeni_functions_list = [
    add_categories,
    update_causes
]

gemeni_functions = {func.__name__: func for func in gemeni_functions_list}
