
from joblib import Parallel, delayed

from analysis_artificial import analysis_general, visualise_results


N_features = [3,5,7,10]
dataset_names = ['artificial40','artificial41','artificial42','artificial43','artificial44']

def do_analysis():
    N_samples = 100
    for dn in dataset_names:
        analysis_general(dn, N_features, N_samples)

def evaluate():
    Parallel(n_jobs=4)(delayed(visualise_results)(dn, N_features, start_lim=0.035) for dn in dataset_names)
    # N: #data points
    # M: #parameters

# do_analysis()
evaluate()