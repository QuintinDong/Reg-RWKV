# Reg-RWKV
Download the images and segmentation masks for LPBA40 dataset:

   LPBA40 Images: [LPBA40_rigidly_registered_pairs.tar.gz](https://www.synapse.org/#!Synapse:syn3251419)  
   LPBA40 Labels: [LPBA40_rigidly_registered_label_pairs.tar.gz](https://www.synapse.org/#!Synapse:syn3251070)  
Unzip them in folder `datasets/LPBA40`:

   `datasets/LPBA40/LPBA40_rigidly_registered_pairs`  
   `datasets/LPBA40/LPBA40_rigidly_registered_label_pairs`  

  Pre-process the LPBA40 dataset:

   ```shell
   cd scripts
   python preprocessing_lpba40.py
   ```
   
   output small image results:
   
   `datasets/LPBA40/LPBA40_rigidly_registered_pairs_histogram_standardization_small`  
   `datasets/LPBA40/LPBA40_rigidly_registered_label_pairs_small`

   output large image results:
   
   `datasets/LPBA40/LPBA40_rigidly_registered_pairs_histogram_standardization_large`  
   `datasets/LPBA40/LPBA40_rigidly_registered_label_pairs_large`
