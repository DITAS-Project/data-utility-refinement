/**
 * Copyright 2018 Information System Group, DEIB, Politecnico di Milano
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 * 
 * This is being developed for the DITAS Project: https://www.ditas-project.eu/
 */


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
