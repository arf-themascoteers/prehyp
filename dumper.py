import numpy as np
from sklearn.preprocessing import MinMaxScaler
import scipy.io as sio
import pandas as pd


def dump(X_file,gt_file,dump_file,X_key,gt_key):
    X_img = sio.loadmat(X_file)
    gt_img = sio.loadmat(gt_file)
    X = X_img.get(X_key).astype('float64')
    gt = gt_img.get(gt_key).astype('float64')

    X = X.reshape(X.shape[0] * X.shape[1], X.shape[2])
    gt = gt.reshape(-1)

    # mask = (gt!=0)
    #
    # gt = gt[mask]
    # X = X[mask]

    #scaler = MinMaxScaler()
    #X = scaler.fit_transform(X)

    columns = [str(i) for i in range(X.shape[1])] + ["class"]
    data = np.concatenate((X,gt.reshape(-1,1)), axis=1)
    df = pd.DataFrame(columns=columns, data=data)
    # mapping = {v: i for i, v in enumerate(sorted(df["class"].unique()))}
    # df["class"] = df["class"].map(mapping)
    mapping = ""
    df.to_csv(dump_file, index=False)
    return mapping