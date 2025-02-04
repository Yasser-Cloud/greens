


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

# Add EarlyStoppingCallback and SaveModelCallback
cbs = [
    EarlyStoppingCallback(monitor='valid_loss', patience=5),  # Stop training if validation loss doesn't improve for 5 epochs
    SaveModelCallback(monitor='valid_loss', fname='convnext')  # Save the best model based on validation loss
]
# Train the model
learn.fine_tune(epochs=20,cbs=cbs,base_lr=  0.001737800776027143)


# Wow not bad but unfortunately, the model is too big. I want a small one for production it's 338.2 MB

#will find your model in models folder
