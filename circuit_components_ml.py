from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import seaborn as sns
import skimage as ski
from skimage.color import rgb2gray
from skimage.feature import hog
import joblib

def plot_confusion_matrix(y_test, y_pred):
    acc = round(metrics.accuracy_score(y_test, y_pred), 2)
    cm = metrics.confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt=".0f")
    plt.xlabel('y_pred')
    plt.ylabel('y')
    plt.title('Accuracy Score: {0}'.format(acc), size=10)
    plt.show()


paths = ['battery', 'dc_volt_src', 'diode', 'gnd', 'inductor', 'resistor','voltmeter']
data_images =[]
categories = []
for path in paths:
    for i in range(1, 201):
        try:
            image = ski.io.imread(f'{path}/{i}.bmp')
            data = hog(image,pixels_per_cell=(8,8))
            data_images.append(data)
            categories.append(path)
        except FileNotFoundError:
            print(f"Dosya bulunamadı: {path}/{i}.bmp. Atlanıyor.")
            continue
        except ValueError:
            print("Dosya kanal sayisi fazla")
            image = ski.io.imread(f'{path}/{i}.bmp')
            data = rgb2gray(image)
            data = hog(data,pixels_per_cell=(8,8))
            data_images.append(data)
            categories.append(path)
            continue
        

X = data_images
y = categories
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=46)
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
y_pred = knn_model.predict(X_test)




# Eğitilmiş KNN modeli kaydetme
joblib.dump(knn_model, "knn_model_api.pkl")



accuracy = metrics.accuracy_score(y_test, y_pred)

plot_confusion_matrix(y_test, y_pred)

print(metrics.classification_report(y_test, y_pred))