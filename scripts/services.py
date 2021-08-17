from scripts.tools import count_form_boolean_fields
from scripts.metadata import bibliographic_managers, metadata_export_types

def evaluate_items(links, items_dict):
    if 0 < len(links):
        values = {i: 1 for i, j in items_dict.items()}
        for i in links:
            for x, y in list(items_dict.items()):
                items_sum = sum([1 if i[x][m] is not None else 0 for m in y])
                if items_sum == len(y):
                    pass
                elif items_sum == 0:
                    values[x] = 0
                    del items_dict[x]
                else:
                    values[x] = 0.5
            if not items_dict:
                break
        return values
    return {i: 0 for i, j in items_dict.items()}

def execute_services(form, links):
    services_resume = count_form_boolean_fields(form)
    evaluated_items = evaluate_items(links, {'bibliographic_managers': bibliographic_managers,
                                             'metadata_exports': metadata_export_types})
    services_resume['bibliographic_managers'], services_resume['metadata_exports'] = evaluated_items[
                                                                                         'bibliographic_managers'], \
                                                                                     evaluated_items['metadata_exports']
    services_resume['total'] = sum(
        services_resume[i]['value'] if dict == type(services_resume[i]) else services_resume[i] for i in
        services_resume)
    return services_resume
