


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
    description="Dill, Parsley, Coriander or Watercress?"
)

iface.launch()