def print_models(unprinted_design, completed_model):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_model.append(current_design)


def show_completed_models(models):
    print("\nThe following models have been printed:")
    for completed_model in models:
        print(completed_model)
