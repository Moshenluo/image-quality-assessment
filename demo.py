from __future__ import print_function, division
import os
import csv
import torch
import numpy as np
import option
from torch.utils.data import Dataset, DataLoader
from dataset import AVADataset
from tqdm import tqdm
import argparse
import train_nni
opt = option.init()
device = torch.device("cuda")

def create_data_part(opt):
    test_csv_path = os.path.join(r'C:\Users\17168\Desktop\TAD66K\TAD66K', 'S1.csv')
    test_ds = AVADataset(test_csv_path,r'C:\Users\17168\Desktop\images\download_images\S1', if_train = False)
    test_loader = DataLoader(test_ds, batch_size=20, num_workers=0, shuffle=False)
    return test_loader
def validate(opt,model, loader):
    model.eval()

    torch.set_printoptions(precision=3)

    pred_score = []
    for idx, x in enumerate(tqdm(loader)):
        x = x.type(torch.FloatTensor).to(device)
        y_pred = model(x)
        pscore_np = y_pred.data.cpu().numpy().astype('float')
        pred_score += pscore_np.mean(axis=1).tolist()
    pred_score = np.array(pred_score)
    return pred_score

def start_demo(opt,csv_path):
    dataloader_test = create_data_part(opt)
    model = train_nni.TANet()
    model.load_state_dict(torch.load(r'C:\Users\17168\Desktop\TAD66K\TAD66K\SRCC_513_LCC_531_MSE_016.pth', map_location='cuda:0'))
    model = model.to(device)

    pred_score = validate(opt, model=model, loader=dataloader_test)
    pred_score *= 10  

    with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        rows[0].insert(1, 'score')
        for i in range(len(pred_score)):
            rows[i+1].insert(1, str(pred_score[i]))  

    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



if __name__ == '__main__':
    csv_path = 'S1.csv'
    start_demo(opt, csv_path)