class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        scores_length = len(self.scores)
        sorted_scores = sorted(self.scores)
        if len(self.scores) >= 3:
            return [sorted_scores[-1], sorted_scores[-2], sorted_scores[-3]]
        if scores_length == 1:
            return sorted_scores
        elif scores_length == 2:
            return [sorted_scores[-1], sorted_scores[-2]]
