import os
import pickle
import re
import sys
from joblib import Parallel, delayed
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

from CSFSEvaluator import CSFSEvaluator
from CSFSLoader import CSFSLoader
from CSFSSelector import CSFSBestUncertainSelector

# def _conduct_analysis(df, target, std, N_features, N_samples, dataset_name):
#     sys.stdout.write('std:{}{}'.format(std,'\n'))
#     evaluator = CSFSEvaluator(df, target, fix_std=std)
#     best_noisy_selector = CSFSBestUncertainSelector(df, target, fix_std=std)
#     for n in N_features:
#         aucs = evaluator.evaluate_noisy(n, N_samples, best_noisy_selector)
#
#         filepath = '{}/{}features_{}samples_{:.9f}std'.format(dataset_name, n, len(aucs['best_noisy']), std)
#         if not os.path.isdir('pickle-dumps/'+dataset_name):
#             os.mkdir('pickle-dumps/'+dataset_name)
#
#         pickle.dump(aucs, open("pickle-dumps/{}.pickle".format(filepath), 'wb'))
from analysis_artificial import visualise_results


N_features = [3,5,7,10]#,11,13,16]


def analysis_general(dataset_name, N_features, N_samples):
    path = "datasets/artificial/{}.csv".format(dataset_name)
    df = CSFSLoader().load_dataset(path)
    target = "T"

    Parallel(n_jobs=8)(delayed(_conduct_analysis)(df, target, std, N_features, N_samples, dataset_name) for std in np.linspace(0.00001, 0.3, 500))

def do_analysis():
    N_features = [3,5,7,10]#,11,13,16]
    N_samples = 100
    analysis_general("artificial20",N_features, N_samples)
    analysis_general("artificial21",N_features, N_samples)
    analysis_general("artificial22",N_features, N_samples)
    analysis_general("artificial23",N_features, N_samples)
    analysis_general("artificial24",N_features, N_samples)
    analysis_general("artificial25",N_features, N_samples)
    analysis_general("artificial26",N_features, N_samples)
    analysis_general("artificial27",N_features, N_samples)

#
# def get_result_data(n_features, dataset_name):
#     """
#
#     :return: {no_features: {std: auc},...} e.g. {16: {0.200036667: 0.53119531952662713, 0.105176567: 0.57273262130177505
#     """
#     path = 'pickle-dumps/{}/'.format(dataset_name)
#     files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
#
#     results = dict()
#     pattern = r'(\d+)features_100samples_(.*?)std'
#     for f in files:
#         match = re.match(pattern, f)
#         # print(f)
#         no_features = int(match.group(1))
#         std = float(match.group(2))
#
#         if no_features not in results.keys():
#             results[no_features] = dict()
#
#         results[no_features][std] = (np.mean(pickle.load(open(os.path.join(path,f), 'rb'))['best_noisy']))
#     if n_features:
#         results = {r:results[r] for r in n_features}
#     return results
# def extract_x_y(result, n_features, start_lim=0):
#     """
#     extracts x and y from results for a certain n_features
#     :param result:
#     :param n_features:
#     :return: x,y where x: std and y:auc
#     """
#     if n_features not in result.keys():
#         print('{} not found'.format(n_features))
#         return None
#     x = sorted([std for std in result[n_features].keys() if std > start_lim])
#     y = [result[n_features][std] for std in x]
#
#     return np.array(x, dtype=float), np.array(y, dtype=float)
#
# def visualise_results(dataset_name, show_plot=True):
#     N_features = [3,5,7,10]
#     results = get_result_data(N_features, dataset_name)
#     plt.hold(True)
#     start_lim = 0.1
#     params = dict()
#
#     def func(x,  w1, p1, w2, p2):
#         return w1 * pow(x, p1) + w2 * pow(x, p2)
#
#     # def func(x, w1, p1, w2, p2, w3):
#     #     return w1 * pow(x, p1) + w2 * pow(x, p2) + w3 * np.log10(x)
#
#     for n_f in N_features:
#         print('== no of features: {}'.format(n_f))
#         x,y = extract_x_y(results, n_f, start_lim=0)
#         std = np.std(y)
#         plt.plot(x, y, alpha=0.5, label='data {} (std={:.3f})'.format(n_f, std))
#         x,y = extract_x_y(results, n_f, start_lim=start_lim)
#         popt, pcov = curve_fit(func, x, y)
#         params[n_f] = popt
#         perr = np.sqrt(np.diag(pcov))
#         avg_err = np.mean(perr)
#         print('params: {} '.format(popt))
#         print('errors: {}'.format(perr))
#         print('avg error: {}'.format(avg_err))
#
#         plt.plot(x, func(x, *popt), '-k', linewidth=2, label="Fitted {} (avg err: {:.3f})".format(n_f, avg_err))
#
#     plt.legend(loc=3)
#     plt.title('auc scores / fitted curves for noisy IG. start fitting at std={}'.format(start_lim))
#     plt.xlim([-.01, 0.31])
#     plt.ylim([0.5, 1.05])
#     plt.xlabel('std')
#     plt.ylabel('auc')
#     fig1 = plt.gcf()
#     if show_plot:
#         plt.show()
#
#
#     if not os.path.isdir('plots/{}/'.format(dataset_name)):
#             os.mkdir('plots/{}/'.format(dataset_name))
#     fig1.savefig('plots/{}/std_result.png'.format(dataset_name), dpi=100)
#     plt.hold(False)
#     plt.clf()

def evaluate():
    dataset_names = ['artificial20','artificial21','artificial22','artificial23','artificial24','artificial25','artificial26','artificial27']
    Parallel(n_jobs=3)(delayed(visualise_results)(dn, N_features) for dn in dataset_names)

if __name__ == "__main__":

    # do_analysis()
    evaluate()