from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

email_data = pd.DataFrame({
    'ExMarks': [2,1,4,5,2,3,0,6,1,5],
    'Uppercase': [1,2,3,4,1,5,1,2,0,5],
    'Spam': [0,0,1,1,0,1,0,1,0,1]
})
X = email_data[['ExMarks', 'Uppercase']].values
y = email_data['Spam'].values

svm_linear = SVC(kernel='linear').fit(X, y)
svm_rbf = SVC(kernel='rbf').fit(X, y)

example = np.array([[3, 3]])
pred_linear = svm_linear.predict(example)[0]
pred_rbf = svm_rbf.predict(example)[0]
print("\nSVM Predictions for (3, 3):")
print("Linear Kernel:", "Spam" if pred_linear == 1 else "Not Spam")
print("RBF Kernel:", "Spam" if pred_rbf == 1 else "Not Spam")

# Plot decision boundaries
xx, yy = np.meshgrid(np.linspace(0, 7, 200), np.linspace(0, 7, 200))
grid = np.c_[xx.ravel(), yy.ravel()]
Z_linear = svm_linear.predict(grid).reshape(xx.shape)
Z_rbf = svm_rbf.predict(grid).reshape(xx.shape)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.contourf(xx, yy, Z_linear, alpha=0.3, cmap='coolwarm')
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette='Set1')
plt.title("SVM with Linear Kernel")

plt.subplot(1, 2, 2)
plt.contourf(xx, yy, Z_rbf, alpha=0.3, cmap='coolwarm')
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette='Set1')
plt.title("SVM with RBF Kernel")
plt.tight_layout()
plt.show()