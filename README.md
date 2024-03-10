# Chest X-ray Analysis using Deep Learning

![banner](assets/banner.png)

This project is the final streamlit app developed for Omdena Myanmar Chapter

## Project Goal

The project's primary objective is to create an AI-driven healthcare 
solution for chest X-ray analysis, disease detection, and COVID-19 diagnosis, utilizing deep learning algorithms. 
To begin, an extensive literature review will be conducted, informing the project's goals. A diverse dataset of 
chest X-ray images, encompassing COVID-19 cases and other chest diseases, will be collected and preprocessed for 
model training. Exploratory data analysis will be performed to reveal insights and potential 
biases.<br><br>Choosing the most appropriate deep learning algorithm or architecture will be a key step, 
considering factors such as complexity, interpretability, and computational requirements. The selected model will 
be implemented, trained, and optimized to achieve precise disease detection. Additionally, a user-friendly web or 
mobile app will be developed to provide real-time results for uploaded chest X-ray images.<br><br>The final 
solution will be deployed in a secure, scalable hosting environment. Comprehensive project documentation and a 
final presentation will be delivered to showcase results and the solution's potential impact on healthcare. 
Knowledge sharing and open discussions about AI-driven healthcare solutions will be encouraged.

## Requirements

To run this locally, you need to have the following dependencies installed:

- Python 3.8 or above
- Streamlit

```shell
pip install -r requirements.txt
```

## Run Web Application Locally

To start the system, run the following command in your terminal:

```shell
streamlit run main.py
```

Once the application is running, you can access it through your web browser. Under the models section the user will be asked to upload the chest x-ray image. After providing the required inputs, click the "Predict" button to obtain the predicted diagnosis result.
