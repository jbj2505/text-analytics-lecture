from os.path import join
from global_utils import get_data_path
from sklearn.datasets import fetch_20newsgroups


def load_dataset(train_test_all):
    """Loads 20 News Groups data set."""

    # Creates path to file.
    data_home = get_data_path(join('raw', '20news-bydate_py3.pkz'))
    # The selection of categories is optional. If empty we will obtain samples from all categories
    categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
    # subset can be: train, test or all
    data_set = fetch_20newsgroups(subset=train_test_all, categories=categories, shuffle=True,
                                 random_state=42, download_if_missing=False, data_home=data_home)
    return data_set


def target_classes(dataset):
    # Classes in the dataset
    return dataset.target_names


def nr_samples(dataset):
    # Number of training samples:
    return len(dataset.data)


def sample_content(dataset, sample_pos):
    sample_pos -= 1  # Why -1? Because the vector starts counting at position 0

    return dataset.data[sample_pos]


def sample_class_pos(dataset, sample_pos):
    class_pos = dataset.target[sample_pos]

    return class_pos


def sample_class(dataset, class_pos):
    return dataset.target_names[class_pos]


def sample_filename(dataset, sample_pos):
    return dataset.filenames[sample_pos]
