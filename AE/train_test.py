import data_process_2
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
from sklearn import decomposition
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier

bad=open("output1.txt",'r')
good=open("output2.txt",'r')

bad_processed=list()
good_processed=list()
count=0
for line in bad:
	line=[int(ele) for ele in line.rstrip("\n").split(",")]
	bad_processed.append(line)
	count+=1
	# print(line)
for line in good:
	line=[int(ele) for ele in line.rstrip("\n").split(",")]
	good_processed.append(line)
	count-=1
	if(count==0):
		break

bad_y=[1]*len(bad_processed)
good_y=[0]*len(good_processed)

data_set=good_processed+bad_processed
y=good_y+bad_y
# plt.hist(data_set[1])
# plt.show()

fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()

pca=decomposition.PCA(n_components=3)
pca.fit(data_set)
bla_bla=pca.transform(data_set)
#bla_bla=np.matrix(bla_bla)
x_list=[ele[0] for ele in bla_bla]
y_list=[ele[1] for ele in bla_bla]
z_list=[ele[2] for ele in bla_bla]
# plt.scatter(x_list,y_list,z_list)
# plt.show()

# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
plt.scatter(x_list, y_list, z_list, c=y,
           edgecolor='k')

plt.show()

# rescaledX = Normalizer.fit(data_set)
normalisedX=scale(data_set,axis=0)
# print(normalisedX[0])

X_train, X_test, y_train, y_test = train_test_split(normalisedX, y, test_size=0.45, random_state=58)
print(len(X_test),len(X_train))

clf = SVC()
clf.fit(X_train, y_train)
y_pred=clf.predict(X_test)
# for i in range(len(y_test)):
	# print(y_test[i],y_pred[i])
n_correct = sum(y_pred == y_test)
print(n_correct / len(y_pred)) 

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train,y_train)
y_pred=neigh.predict(X_test)    
n_correct = sum(y_pred == y_test)
print(n_correct / len(y_pred)) 