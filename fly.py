import tensorflow as tf
import numpy as np

def str2numpy(s):
    return np.array([[(1 if t == '*' else 0) for t in tt]
                     for tt in s.split('\n')[1:-1]], dtype=np.float32)

def make_glider():
    f = '''
*                                  
                                   
             *                     
              *                    
            ***                    
                                   
                                   
'''
    return str2numpy(f)

def create_glider_graph():
    graph = tf.Graph()
    with graph.as_default():
        field = tf.placeholder(dtype=tf.float32)
        conv_mask = tf.constant([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=tf.float32)
        conv_mask = tf.reshape(conv_mask, (3, 3, 1, 1))
        p_ext_field = tf.concat([field[-1:0, :], field, field[0:1, :]], axis=0)
        q_ext_field = tf.concat([p_ext_field[:, -1:0], p_ext_field, p_ext_field[:, 0:1]], axis=1)
        fsh = tf.shape(q_ext_field)
        nhwc_ext_field = tf.reshape(q_ext_field, (1, fsh[0], fsh[1], 1))
        neighbours = tf.nn.conv2d(input=nhwc_ext_field, filter=conv_mask, strides=[1, 1, 1, 1], padding='SAME')
        result = tf.reshape(neighbours, fsh)[:-1, :-1]
        # result = nhwc_ext_field
    return graph, field, result

def main():
    input = make_glider()
    print(input.shape)
    graph, field, result = create_glider_graph()
    with tf.Session(graph=graph) as sess:
        ans = sess.run(result, {field: input})
    print(ans.shape)
    print(ans.astype(np.uint8))

if __name__ == '__main__':
    main()
