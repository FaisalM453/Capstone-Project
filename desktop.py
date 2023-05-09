import tkinter as tk
import pickle
from tkinter import messagebox
import numpy as np
# Load the iris dataset and create a decision tree model
# (insert the code for this here)

# Create the Tkinter window
root = tk.Tk()
root.title("Iris Species Predictor")

# Create the GUI widgets
label1 = tk.Label(root, text="Sepal Length:")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Sepal Width:")
entry2 = tk.Entry(root)
label3 = tk.Label(root, text="Petal Length:")
entry3 = tk.Entry(root)
label4 = tk.Label(root, text="Petal Width:")
entry4 = tk.Entry(root)
button1 = tk.Button(root, text="Predict")

# Define the prediction function
def predict_species():
    sepal_length = float(entry1.get())
    sepal_width = float(entry2.get())
    petal_length = float(entry3.get())
    petal_width = float(entry4.get())
    # Create a numpy array from the input values
    new_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Use the trained classifier to make a prediction
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    predicted_class = model.predict(new_data)[0]

    # Return the predicted class
    tk.messagebox.showinfo("Prediction", f"The predicted species is {predicted_class}")
  

# Attach the prediction function to the button
button1.config(command=predict_species)

# Display the GUI window
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
label3.grid(row=2, column=0)
entry3.grid(row=2, column=1)
label4.grid(row=3, column=0)
entry4.grid(row=3, column=1)
button1.grid(row=4, column=0, columnspan=2)
root.geometry("500x500")
root.mainloop()