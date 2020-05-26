import tensorflow as tf

x1 = tf.constant(5)                  
x2 = tf.constant(6)                       # Model

result = tf.multiply(x1, x2)

print(result)


 
with tf.Session() as sess:
    output = sess.run(result)             # Session
    print(output)
    
print(output)
