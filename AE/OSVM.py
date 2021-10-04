import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm
from sklearn import metrics 
from sklearn import preprocessing
import tensorflow as tf
from sklearn.model_selection import train_test_split
from functools import partial
import sys
import math




bad=open("C:/Users/SKsaqlain/Desktop/AE/output1.txt",'r')
good=open("C:/Users/SKsaqlain/Desktop/AE/output2.txt",'r')

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

bad_y=[-1]*len(bad_processed)
good_y=[1]*len(good_processed)
good_processed_v=list()

#print(preprocessing.normalize((np.asarray(ele)), norm='l2').tolist()[0])
for ele in good_processed:
    good_processed_v.append(preprocessing.normalize((np.asarray([ele])), norm='l2').tolist()[0])
good_processed=good_processed_v

bad_processed_v=list()
for ele in bad_processed:
    bad_processed_v.append(preprocessing.normalize((np.asarray([ele])), norm='l2').tolist()[0])
bad_processed=bad_processed_v

data_set=bad_processed+good_processed
target=bad_y+good_y


X_train, X_test, y_train, y_test = train_test_split(good_processed, good_y, test_size=0.0, random_state=58)
print("training",len(X_test),len(X_train))

X_train_bad, X_test_bad, y_train_bad, y_test_bad= train_test_split(bad_processed, bad_y, test_size=0.45, random_state=58)
print("testing",len(X_train_bad),len(X_test_bad))



n_inputs = 45
n_hidden1 = 20
n_hidden2 = 10  # codings
n_hidden3 = n_hidden1
n_outputs = n_inputs

learning_rate = 0.01
l2_reg = 0.0001

X = tf.placeholder(tf.float32, shape=[None, n_inputs])

he_init = tf.contrib.layers.variance_scaling_initializer() # He initialization
#Equivalent to:
#he_init = lambda shape, dtype=tf.float32: tf.truncated_normal(shape, 0., stddev=np.sqrt(2/shape[0]))
l2_regularizer = tf.contrib.layers.l2_regularizer(l2_reg)
my_dense_layer = partial(tf.layers.dense,
                         activation=tf.nn.elu,
                         kernel_initializer=he_init,
                         kernel_regularizer=l2_regularizer)

hidden1 = my_dense_layer(X, n_hidden1)
hidden2 = my_dense_layer(hidden1, n_hidden2)
hidden3 = my_dense_layer(hidden2, n_hidden3)
outputs = my_dense_layer(hidden3, n_outputs, activation=None)

reconstruction_loss = tf.reduce_mean(tf.square(outputs - X))

reg_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
loss = tf.add_n([reconstruction_loss] + reg_losses)

optimizer = tf.train.AdamOptimizer(learning_rate)
training_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()
saver = tf.train.Saver() # not shown in the book

phi=-1#hyper parameters
beta=1
n_epochs = 100
batch_size = 50
output_val=np.empty(shape=[0,0])
with tf.Session() as sess:
    init.run()
    global phi
    global beta
    for epoch in range(n_epochs):
        n_batches = len(X_train) // batch_size
        i=0
        for iteration in range(n_batches):
            print("\r{}%".format(100 * iteration // n_batches), end="") # not shown in the book
            sys.stdout.flush()
            try:                                          # not shown
            	X_batch=X_train[i:(i+batch_size)][:]
            except:
            	X_batch=X_train[i:][:]
            i=i+batch_size

            sess.run(training_op, feed_dict={X: X_batch})
        loss_train = reconstruction_loss.eval(feed_dict={X: X_batch})# not shown
        if(loss_train<=phi):
            phi=loss_train
        beta=loss_train/phi
        print("\r{}".format(epoch), "Train MSE:", loss_train)     
    
    X_train=outputs.eval(feed_dict={X:X_train})
    X_train_bad=outputs.eval(feed_dict={X:X_train_bad})
    X_test_bad=outputs.eval(feed_dict={X:X_test_bad})
    # fit the model
    clf = svm.OneClassSVM(nu=0.25, kernel="rbf", gamma=0.1)
    clf.fit(X_train)
    y_pred_train = clf.predict(X_train)
    y_pred_test = clf.predict(X_train_bad)
    y_pred_ran=clf.predict(X_test_bad)
    #y_pred_outliers = clf.predict(X_train_bad)
    n_error_train = y_pred_train[y_pred_train == -1].size
    n_error_test = y_pred_test[y_pred_test == -1].size
    n_error_ran=y_pred_ran[y_pred_ran==-1].size
    
    #n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
    
    print(len(X_train),n_error_train)
    print(len(X_train_bad),n_error_test)
    print(len(X_test_bad),n_error_ran)
    y=clf.predict(data_set)
    print("accuracy: ", metrics.accuracy_score(target,y))
    
#print(n_error_outliers