# Metric for 3D medical image segmentation
In 3D medical image segmentation, there are several metrics for evaluation. <br>
1. Overlap based metric : sensitivity, specificity, false positive rate, false negative rate, F-Measure, **Dice similarity coefficient**
, Jaccard index, and global consistency error
2. NCC volume based metric : volumetric similarity(registration between target and prediction is needed.)
3. Information Theory based metric : mutual information(MI), **varation of information(VOI)**
4. Probability based metric : interclass correlation(ICC), probabilistic distance(PBD), Cohens kappa, Area under ROC curve(AUC)
5. Spatial distance based metric : Hausdorff distance, **mean Hausdorff distance**, and Mahalanobis distance
6. Paircounting based metric : Rand index, **adjusted Rand index**
# Case study
1. For boundary accuracy : spatial distance based metric(Hausdorff distance), not volume based
2. For too small segment : Spatial distance based metric(Hausdorff distance), not overlap based
3. For complex boundary : mean Hausdorff distance
4. For detecting all true segment(despite false positive and false negative) : variation of information(VOI)
5. For outlier : Avoid hausdorff distance becaute this metric is so sensitive.
# Reference
[Review of Evaluation Metrics for 3D Medical Image Segmentation](https://www.ksiim.org/api/society/journal/download/292/3)%20ksiim%20%EA%B9%80%EC%9E%A5%EC%9A%B0.pdf)
