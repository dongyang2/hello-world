# dropout具体实现
# Python 3

import numpy as np


def dropout(x, drop_proba):
    return x*np.random.choice(
        [0, 1],
        x.shape,
        p=[drop_proba, 1-drop_proba]
    )/(1.-drop_proba)


def main():
    # x = np.random.random((10, 100))                  # 模拟一个batch_size=10、维度为100的输入
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    np.random.seed(2018)

    print(dropout(x, 0.6))


if __name__ == "__main__":
    main()
