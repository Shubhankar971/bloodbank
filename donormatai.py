from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from typing import Any, Dict, List


def find_best_donor(patient: Dict[str, Any], donors: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return donors that match the patient's blood group and city."""
    data = pd.DataFrame(donors)

    matches = data[
        (data['blood_group'] == patient['blood_group']) &
        (data['city'] == patient['city'])
    ]

    return matches.to_dict('records')


if __name__ == '__main__':
    patient = {
        'blood_group': 'O+',
        'city': 'Mumbai'
    }

    donors = [
        {
            'name': 'Rahul',
            'blood_group': 'O+',
            'city': 'Mumbai'
        },
        {
            'name': 'Amit',
            'blood_group': 'A+',
            'city': 'Delhi'
        }
    ]

    print(find_best_donor(patient, donors))
