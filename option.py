import argparse

def init():
    parser = argparse.ArgumentParser(description="PyTorch")
    parser.add_argument('--path_to_images', type=str, default="C:/Users/17168/Desktop/data/TAD66K",
                        help='directory to images')
    parser.add_argument('--path_to_save_csv', type=str,default="C:/Users/17168/Desktop/data/labels/unmerge",
                        help='directory to csv_folder')
    parser.add_argument('--experiment_dir_name', type=str, default='.',
                        help='directory to project')
    parser.add_argument('--path_to_model_weight', type=str, default='C:/Users/17168/Desktop/TAD66K/TAD66K/SRCC_513_LCC_531_MSE_016.pth',
                        help='directory to pretrain model')
    parser.add_argument('--init_lr_res365_last', type=int, default=0.0003, help='learning_rate')
    parser.add_argument('--init_lr_mobileNet', type=int, default=0.0003, help='learning_rate')
    parser.add_argument('--init_lr_head', type=int, default=0.0003, help='learning_rate')
    parser.add_argument('--init_lr_head_rgb', type=int, default=0.0003, help='learning_rate')
    parser.add_argument('--init_lr_hypernet', type=int, default=0.0003, help='learning_rate')
    parser.add_argument('--init_lr_tygertnet', type=int, default=0.0003, help='learning_rate')
    parser.add_argument('--init_lr', type=int, default=0.0003, help='learning_rate')
    parser.add_argument('--num_epoch', type=int, default=200, help='epoch num for train'
                        )
    parser.add_argument('--batch_size', type=int,default=20,help='16how many pictures to process one time'
                        )
    parser.add_argument('--num_workers', type=int, default=0, help ='num_workers',
                        )
    parser.add_argument('--gpu_id', type=str, default='0', help='which gpu to use')
    args = parser.parse_args()
    return args
