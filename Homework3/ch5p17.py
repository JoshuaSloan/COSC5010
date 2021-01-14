import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix 

y = np.array([2,2,1,1,2,2,1,1,2,1])
M1 = np.array([0.73,0.69,0.44,0.55,0.67,0.47,0.08,0.15,0.45,0.35])
M2 = np.array([0.61,0.03,0.68,0.31,0.45,0.09,0.38,0.05,0.01,0.04])
fpr1, tpr1, thresholds1 = metrics.roc_curve(y, M1, pos_label=2)
fpr2, tpr2, thresholds2 = metrics.roc_curve(y, M2, pos_label=2)

plt.figure()
lw = 1.5
plt.plot(fpr1, tpr1, color='blue', lw=lw, label = "M1")
plt.plot(fpr2, tpr2, color='red', lw=lw, label = "M2")
plt.plot([0, 1], [0, 1], color='grey', lw=lw, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves for Posterior Probabilities')
plt.legend(loc="lower right")
plt.show()

t1 = 0.5
t2 = 0.1
t_test = [t1,t2]
models = [M1,M2]
for t_val in t_test:
    for model in models:    
        pred_y = []
        for instance in model:
            if(instance > t_val):
                pred_y.append(2)
            else:
                pred_y.append(1)
                
        TN, FP, FN, TP = confusion_matrix(y, pred_y).ravel() 
        
        print("Model 1" if np.array_equal(model,M1) else "Model 2","at threshold",t_val)
        cMat = np.array([[TP,FP],[FN,TN]])
        precision = TP/(TP+FP)
        recall = TP/(TP+FN)
        f_measure = 2*TP/(2*TP+FP+FN)
        FPR = FP/(FP+TN)
        print("Confusion Matrix:")
        print(cMat)
        print("Precision:",precision)
        print("Recall:",recall)
        print("F-measure:",f_measure)
        print("False Positive Rate:",FPR)
        print()
