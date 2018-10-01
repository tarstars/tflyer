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
         *                    *      
          *                 ***      
        ***                          
                                     
                                     
                                     
                                     
'''
    return str2numpy(f)

def create_glider_graph():
    graph = tf.Graph()
    with graph.as_default():
        field = tf.placeholder(dtype=tf.float32)
        fsh = tf.shape(field)
        n_field = field - 0.5
        conv_mask = tf.constant([[1, 1, 1], [1, 0, 1], [1, 1, 1]],
                                dtype=tf.float32)
        conv_mask = tf.reshape(conv_mask, (3, 3, 1, 1))
        p_ext_field = tf.concat([field[-1:, :], field, field[:1, :]], axis=0)
        q_ext_field = tf.concat([p_ext_field[:, -1:], p_ext_field,
                                 p_ext_field[:, :1]],
                                axis=1)
        efsh = tf.shape(q_ext_field)
        nhwc_ext_field = tf.reshape(q_ext_field, (1, efsh[0], efsh[1], 1))
        neighbours = tf.nn.conv2d(input=nhwc_ext_field, filter=conv_mask,
                                  strides=[1, 1, 1, 1], padding='SAME')
        cycle_nei = neighbours[0, 1:-1, 1:-1, 0]
        stay_mask = tf.nn.relu(1.5 - (tf.nn.relu(cycle_nei - 1.5) +
                                      tf.nn.relu(2.5 - cycle_nei)))
        born_mask = tf.nn.relu(1.5 - (tf.nn.relu(cycle_nei - 2.5) +
                                      tf.nn.relu(3.5 - cycle_nei)))
        new_field = tf.sign(tf.nn.relu(tf.multiply(n_field, stay_mask)) +
                            born_mask)
        result = new_field
    return graph, field, result

def main():
    input = make_glider()
    graph, field, result = create_glider_graph()
    with tf.Session(graph=graph) as sess:
        for _ in range(1000):
            ans = sess.run(result, {field: input})
            print(numpy2str(ans.astype(np.uint8)))
            time.sleep(0.05)
            print('\033[2J')
            input = ans

if __name__ == '__main__':
    main()
