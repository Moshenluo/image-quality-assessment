# Image Quality Assessment (IQA) using Deep Learning

## 📖 项目简介

**本科毕业论文项目**

| 项目 | 信息 |
|------|------|
| **论文题目** | 基于 AI 的绘画图像美学与情感评价研究 |
| **作者** | 毛申卓 |
| **学号** | 2191146 |
| **学院** | 通信学院 |
| **专业** | 电子信息与电气信息系统 |
| **班级** | 信管一班 |
| **指导教师** | 陈佩龙 |
| **学校** | 上海师范大学 |
| **时间** | 2025 年 4 月 |

---

本项目实现了一个基于深度学习的图像质量评估（Image Quality Assessment, IQA）系统，使用 ResNet18 作为骨干网络，结合 NNI（Neural Network Intelligence）进行超参数搜索优化。

### 主要功能

- 🖼️ 图像质量预测（使用预训练模型）
- 📊 数据集处理与分析
- 🔍 NNI 超参数自动搜索
- 📈 训练与验证

## 🏗️ 项目结构

```
TAD66K/
├── config.yml              # 配置文件
├── dataset.py              # 数据集加载与处理
├── demo.py                 # 演示脚本（图像质量预测）
├── imagename2csv.py        # 图像名称转 CSV 工具
├── option.py               # 参数配置
├── search_space.json       # NNI 超参数搜索空间
├── train_nni.py            # NNI 训练脚本
├── util.py                 # 工具函数
├── dataset/
│   ├── merge/              # 合并后的数据集
│   │   ├── train.csv
│   │   └── ttest.csv
│   └── unmerge/            # 原始数据集
│       ├── train/          # 训练集（按类别分）
│       └── test/           # 测试集（按类别分）
└── README.md               # 本文件
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- PyTorch 1.7+
- NNI 2.0+
- 其他依赖见 `requirements.txt`（如有）

### 安装依赖

```bash
pip install torch torchvision
pip install nni
pip install pillow
pip install pandas
pip install numpy
```

### 图像质量预测（Demo）

使用预训练模型进行图像质量评估：

```bash
python demo.py --image_path path/to/your/image.jpg
```

### 训练模型

使用 NNI 进行超参数搜索训练：

```bash
nnictl create --config config.yml
```

查看训练状态：

```bash
nnictl status
```

访问 NNI Web 界面（默认端口 8080）查看搜索结果和训练进度。

### 数据集处理

将图像名称转换为 CSV 格式：

```bash
python imagename2csv.py --input_dir path/to/images --output_dir dataset/
```

## 📊 数据集

数据集包含多个类别的图像质量评估数据：

- **训练集**: `dataset/unmerge/train/`（50+ 个类别）
- **测试集**: `dataset/unmerge/test/`（50+ 个类别）
- **合并数据**: `dataset/merge/`

### 数据类别

包括：art, beach, bird, car, cat, city, clouds, dog, flower, food, nature, night, portrait, sea, sky, sunset, water 等 50+ 个场景类别。

## 🔧 配置说明

### config.yml 主要参数

```yaml
# 训练参数
trialConcurrency: 2
maxExecDuration: 1h
maxTrialNum: 20
trainingServicePlatform: local

# 模型参数
model: resnet18
pretrained: true
num_classes: 1

# 数据参数
batch_size: 32
learning_rate: 0.001
epochs: 50
```

### search_space.json

定义 NNI 超参数搜索空间，包括：
- 学习率范围
- batch size 选择
- 优化器选择
- dropout 率等

## 📈 评估指标

- **SRCC**: Spearman 秩相关系数
- **LCC**: 线性相关系数
- **MSE**: 均方误差

预训练模型性能（示例）：
- SRCC: 0.513
- LCC: 0.531
- MSE: 0.16

## 🎓 论文摘要

### 研究背景

随着人工智能技术的发展，绘画图像的美学与情感评价成为计算机视觉和艺术交叉领域的研究热点。本研究旨在利用深度学习技术，建立自动化的绘画图像美学质量评估模型。

### 主要研究内容

1. **中国古典建筑绘画美学研究** - 分析中国古典建筑绘画的美学特征与评价体系
2. **图像美学评价研究现状** - 综述图像美学评价的研究方法与进展
3. **人工标注与图像美学评价** - 研究人工标注在图像美学评价中的作用
4. **深度学习与图像美学评价** - 探索深度学习在图像美学评价中的应用

### 技术路线

- 使用 ResNet18 作为特征提取骨干网络
- 利用 NNI 进行超参数自动搜索优化
- 在 AVA、AADB、Flickr-AES 等数据集上进行训练与验证
- 评估指标：SRCC（Spearman 秩相关系数）、LCC（线性相关系数）、MSE（均方误差）

## 📝 使用说明

### 1. 准备数据

确保数据集 CSV 文件位于 `dataset/` 目录下。

### 2. 修改配置

根据需求修改 `config.yml` 中的参数。

### 3. 开始训练

```bash
nnictl create --config config.yml
```

### 4. 查看结果

- NNI Web 界面：http://localhost:8080
- 训练日志：查看 `logs/` 目录

### 5. 使用预训练模型

```bash
python demo.py --image_path your_image.jpg --model_path SRCC_513_LCC_531_MSE_016.pth
```

## 🔗 相关资源

- [PyTorch 官方文档](https://pytorch.org/docs/)
- [NNI 官方文档](https://nni.readthedocs.io/)
- [ResNet 论文](https://arxiv.org/abs/1512.03385)

## 📄 许可证

本项目为上海师范大学本科毕业论文代码，仅供学习研究使用。

## 📧 联系方式

- **作者**: 毛申卓
- **GitHub**: [@Moshenluo](https://github.com/Moshenluo)
- **Email**: 1411795718@qq.com
- **学校**: 上海师范大学 通信学院

---

**最后更新**: 2026-03-13
