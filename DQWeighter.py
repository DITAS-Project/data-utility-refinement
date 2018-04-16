import json

def DQWeighter(dimensions, application):

    weights = json.load(open("weights.json"))

    accuracy = dimensions['accuracy']
    completeness = dimensions['completeness']
    consistency = dimensions['consistency']
    timeliness=dimensions['timeliness']

    accuracy_weight = weights[application]['accuracy']
    completeness_weight = weights[application]['completeness']
    consistency_weight = weights[application]['consistency']
    timeliness_weight = weights[application]['timeliness']


    accuracy_weighted=accuracy * accuracy_weight
    completeness_weighted=completeness * completeness_weight
    consistency_weighted=consistency * consistency_weight
    timeliness_weighted=timeliness * timeliness_weight

    results={'URL': dimensions['URL'],
             'completeness': completeness_weighted,
             'consistency': consistency_weighted,
             'accuracy': accuracy_weighted,
             'timeliness': timeliness_weighted
             }

    return results
