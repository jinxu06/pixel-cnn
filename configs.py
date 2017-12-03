

configs = {}

## SVHN
configs["svhn-forward"] = {
    "data_dir": "/data/ziz/not-backed-up/jxu/SVHN",
    "save_dir": "/data/ziz/jxu/save-svhn-forward",
    #"save_dir": "/data/ziz/jxu/save-svhn-forward-less-epoch",
    "nr_filters": 100,
    "nr_resnet": 5,
    "data_set": "svhn",
    "batch_size": 6,
    "init_batch_size": 6,
}
configs["svhn-backward"] = {
    "data_dir": "/data/ziz/not-backed-up/jxu/SVHN",
    "save_dir": "/data/ziz/jxu/save-svhn-backward",
    "nr_filters": 100,
    "nr_resnet": 5,
    "data_set": "svhn",
    "batch_size": 6,
    "init_batch_size": 6,
    "masked": True,
    "rot180": True,
}
configs["svhn-backward-rename"] = {
    "data_dir": "/data/ziz/not-backed-up/jxu/SVHN",
    "save_dir": "/data/ziz/jxu/save-svhn-backward-rename",
    "nr_filters": 100,
    "nr_resnet": 5,
    "data_set": "svhn",
    "batch_size": 6,
    "init_batch_size": 6,
    "masked": True,
    "rot180": True,
}

## CelebA
configs["celeba-forward"] = {
    "data_dir": "/data/ziz/not-backed-up/jxu/CelebA",
    "save_dir": "/data/ziz/jxu/save-forward",
    "nr_filters": 160,
    "nr_resnet": 5,
    "data_set": "celeba",
    "batch_size": 6,
    "init_batch_size": 6,
}
configs["celeba-backward"] = {
    "data_dir": "/data/ziz/not-backed-up/jxu/CelebA",
    "save_dir": "/data/ziz/jxu/save-backward",
    "nr_filters": 160,
    "nr_resnet": 5,
    "data_set": "celeba",
    "batch_size": 6,
    "init_batch_size": 6,
    "masked": True,
    "rot180": True,
}
configs["celeba-backward-rename"] = {
    "data_dir": "/data/ziz/not-backed-up/jxu/CelebA",
    "save_dir": "/data/ziz/jxu/save-backward-rename",
    "nr_filters": 160,
    "nr_resnet": 5,
    "data_set": "celeba",
    "batch_size": 6,
    "init_batch_size": 6,
    "masked": True,
    "rot180": True,
}

configs["celeba-hr-backward"] = {
    "data_dir": "/data/ziz/not-backed-up/jxu/CelebA",
    "save_dir": "/data/ziz/jxu/save64-backward",
    "nr_filters": 100,
    "nr_resnet": 5,
    "data_set": "celeba",
    "batch_size": 6,
    "init_batch_size": 6,
    "masked": True,
    "rot180": True,
    "save_interval":5,
    "nr_gpu":7,
}
