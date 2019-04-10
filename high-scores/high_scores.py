class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        scores_length = len(self.scores)
        reverse_sorted_scores = sorted(self.scores, reverse=True)
        return reverse_sorted_scores[:3] if scores_length >= 3 else reverse_sorted_scores[:scores_length]
