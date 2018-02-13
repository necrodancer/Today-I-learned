# Dataset
Dataset can be separated into  three types:
1. Training set
2. Validation set
3. Test set
# Training set
Training set is to train parameters of neural networks(NN). 
# Validation set
Some of (usually 10% of) training set is to validate trained parameter.<br>
It does not participate in training, just evaluating accuray of NN.
# Test set
The unseen dataset(unlike validation set). Once NN is considered ready to predict sth, test set is used in practical or to show its generalized performance.
# Cross validation
Fold train set such as n-fold(n = 3,4, ...).<br>
Only one fold is used as validation set, and the other set is used for training.
Once training and validation is done, prepare untrained parameters, and use another fold as validation set and the other folds as training set.<br>
Repeat for every fold.<br>
Finally, the average of accuracies of n NNs represents NN's performance.<br>
The reason why to do cross validation is to avoid data unbalance.<br>
One more thing, cross validation needs a lot of computations, so it is proper to small amounts of dataset.
# Further works
1. To implement cross validation.
