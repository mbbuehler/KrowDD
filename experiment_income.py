import numpy as np
import pandas as pd

from CSFSCrowdCleaner import CSFSCrowdCleaner, CSFSCrowdAggregator, CSFSCrowdAnalyser
from CSFSDataPreparator import DataPreparator
from abstract_experiment import AbstractExperiment
from application.EvaluationRanking import ERCondition


class ExperimentIncome(AbstractExperiment):

    def __init__(self, dataset_name, experiment_number, experiment_name):
        super().__init__(dataset_name, experiment_number, experiment_name)
        self.feature_range = range(1, 16)

        self.path_raw = '{}raw/{}/income.csv'.format(self.base_path, experiment_name)
        self.path_cleaned = '{}cleaned/{}/income_clean.csv'.format(self.base_path, experiment_name)
        self.path_bin = '{}cleaned/{}/income_clean_bin.csv'.format(self.base_path, experiment_name)
        self.path_autocorrelation = '{}cleaned/{}/income_bin_autocorrelation.csv'.format(self.base_path, experiment_name)
        self.path_meta = '{}cleaned/{}/income_clean_bin_meta.csv'.format(self.base_path, experiment_name)
        self.path_answers_raw = '{}results/{}/answers_raw3.xlsx'.format(self.base_path, experiment_name)
        self.path_answers_clean = '{}results/{}/answers_clean.csv'.format(self.base_path, experiment_name)
        self.path_answers_clean_grouped = '{}results/{}/answers_clean_grouped.pickle'.format(self.base_path, experiment_name)
        self.path_answers_plots = '{}results/{}/visualisations/{}_histograms_answers.html'.format(self.base_path, experiment_name, self.dataset_name)
        self.path_answers_aggregated = '{}results/{}/answers_aggregated.csv'.format(self.base_path, experiment_name)
        self.path_answers_metadata = '{}results/{}/answers_metadata.csv'.format(self.base_path, experiment_name)
        self.path_no_answers_vs_auc = '{}results/{}/answers_vs_auc.pickle'.format(self.base_path, experiment_name)
        self.path_answers_delta = '{}results/{}/answers_delta.pickle'.format(self.base_path, experiment_name)

        self.path_csfs_auc = '{}results/{}/csfs_auc.csv'.format(self.base_path, experiment_name)
        self.path_csfs_std = '{}results/{}/csfs_std.csv'.format(self.base_path, experiment_name)
        self.path_questions = '{}questions/{}/questions.csv'.format(self.base_path, experiment_name)
        self.path_flock_result = '{}results/{}/flock_auc.csv'.format(self.base_path, experiment_name)
        #
        # self.path_cost_ig_test = 'application/conditions/test/income.csv'
        # self.path_cost_ig_expert = 'application/conditions/expert/income.csv'
        # self.path_budget_evaluation = '{}budget/{}/budget_evaluation.csv'.format(self.base_path, experiment_name)
        # self.path_cost_ig_base = '{}evaluation/income_base.csv'.format(self.base_path, experiment_name)
        self.path_budget_evaluation_base = '{}evaluation/base.csv'.format(self.base_path, experiment_name)
        self.path_budget_evaluation_cost = '{}evaluation/budget_evaluation_cost.csv'.format(self.base_path, experiment_name)
        self.path_budget_evaluation_nofeatures = '{}evaluation/budget_evaluation_nofeatures.csv'.format(self.base_path, experiment_name)
        self.path_budget_evaluation_cost_rawaucs = '{}evaluation/budget_evaluation_cost_rawaucs.pickle'.format(self.base_path, experiment_name)
        self.path_budget_evaluation_nofeatures_rawaucs = '{}evaluation/budget_evaluation_nofeatures_rawaucs.pickle'.format(self.base_path, experiment_name)

        self.path_final_evaluation_aggregated = '{}evaluation/final_evaluation_aggregated.pickle'.format(self.base_path)
        self.path_final_evaluation_combined = '{}evaluation/final_evaluation_combined.csv'.format(self.base_path)

        self.path_auc_plots = '{}evaluation/visualisation/{}_histograms_aucs.html'.format(self.base_path, self.dataset_name)
        self.path_descriptions_domain = '{}evaluation/experts_domain/income_description_domain.csv'.format(self.base_path)


        self.target = 'income==>50K'


    def preprocess_raw(self):
        """
        Selects only interesting features, fills gaps
        outputs a csv into "cleaned" folder
        :return:
        """
        df_raw = pd.read_csv(self.path_raw, quotechar='"', delimiter=',')
        df_raw.to_csv(self.path_cleaned, index=False)

    def bin_binarise(self):
        """
        binning and binarise
        outputs a csv into "cleaned" folder "_bin"
        :return:
        """
        df = pd.read_csv(self.path_cleaned)
        preparator = DataPreparator()
        df = preparator.prepare(df)
        df.to_csv(self.path_bin, index=False)

    def run(self):

        N_Features = range(3, 17, 2)
        n_samples = 100 # number of repetitions to calculate average auc score for samples)
        # experiment.set_up_basic_folder_structure()
        # experiment.set_up_experiment_folder_structure('experiment1')
        # experiment.preprocess_raw()
        # experiment.bin_binarise()
        # experiment.get_metadata()
        # experiment.evaluate_crowd_all_answers()
        # exit()
         # experiment.drop_analysis(N_Features, n_samples)
        #experiment.evaluate_flock(N_Features, n_samples, range(3, 100, 1))
        # experiment.evaluate_csfs_auc()

        # experiment.drop_analysis(N_Features, n_samples)
        # N_Features = [65, 80, 95, 116]
        # N_Features = [5, 17, 32, 50]
        # experiment.drop_evaluation(N_Features, n_samples)
        # experiment.evaluate_budget(budget_range)
        # df_budget_evaluation = pd.read_csv(experiment.path_budget_evaluation, index_col=0, header=[0, 1])
        # experiment.get_figure_budget_evaluation(df_budget_evaluation)
        # experiment.evaluate_ranking_cost(budget_range)
        # experiment.evaluate_ranking_nofeatures(N_Features)
        # experiment.autocorrelation()
        # experiment.final_evaluation()
        # experiment.final_evaluation_visualisation(feature_range=no_features)
        # experiment.crowd_answers_plot()
        # experiment.evaluate_csfs_auc()
        # experiment.final_evaluation()
        # experiment.final_evaluation_visualisation(feature_range)
        # experiment.crowd_answers_plot(auto_open=auto_open_plots)
        # experiment.final_evaluation_combine(feature_range, bootstrap_n=bootstrap_n, repetitions=repetitions)
        # experiment.crowd_auc_plot(auto_open=auto_open_plots)
        # experiment.statistical_comparison(feature_range)
        # experiment.evaluate_no_answers()
        # experiment.evaluate_no_answers_get_fig(feature_range)
        # experiment.evaluate_answers_delta()
        # self.evaluate_answers_delta_plot(auto_open=True)
        # self.humans_vs_actual_auc()
        # experiment.humans_vs_actual_auc_plot()
        # self.add_csfs_auc_to_human_vs_actual()

        #self.human_comparison_table(feature_slice=self.feature_slice)
        # experiment.evaluate_condition(ERCondition.RANDOM)
        # self.domain_feedback()
        self.domain_feedback_plot_ranking_counts()
        self.domain_feedback_plot_scores()
        self.domain_feedback_plot_actual_ig()

if __name__ == '__main__':
    experiment = ExperimentIncome('income', 1, 'experiment1')
    experiment.run()