import time

import numpy as np
import tensorflow as tf

def str2numpy(s):
    return np.array([[(1 if t == '*' else 0) for t in tt]
                     for tt in s.split('\n')[1:-1]], dtype=np.float32)

def numpy2str(a):
    return '\n'.join((''.join('*' if t > 0.5 else ' ' for t in tt)
                               for tt in a))

def make_glider():
    f = '''
                                     
                                     
                                     
                                     
                                     
                                     
             *                       
              *                      
            ***                      
                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                     
'''
    return str2numpy(f)

def create_one_step_graph():
    ''' It is not full solution yet, but the simple and effective way
    to show that there is an exact solution among neural networks.
    This graph contains only typical for neural networks operations:
    plus, minus, multiplication and relu. Nevertheless, it allows us
    to perform one step of Convey's life game. Glider moving through
    the rectangular field allows us to test in the simple and efficient
    way that it is OK with all corner cases.
    '''
    graph = tf.Graph()
    with graph.as_default():
        field = tf.placeholder(dtype=tf.float32)
        n_field = tf.expand_dims(field - 0.5, 0)
        n_field = tf.expand_dims(n_field, 3)
        conv_mask = tf.constant([[1, 1, 1],
                                 [1, 0, 1],
                                 [1, 1, 1]], dtype=tf.float32)
        conv_mask = tf.expand_dims(conv_mask, 2)
        conv_mask = tf.expand_dims(conv_mask, 3)

        p_field = tf.concat([field[-1:, :], field, field[:1, :]], axis=0)
        pq_field = tf.concat([p_field[:, -1:], p_field, p_field[:, :1]], axis=1)
        ext_field = tf.expand_dims(pq_field, 2)
        ext_field = tf.expand_dims(ext_field, 0)

        neis = tf.nn.conv2d(input=ext_field, filter=conv_mask,
                            strides=[1, 1, 1, 1], padding='VALID')
        stay_mask = tf.nn.relu(1.5 - (tf.nn.relu(neis - 1.5) +
                                      tf.nn.relu(2.5 - neis)))
        born_mask = tf.nn.relu(1.5 - (tf.nn.relu(neis - 2.5) +
                                      tf.nn.relu(3.5 - neis)))
        next_field = tf.sign(tf.nn.relu(tf.multiply(n_field, stay_mask))
                             + born_mask)
    return graph, field, next_field[0, :, :, 0]

def main():
    input = make_glider()
    graph, field, next_field = create_one_step_graph()
    with tf.Session(graph=graph) as sess:
        for _ in range(1000):
            ans = sess.run(next_field, {field: input})
            print(numpy2str(ans.astype(np.uint8)))
            time.sleep(0.01)
            print('\033[2J')
            input = ans

if __name__ == '__main__':
    main()
