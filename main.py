#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    @version: V-17-5-2
    @author: Linlifang
    @file: main.py
    @time: 17-5-2.下午1:36
"""
from api.crf_model import CRFModel


def train():
    # 训练模型
    crf_model = CRFModel(model='model/model111')
    crf_model.crf_learn(filename='data/train_file_1')


def test():
    crf_model = CRFModel(model='model/model2')
    a = '兄弟姐妹7人，现有1兄1姐健在,家族中无传染病及遗传病史'
    data = crf_model.crf_test(tag_data=a)
    print(data)
    # raw_data = []
    # result_data = []
    # # 获取数据
    # with open('data/test.data', 'r') as fp:
    #     for line in fp.readlines():
    #         raw_data.append(line.strip())
    # # 训练
    # for kk in raw_data:
    #     data = crf_model.crf_test(tag_data=kk)
    #     result_data.append('<@>'.join([kk, data]))
    #
    # # 保存数据
    # with open('output/output.data', 'w') as fp:
    #     fp.write('\n'.join(result_data))


def main(is_training=True):
    if is_training:
        train()
    else:
        test()


if __name__ == '__main__':
    main(is_training=False)
