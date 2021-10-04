import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from sklearn import preprocessing
import sys

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

bad_y=[1]*len(bad_processed)
good_y=[0]*len(good_processed)
good_processed_v=list()
for ele in good_processed:
    good_processed_v.append(preprocessing.normalize((np.asarray([ele])), norm='l2').tolist()[0])
good_processed=good_processed_v

bad_processed_v=list()
for ele in bad_processed:
    bad_processed_v.append(preprocessing.normalize((np.asarray([ele])), norm='l2').tolist()[0])
bad_processed=bad_processed_v


def rms(v1,v2):
    err=0
    for i in range(len(v1)):
        err=err+(v1[i]-v2[i])**2
    return (err/len(v1))**0.5

X_train, X_test, y_train, y_test = train_test_split(good_processed, good_y, test_size=0.10, random_state=58)
print(len(X_test),len(X_train))


dataset=X_test+bad_processed
labels=[1]*len(X_test)+[0]*len(bad_processed)
#test_data_tr,test_data_tt,test,y_tr,y_tt=train_test_split(dataset,labels, test_size=0.01, random_state=58)

# Training Parameters
learning_rate = 0.001
n_epochs = 70
batch_size = 50
# Network Parameters
num_hidden_1 =27 # 1st layer 
num_hidden_2 = 10 # 2nd layer 
num_input = 45 #input vector


X = tf.placeholder("float", [None, num_input])

weights = {
    'encoder_h1': tf.Variable(tf.random_normal([num_input, num_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([num_hidden_1, num_hidden_2])),
    'decoder_h1': tf.Variable(tf.random_normal([num_hidden_2, num_hidden_1])),
    'decoder_h2': tf.Variable(tf.random_normal([num_hidden_1, num_input])),
}
biases = {
    'encoder_b1': tf.Variable(tf.random_normal([num_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([num_hidden_2])),
    'decoder_b1': tf.Variable(tf.random_normal([num_hidden_1])),
    'decoder_b2': tf.Variable(tf.random_normal([num_input])),
}

# Building the encoder
def encoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),
                                   biases['encoder_b1']))
    # Encoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                   biases['encoder_b2']))
    return layer_2


# Building the decoder
def decoder(x):
    # Decoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']),
                                   biases['decoder_b1']))
    # Decoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']),
                                   biases['decoder_b2']))
    return layer_2

# Construct model
encoder_op = encoder(X)
decoder_op = decoder(encoder_op)

# Prediction
y_pred = decoder_op
# Targets (Labels) are the input data.
y_true = X

# Define loss and optimizer, minimize the squared error
reconstruction_loss = tf.reduce_mean(tf.pow(y_true - y_pred, 2))

reconstruction_loss_2=tf.reduce_mean(tf.pow(y_true-y_pred,2),1)


reg_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
loss = tf.add_n([reconstruction_loss] + reg_losses)
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(loss)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start Training
# Start a new TF session
beta=-1
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Training
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

            sess.run(optimizer, feed_dict={X: X_batch})
            l2=reconstruction_loss_2.eval(feed_dict={X:X_batch})
            for ele in l2:
                if(ele>beta):
                    beta=ele
            

        loss_train = reconstruction_loss.eval(feed_dict={X: X_batch})   # not shown
        print("\r{}".format(epoch), "Train MSE:", loss_train)
    output=sess.run(decoder_op,feed_dict={X:dataset})
    #test_output=reconstruction_loss_2.eval(feed_dict={X:dataset})
    count=0
    l=[]
    for i in range(len(output)):
        err=rms(output[i],dataset[i])
        if(err > 0.10*beta):
            l.append(0)
        else:
            l.append(1)
    tn, fp, fn, tp = confusion_matrix(labels,l).ravel() 
    print("[tn %s,fp %s, fn %s,tp %s]"%(tn, fp, fn, tp))
    #print("confusion matrix ",cm)
    for i in range(len(l)):
        if(l[i]==labels[i]):
            count+=1
    print(count/len(l))

     