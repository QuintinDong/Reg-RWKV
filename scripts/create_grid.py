import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

# 读取NIfTI文件
def read_deformation_field(nifti_file):
    deformation_field = sitk.ReadImage(nifti_file)
    return sitk.GetArrayFromImage(deformation_field)

# 创建规则网格
def create_grid(shape, spacing=5):
    z = np.arange(0, shape[0], spacing)
    y = np.arange(0, shape[1], spacing)
    x = np.arange(0, shape[2], spacing)
    grid_z, grid_y, grid_x = np.meshgrid(z, y, x, indexing='ij')
    return grid_x, grid_y, grid_z

# 应用变形场
def apply_deformation_field(grid_x, grid_y, grid_z, deformation_field):
    # 将网格索引转换为整数类型
    grid_x = grid_x.astype(int)
    grid_y = grid_y.astype(int)
    grid_z = grid_z.astype(int)

    # 确保索引在有效范围内
    height, width, depth, _ = deformation_field.shape
    valid_indices = (grid_z < height) & (grid_y < width) & (grid_x < depth)
    
    deformed_grid_x = np.copy(grid_x).astype(float)
    deformed_grid_y = np.copy(grid_y).astype(float)
    deformed_grid_z = np.copy(grid_z).astype(float)

    deformed_grid_x[valid_indices] += deformation_field[grid_z[valid_indices], grid_y[valid_indices], grid_x[valid_indices], 0]
    deformed_grid_y[valid_indices] += deformation_field[grid_z[valid_indices], grid_y[valid_indices], grid_x[valid_indices], 1]
    deformed_grid_z[valid_indices] += deformation_field[grid_z[valid_indices], grid_y[valid_indices], grid_x[valid_indices], 2]

    return deformed_grid_x, deformed_grid_y, deformed_grid_z

# 可视化网格
def plot_grid_2d(grid_x, grid_y, deformed_grid_x, deformed_grid_y, z_index=0):
    plt.figure(figsize=(10, 10))

    # 绘制原始网格
    for i in range(grid_x.shape[0]):
        plt.plot(grid_x[i, :, z_index], grid_y[i, :, z_index], color='blue', alpha=0.5)
    for j in range(grid_x.shape[1]):
        plt.plot(grid_x[:, j, z_index], grid_y[:, j, z_index], color='blue', alpha=0.5)

    # 绘制变形后的网格
    for i in range(deformed_grid_x.shape[0]):
        plt.plot(deformed_grid_x[i, :, z_index], deformed_grid_y[i, :, z_index], color='red', alpha=0.5)
    for j in range(deformed_grid_x.shape[1]):
        plt.plot(deformed_grid_x[:, j, z_index], deformed_grid_y[:, j, z_index], color='red', alpha=0.5)

    plt.title('Deformed Grid (2D XY slice at Z={})'.format(z_index))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# 主函数
def main():
    nifti_file = r'D:\qinchendong\ICASSP2025\unsupervised-medical-image-segmentation-master\checkpoints\lpba40_contrastive_learning\output_lpba40_contrastive_learning\deformation_nii\l31_to_l32.nii'
    
    deformation_field = read_deformation_field(nifti_file)
    grid_x, grid_y, grid_z = create_grid(deformation_field.shape[:3], spacing=5)
    deformed_grid_x, deformed_grid_y, deformed_grid_z = apply_deformation_field(grid_x, grid_y, grid_z, deformation_field)
    
    plot_grid_2d(grid_x, grid_y, deformed_grid_x, deformed_grid_y, z_index=10)  # 选择一个切片索引来显示二维网格

if __name__ == "__main__":
    main()







#nifti_file = r'D:\qinchendong\ICASSP2025\unsupervised-medical-image-segmentation-master\checkpoints\lpba40_contrastive_learning\output_lpba40_contrastive_learning\deformation_nii\l31_to_l32.nii'