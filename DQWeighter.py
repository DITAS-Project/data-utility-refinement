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
    
    normalization= (accuracy_weighted+ completeness_weighted+ consistency_weighted + timeliness_weighted)
    
    accuracy_weighted_norm=accuracy * (accuracy_weight/normalization)
    completeness_weighted_norm=completeness * (completeness_weight/normalization)
    consistency_weighted_norm=consistency * (consistency_weight/normalization)
    timeliness_weighted_norm=timeliness * (timeliness_weight/normalization)

    results={'completeness': completeness_weighted_norm,
             'consistency': consistency_weighted_norm,
             'accuracy': accuracy_weighted_norm,
             'timeliness': timeliness_weighted_norm
             }

    return results
