# AI_research_assistant Project

- [LinkedIn - Rajarshi Roy](https://www.linkedin.com/in/rajarshi-roy-learner/)
  
- [Github - Rajarshi Roy](https://github.com/Rajarshi12321/)

- [Medium - Rajarshi Roy](https://medium.com/@rajarshiroy.machinelearning)
  
- [Kaggle - Rajarshi Roy](https://www.kaggle.com/rajarshiroy0123/)
- [Mail - Rajarshi Roy](mailto:royrajarshi0123@gmail.com)
- [Personal-Website - Rajarshi Roy](https://rajarshi12321.github.io/rajarshi_portfolio/)


## Table of Contents

- [AI\_research\_assistant Project](#ai_research_assistant-project)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [For MLOPs tools:](#for-mlops-tools)
  - [Tech Stack](#tech-stack)
  - [Images](#images)
  - [Working with the code](#working-with-the-code)
  - [Contributing](#contributing)
  - [Contact](#contact)
  - [License](#license)


## About The Project

Welcome to the AI Research Assistant repository. This AI Research Assistant app is powered by Google Gemini. It helps in question answering about the provided research paper by uploading them through Streamlit, we save it in the `Data` folder and clean the document, index it by using Llamma-Index using Gemini Embedding Model. The created index is the upserted into Pinecone Vector DB.
The query function in the data_querying module will retrieve the vectors from Pinecone Vector DB and use that for generating response by embedding a basic prompt in it.

### For MLOPs tools:
I have used Github Actions for implementing CI/CD pipeline and AWS ECR for container registry of The Docker container and AWS EC2 for hosting it.

## Tech Stack
- Python
- LlamaIndex
- Google Gemini
- Streamlit
- Pinecone
- Docker
- Github Actions
- AWS ECR
- AWS EC2


## Images 

Main Page :
![image](https://github.com/Rajarshi12321/AI_research_assistant/assets/94736350/f878b503-507e-4bea-bc38-e539797d818e)


Page when querying and uploading pdf :

1. ![image](https://github.com/Rajarshi12321/AI_research_assistant/assets/94736350/8c912caa-a1ee-495c-af18-a934a87d4451)



2. ![image](https://github.com/Rajarshi12321/AI_research_assistant/assets/94736350/b3766e1e-225d-4f10-8ec8-d9c4a696ece0)

- ![image](https://github.com/Rajarshi12321/AI_research_assistant/assets/94736350/ff266891-2910-4216-bddb-5bb381f5ceeb)


## Working with the code


I have commented most of the neccesary information in the respective files.

To run this project locally, please follow these steps:-

1. Clone the repository:

   ```shell
   git clone https://github.com/Rajarshi12321/AI_research_assistant.git
   ```


2. **Create a Virtual Environment** (Optional but recommended)
  It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```shell
     conda create -p <Environment_Name> python==<python version> -y
     ```
     Example:
     ```shell
     conda create -p venv python=3.9 -y 
     ```
    Note:
    - It is important to use python=3.9 for proper use of LlamaIndex or else you would get unexpecterd errors


3. **Activate the Virtual Environment** (Optional)
   Activate the virtual environment based on your operating system:
      ```shell
      conda activate <Environment_Name>/
      ```
      Example:
     ```shell
     conda activate venv/
     ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

   Ensure you have Python installed on your system (Python 3.9 or higher is recommended).<br />
   Once the dependencies are installed, you're ready to use the project.

5. Create a .env file in the root directory and add your Pinecone credentials as follows:
    ```shell  
    PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    GEMINI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```


6. Run the Flask app: Execute the following code in your terminal.
   ```shell  
   streamlit run app.py 
   ```
   

6. Access the app: Open your web browser and navigate to http://localhost:8501/ to use the House Price Prediction and Property Recommendation app.

## Contributing
I welcome contributions to improve the functionality and performance of the app. If you'd like to contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bug fix.

2. Make your changes and ensure that the code is well-documented.

3. Test your changes thoroughly to maintain app reliability.

4. Create a pull request, detailing the purpose and changes made in your contribution.

## Contact

Rajarshi Roy - [royrajarshi0123@gmail.com](mailto:royrajarshi0123@gmail.com)



## License
This project is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.

I hope this README provides you with the necessary information to get started with the road to Generative AI with Google Gemini and LlamaIndex.
