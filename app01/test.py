import numpy as np
import tensorflow as tf

x = [[6025,36300625,1401,8441025,1962801],
 [6540,42771600,1401,9162540,1962801],
 [7054,49758916,1401,9882654,1962801],
 [6934,48080356,1134,7863156,1285956]]
y = [[250],[300],[350],[300]]
# y = [11,12.5,20,18]
x_pred = [[6025,36300625,1401,8441025,1962801]]

tf_x = tf.placeholder(tf.float32, [None,5])     # input x
tf_y = tf.placeholder(tf.float32, [None,1])     # input y

# neural network layers
l1 = tf.layers.dense(tf_x, 20, tf.nn.relu)          # hidden layer
output = tf.layers.dense(l1, 1)                     # output layer

loss = tf.losses.mean_squared_error(tf_y, output)   # compute cost
optimizer = tf.train.AdamOptimizer(learning_rate=0.1)
train_op = optimizer.minimize(loss)

sess = tf.Session()                                 # control training and others
sess.run(tf.global_variables_initializer())         # initialize var in graph


for step in range(30000):
    # train and net output
    _, l, pred = sess.run([train_op, loss, output], {tf_x: x, tf_y: y})
    if step % 10 == 0:
        print('loss is: ' + str(l))
        # print('prediction is:' + str(pred))

output_pred = sess.run(output,{tf_x:x_pred})
print('input is:' + str(x_pred[0][:]))
print('output is:' + str(output_pred[0][0]))
