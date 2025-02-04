# import gdown

# # Replace with your Google Drive file ID
# file_id = "15VdFsCglzw_mDNLx7Pdcmp01pjarpIHH"
# url = f"https://drive.google.com/uc?id={file_id}"
# output = "model.zip"
# gdown.download(url, output, quiet=False)


## change it to .pkl




from fastai.vision.all import *

# Define the path to your dataset
path = Path("herb_dataset/dataset_split")

# Create a DataBlock
dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock),  
    get_items=get_image_files,          
    splitter=GrandparentSplitter(train_name='train', valid_name='test'),  
    get_y=parent_label,               
    item_tfms=Resize(224, method='squish'),              # Resize images to 224x224
    batch_tfms=aug_transforms(max_rotate=30, max_zoom=1.5, max_lighting=0.2)         # Apply data augmentation
).dataloaders(path, bs=16)              # Create DataLoaders with batch size 16



learn = vision_learner(
    dls,
    convnext_base,
    metrics=accuracy
)

learn.load("models/convnext")  # Replace with the name of your saved checkpoint

# Wow not bad but unfortunately, the model is too big. I want a small one for production it's 338.2 MB

#will find your model in models folder
learn.export("convnext_model.pkl")
