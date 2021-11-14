import tensorflow as tf


def write_tfrecords(x, y, tfr_filename):
    writer = tf.io.TFRecordWriter(filename)

    for image, label in zip(x, y):
        example = tf.train.Example(features=tf.train.Features(
            feature={
                'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image.tobytes()])),
                'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
            }))
        writer.write(example.SerializeToString())

write_tfrecords(x_test, y_test, './data/validation/validation.tfrecords')

write_tfrecords(x_train, y_train, './data/train/train.tfrecords')