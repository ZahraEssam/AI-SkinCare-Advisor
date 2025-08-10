import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import google.generativeai as genai
from tkinter import PhotoImage

# Set the API Key for the model
genai.configure(api_key="AIzaSyB6meCG-MgBRqudBPTW3RSkfTxE3QMnq4k")

# Set up the model to use
model = genai.GenerativeModel(model_name="gemini-2.5-flash")
# List of skin conditions
skin_conditions = ["Basal Cell Carcinoma", "Squamous Cell Carcinoma", "Melanoma", "Eczema", "Psoriasis", "Acne", "Rosacea"]

# List of skin types
skin_types = ["Oily", "Dry", "Sensitive", "Normal", "Combination"]

# List of affected areas
affected_areas = ["Face", "Neck", "Chest", "Back", "Arms", "Legs", "Abdomen"]

# Function to display medical advice based on user input
def display_response():
    # Get user input
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    diagnosis = skin_condition_slider.get()
    affected_area = affected_area_slider.get()
    skin_type = skin_type_slider.get()

    # Formatted prompt
    prompt = f"""
    You're a friendly AI medical assistant 👩‍⚕️👨‍⚕️.

    Here’s the information from the patient:

    👤 Name: {name}
    🎂 Age: {age}
    🚻 Gender: {gender}
    🩻 Diagnosis: {diagnosis}
    🧴 Skin Type: {skin_type}
    📍 Affected Area: {affected_area}

    Now, give the patient some simple and helpful advice:

    1. Greet the patient by name warmly and kindly. 🫶
    2. Explain their diagnosis in simple words. 🩺
    3. Share 3 quick tips for managing their condition. 📝
    4. Provide 2 things they should avoid or be cautious about. ⚠️
    5. End with a friendly reminder to consult a dermatologist. 👩‍⚕️

    **Each point should be on a new line, clear, and easy to follow.**

    Make sure your tone is supportive and easy to read. Use emojis to keep it light and encouraging! ✨
    """

    # Get the response from the model based on the prompt
    response = model.generate_content(prompt)
    
    # Clear the previous text in the response box
    response_box.delete(1.0, tk.END)
    
    # Display the response in the text box
    response_box.insert(tk.END, response.text)

# Create the main window (GUI)
root = tk.Tk()
root.title("Medical Advice")
root.geometry("800x600")  # Set window size

# Add an image to the interface
try:
    img = PhotoImage(file="C:/Users/LAP STORE/Downloads/medical_advice/1-11222.jpg")  # Make sure the image path is correct
    img_label = tk.Label(root, image=img)
    img_label.pack(pady=10)
except Exception as e:
    print(f"Error loading image: {e}")

# Change background color to calm and medical-like
root.configure(bg="#E9F5FB")  # Light blue background

# Create a PanedWindow to divide the window into two parts
paned_window = tk.PanedWindow(root, orient="horizontal")
paned_window.pack(fill=tk.BOTH, expand=True)

# Left frame for data input
left_frame = tk.Frame(paned_window, bg="#E9F5FB", width=400)
paned_window.add(left_frame)

# Right frame for displaying the response
right_frame = tk.Frame(paned_window, bg="#E9F5FB", width=400)
paned_window.add(right_frame)

# Title of the program
label = tk.Label(left_frame, text="SkinCare Advisor", font=("Arial", 30, "bold"), bg="#E9F5FB", fg="#4A90E2")
label.pack(pady=20)

# Name input field
tk.Label(left_frame, text="Name:", bg="#E9F5FB", font=("Arial", 14), fg="#333").pack()
name_entry = tk.Entry(left_frame, font=("Arial", 14))
name_entry.pack(pady=5)

# Age input field
tk.Label(left_frame, text="Age:", bg="#E9F5FB", font=("Arial", 14), fg="#333").pack()
age_entry = tk.Entry(left_frame, font=("Arial", 14))
age_entry.pack(pady=5)

# Gender selection
tk.Label(left_frame, text="Gender:", bg="#E9F5FB", font=("Arial", 14), fg="#333").pack()
gender_var = tk.StringVar()  # No initial value set

tk.Radiobutton(left_frame, text="Male", variable=gender_var, value="male", bg="#E9F5FB", font=("Arial", 12), fg="#333").pack()
tk.Radiobutton(left_frame, text="Female", variable=gender_var, value="female", bg="#E9F5FB", font=("Arial", 12), fg="#333").pack()

# Slider to choose skin condition
tk.Label(left_frame, text="Choose your skin condition:", bg="#E9F5FB", font=("Arial", 14), fg="#333").pack()
skin_condition_slider = ttk.Combobox(left_frame, values=skin_conditions, state="normal", font=("Arial", 12))
skin_condition_slider.set("")  # Leave slider with no initial value
skin_condition_slider.pack(pady=5)

# Slider to choose skin type
tk.Label(left_frame, text="Choose your skin type:", bg="#E9F5FB", font=("Arial", 14), fg="#333").pack()
skin_type_slider = ttk.Combobox(left_frame, values=skin_types, state="normal", font=("Arial", 12))
skin_type_slider.set("")  # Leave slider with no initial value
skin_type_slider.pack(pady=5)

# Slider to choose affected area
tk.Label(left_frame, text="Choose affected area:", bg="#E9F5FB", font=("Arial", 14), fg="#333").pack()
affected_area_slider = ttk.Combobox(left_frame, values=affected_areas, state="normal", font=("Arial", 12))
affected_area_slider.set("")  # Leave slider with no initial value
affected_area_slider.pack(pady=5)

# Button to generate medical advice
generate_button = tk.Button(left_frame, text="Get Medical Advice", command=display_response, font=("Helvetica", 16), bg="#4CAF50", fg="white")
generate_button.pack(pady=20)

# Text box to display medical advice
response_box = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=80, height=80, font=("Arial", 12), bg="#ffffff")
response_box.pack(pady=150)

# Start the main loop of the window
root.mainloop()

