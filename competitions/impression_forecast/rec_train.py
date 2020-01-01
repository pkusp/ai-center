# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: rec_train.py
@time: 2020/1/1 10:02 PM

这一行开始写关于本文件的说明与解释
"""

from competitions.impression_forecast.rec_model import rec_model
from competitions.impression_forecast.rec_feat_gen import MovieRankDataset
from torch.utils.data import DataLoader
import torch
import torch.optim as optim
import torch.nn as nn
# from tensorboardX import SummaryWriter

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def train(model, num_epochs=5, lr=0.0001):
    loss_function = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    datasets = MovieRankDataset()

    for d in datasets:
        print(d)

    dataloader = DataLoader(datasets, batch_size=1, shuffle=True)

    losses = []
    # writer = SummaryWriter()
    for epoch in range(num_epochs):
        loss_all = 0
        for i_batch, sample_batch in enumerate(dataloader):

            # user_inputs = sample_batch['user_inputs']
            cust_inputs = sample_batch['cust_inputs']
            target = sample_batch['target'].to(device)

            model.zero_grad()

            tag_rank, _, _ = model(cust_inputs)

            loss = loss_function(tag_rank, target)
            if i_batch % 20 == 0:
                # writer.add_scalar('data/loss', loss, i_batch * 20)
                print(loss)

            loss_all += loss
            loss.backward()
            optimizer.step()
        print('Epoch {}:\t loss:{}'.format(epoch, loss_all))
    # writer.export_scalars_to_json("./test.json")
    # writer.close()


if __name__ == '__main__':
    model = rec_model()
    print(device)
    model = model.to(device)

    # train model
    train(model=model,num_epochs=1)
    # torch.save(model.state_dict(), 'Params/model_params.pkl')

    # get user and movie feature
    # model.load_state_dict(torch.load('Params/model_params.pkl'))
    # from recInterface import saveMovieAndUserFeature
    #
    # saveMovieAndUserFeature(model=model)

    # test recsys
    # from recInterface import getKNNitem,getUserMostLike
    # print(getKNNitem(itemID=100,K=10))
    # print(getUserMostLike(uid=100))
