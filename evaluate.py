#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import numpy 
import argparse
import pdb

from scipy.optimize import brentq
from sklearn.metrics import roc_curve
from scipy.interpolate import interp1d

# ==================== === ====================

parser = argparse.ArgumentParser(description = "VoxSRC");

parser.add_argument('--ground_truth', type=str, default='data/veri_test.txt', help='Ground truth file');
parser.add_argument('--prediction', type=str, default='data/veri_test_output.txt', help='Prediction file');
parser.add_argument('--positive', type=int, default=1, help='1 if higher is positive; 0 is lower is positive');

opt = parser.parse_args();

# ==================== === ====================

def calculate_eer(y, y_score, pos):
# y denotes groundtruth scores,
# y_score denotes the prediction scores.

	fpr, tpr, thresholds = roc_curve(y, y_score, pos_label=pos)
	eer = brentq(lambda x : 1. - x - interp1d(fpr, tpr)(x), 0., 1.)
	thresh = interp1d(fpr, thresholds)(eer)

	return eer, thresh

# ==================== === ====================

def read_score(filename):
	with open(filename) as f:
	    scores = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	scores = [float(x.split()[0]) for x in scores] 

	return scores

# ==================== === ====================

y = read_score(opt.ground_truth)
y_score = read_score(opt.prediction)

eer, thresh = calculate_eer(y,y_score,opt.positive)

print('EER : %.3f%%'%(eer*100))