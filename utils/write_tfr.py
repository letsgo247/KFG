import os
from tqdm import tqdm
import tensorflow as tf


def _bytes_feature(value):
    """Returns a bytes_list from a string / byte."""
    if isinstance(value, type(tf.constant(0))):
        value = value.numpy()
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))



def make_example(img_str):
    # Create a dictionary with features that may be relevant.
    feature = {'image/encoded': _bytes_feature(img_str)}

    return tf.train.Example(features=tf.train.Features(feature=feature))


def main(dataset_path, output_file):
    samples = []
    print("Reading data list...")
    for file in tqdm(os.listdir(dataset_path)):
        img_path = os.path.join(dataset_path, file)
        samples.append(img_path)
    
    # print(samples)
    # random.shuffle(samples)

    print("Writing tfrecord file...")
    with tf.io.TFRecordWriter(output_file) as writer:
        for img_path in tqdm(samples):
            tf_example = make_example(img_str=open(img_path, 'rb').read())
            writer.write(tf_example.SerializeToString())


# dataset_path = './Korean/AFAD_test'
# output_file = './Korean/AFAD.tfrecord'
dataset_path = './Foreigner/FFHQ_gathered'
output_file = './Foreigner/FFHQ.tfrecord'

main(dataset_path, output_file)