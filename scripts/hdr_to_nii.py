import nibabel as nib
import os

# 指定包含 Analyze 文件的文件夹路径
input_folder = r'D:\qinchendong\ICASSP2025\unsupervised-medical-image-segmentation-master\checkpoints\lpba40_contrastive_learning\output_lpba40_contrastive_learning\deformation_field_LPBA40_rigidly_registered_pairs_histogram_standardization_small'
output_folder = r'D:\qinchendong\ICASSP2025\unsupervised-medical-image-segmentation-master\checkpoints\lpba40_contrastive_learning\output_lpba40_contrastive_learning\deformation_nii'

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 检查文件是否为 .hdr 文件
    if filename.endswith('.hdr'):
        # 获取不带扩展名的文件名
        base_name = os.path.splitext(filename)[0]
        
        # 构建完整的输入文件路径
        hdr_path = os.path.join(input_folder, filename)
        img_path = os.path.join(input_folder, base_name + '.img')
        
        # 检查对应的 .img 文件是否存在
        if os.path.exists(img_path):
            # 加载 Analyze 格式文件
            analyze_img = nib.load(hdr_path)
            
            # 构建输出文件路径
            output_path = os.path.join(output_folder, base_name + '.nii')
            
            # 保存为 NIfTI 格式
            nib.save(analyze_img, output_path)
            print(f'已将 {hdr_path} 转换为 {output_path}')
        else:
            print(f'对应的 .img 文件不存在: {img_path}')
