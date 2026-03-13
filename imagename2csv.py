import os
import csv
import argparse
from glob import glob

def list_images_to_csv(folder_path, output_csv, extensions=['.jpg']):
    # 创建匹配模式
    pattern = os.path.join(folder_path, '*')
    image_files = []

    # 遍历所有支持的图片格式
    for ext in extensions:
        image_files.extend(glob(os.path.join(folder_path, f'*{ext}')))

    # 按文件名排序
    image_files.sort()

    # 写入CSV文件
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入标题行
        writer.writerow(['image'])

        # 写入每个文件名
        for img_path in image_files:
            filename = os.path.basename(img_path)
            writer.writerow([filename])

    print(f"成功保存 {len(image_files)} 个图片文件名到 {output_csv}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='将文件夹中的图片文件名保存到CSV')
    parser.add_argument('-i', '--input', default=r'C:\Users\17168\Desktop\images\download_images\S1', help='输入图片文件夹路径')
    parser.add_argument('-o', '--output', default='S1.csv', help='输出CSV文件名')

    args = parser.parse_args()

    if not os.path.isdir(args.input):
        raise ValueError("输入路径不是有效的文件夹")

    list_images_to_csv(args.input, args.output)