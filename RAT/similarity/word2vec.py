from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
import os
import logging
import multiprocessing
import numpy as np
from RAT.similarity.text_preprocessing import unpickle_this


def make_model(post_data, size_=300, window_=2, min_count_=2, epochs_=1):
    cores = multiprocessing.cpu_count()

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    model = Word2Vec(size=size_, window=window_, min_count=min_count_, workers=cores-1)
    model.build_vocab(post_data)
    model.train(post_data, total_examples=len(post_data), epochs=epochs_)

    return model


def save_model(file_name, model):
    path = get_tmpfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/' + file_name + '.model'))
    model.save(path)


def load_model(file_name):
    path = get_tmpfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/' + file_name + '.model'))
    return Word2Vec.load(path)


def cos_sim(a, b):
    a = np.squeeze(a)
    b = np.squeeze(b)

    angle = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    if np.isnan(angle):
        return 0
    else:
        return angle


# post_data = unpickle_this('')
# my_model = make_model(post_data, size_=300, window_=2, min_count_=2, epochs_=1)
#
# save_model('', my_model)


# print(model.wv.similarity('', ''))

# for i in my_model.wv.most_similar(positive=[''], topn=100):
#     print(i)
