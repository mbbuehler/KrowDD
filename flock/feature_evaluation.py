import subprocess

import pandas as pd
import numpy as np
import re

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from tabulate import tabulate

from CSFSEvaluator import CSFSEvaluator
from CSFSSelector import CSFSBestActualSelector
from util.util_features import get_features_from_questions


def get_dataset():
    path_dataset = '../datasets/olympia/cleaned/experiment2/Olympic2016_raw_plus.csv'
    path_questions = '../datasets/olympia/questions/experiment2/featuresOlympia_hi_lo_combined.csv'
    df_raw = pd.read_csv(path_dataset)
    # binarise target variable
    df_raw['medals'] = df_raw['medals'].apply(lambda x: 0 if x == 0 else 1)
    # kick all features we don't want
    features = get_features_from_questions(path_questions, remove_binning=True)
    df = df_raw[features]
    df['medals'] = df_raw['medals']

    df = df.dropna(axis='rows')
    return df

def get_dataset_bin():
    path_dataset = '../datasets/olympia/cleaned/experiment2/Olympic2016_raw_plus_bin.csv'
    path_dataset = '../datasets/olympia/cleaned/experiment3/olympic_allyears_plus_bin.csv'
    path_questions = '../datasets/olympia/questions/experiment2/featuresOlympia_hi_lo_combined.csv'
    df_raw = pd.read_csv(path_dataset)
    # kick all features we don't want
    features = get_features_from_questions(path_questions, remove_cond=True)
    features.append('medals')
    df = df_raw[features]
    return df


df_data = get_dataset_bin() # use get_dataset() for original dataset
print(df_data[:3])
exit()
features = list(df_data.columns)

# features.remove('medals') 3 is already removed
target = 'medals'
evaluator = CSFSEvaluator(df_data, target)

R = range(3, len(df_data), 1) # number of samples
print('len data:',len(df_data))
N_Feat = [3, 5, 7, 9, 11]
n_samples = 100 # number of repetitions to calculate average auc score for samples

result = pd.DataFrame(columns=N_Feat, index=R)

# print(df_data[:3])
for r in R:
    print('processing r =',r)
    aucs = {n_feat: list() for n_feat in N_Feat}
    for i in range(n_samples):
        # get a number of samples
        df_sample = df_data.sample(n=r, axis='rows')
        df_sample.index = range(r) # otherwise we have a problem with automatic iteration when calculating conditional probabilities
        best_selector = CSFSBestActualSelector(df_sample, target)

        for n_feat in N_Feat:
            nbest_features = best_selector.select(n_feat)
            auc = evaluator.evaluate_features(nbest_features)
            aucs[n_feat].append(auc)
    result.loc[r] = {n_feat: np.mean(aucs[n_feat]) for n_feat in aucs}
result.to_csv('flock_crowd.csv')
    # auc = np.mean(aucs)
    # print(r, auc)


