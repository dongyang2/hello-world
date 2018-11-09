# pipeline的例子

from sklearn import svm
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

print(__doc__)

# 制作数据
X, y = samples_generator.make_classification(
    n_features=20, n_informative=3, n_redundant=0, n_classes=4,
    n_clusters_per_class=2)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# ANOVA SVM-C
# 1) anova filter, take 3 best ranked features
anova_filter = SelectKBest(f_regression, k=3)  # anova应该就是选前三的意思吧-_=
# 2) svm
clf = svm.SVC(kernel='linear')

# 下面这句话相当于简化了pipeline函数的使用，直接传入模型类而不需要为每个step命名
# 等同于
# from sklearn.pipeline import Pipeline
# pipe = Pipeline(steps=[('select3Best', anova_filter), ('linear_svc', clf)])
anova_svm = make_pipeline(anova_filter, clf)
anova_svm.fit(X_train, y_train)
y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
