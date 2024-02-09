import submission, util
import re
from collections import defaultdict

# Read in examples
trainExamples = util.readExamples('names.train')
devExamples = util.readExamples('names.dev')


def featureExtractor(x):  # phi(x)
    # x = "took Mauritius into"
    phi = defaultdict(float)
    tokens = x.split()
    left, entity, right = tokens[0], " ".join(tokens[1:-1]), tokens[-1]
    phi['entity is ' + entity] = 1
    phi['left is ' + left] = 1
    phi['right is ' + right] = 1
    return phi

# Learn a predictor

weights = submission.learnPredictor(trainExamples, devExamples, featureExtractor,10, 0.1)
util.outputWeights(weights, 'weights')
util.outputErrorAnalysis(devExamples, featureExtractor, weights, 'error-analysis')

# Test!!!
testExamples = util.readExamples('names.test')
predictor = lambda x : 1 if util.dotProduct(featureExtractor(x), weights) > 0 else -1
print('test error =', util.evaluatePredictor(testExamples, predictor))
