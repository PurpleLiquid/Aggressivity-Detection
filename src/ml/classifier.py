from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# SVC
# used to measure and predict TF-idf ngrams
def svm_classifier(train_x, test_x, train_y, test_y):
    SVM = LinearSVC(C=1)
    SVM.fit(train_x, train_y)

    predictions_SVM = SVM.predict(test_x)
    print("SVM F1 Score -> ",f1_score(predictions_SVM, test_y, pos_label=4)*100)
    print("SVM Precision Score -> ",precision_score(predictions_SVM, test_y, pos_label=4)*100)
    print("SVM Recall Score -> ",recall_score(predictions_SVM, test_y, pos_label=4)*100)
    print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, test_y)*100)

def sgd_classifier(train_x, test_x, train_y, test_y):
    sgd = SGDClassifier(loss="log", penalty="l2")
    sgd.fit(train_x, train_y)

    predictions_SGD = sgd.predict(test_x)
    print("SGD F1 Score -> ",f1_score(predictions_SGD, test_y, pos_label=4)*100)
    print("SGD Precision Score -> ",precision_score(predictions_SGD, test_y, pos_label=4)*100)
    print("SGD Recall Score -> ",recall_score(predictions_SGD, test_y, pos_label=4)*100)
    print("SGD Accuracy Score -> ",accuracy_score(predictions_SGD, test_y)*100)
