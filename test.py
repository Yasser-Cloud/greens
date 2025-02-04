import gdown


# to download my training covnext model
# file_id = "15VdFsCglzw_mDNLx7Pdcmp01pjarpIHH"
# url = f"https://drive.google.com/uc?id={file_id}"
# output = "model.zip"
# gdown.download(url, output, quiet=False)


# then run in terminal

##unzip model.zip

#from fastai.vision.all import *


from fastai.vision.all import load_learner
import gradio as gr

# Load the model
model_path = "convnext_model/convnext_model.pkl"
learn = load_learner(model_path)

# Prediction function
def predict(image):
    pred, _, probs = learn.predict(image)
    return pred

# Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs="image",
    outputs="label",
    title="Greens classifier",
    description="Upload an image to classify using the ConvNeXt model."
)

iface.launch()