# Phase0.1 - Setup Enviroment

Assign: R.Smith
Date: May 16, 2023
Phase: Phase0.1 Setup Enviroment
Status: Done
Status 1: Done

# **Setting up Ubuntu Environment for AI Assistant Development**

## **Overview**

This page provides a step-by-step guide on how to set up the Ubuntu environment for your AI assistant development project. Follow these instructions to install the necessary dependencies and create a development environment ready for building and training your AI assistant.

## **Prerequisites**

- Ubuntu operating system (version XYZ or higher)
- Terminal or command line access with administrative privileges

## **Steps**

1. **Update System Packages**
    
    Open the terminal and run the following commands to update the system packages:
    
    ```
    bashCopy code
    sudo apt update
    sudo apt upgrade
    
    ```
    
2. **Install Python**
    
    Check if Python is already installed on your system by running **`python3 --version`** in the terminal. If it is not installed, you can install Python by running the following command:
    
    ```
    bashCopy code
    sudo apt install python3
    
    ```
    
    Verify the installation by running **`python3 --version`**.
    
3. **Set Up a Virtual Environment**
    
    Create a virtual environment to isolate your project dependencies. Run the following commands:
    
    ```
    bashCopy code
    sudo apt install python3-venv
    python3 -m venv project_env
    
    ```
    
    Activate the virtual environment:
    
    ```
    bashCopy code
    source project_env/bin/activate
    
    ```
    
4. **Install Dependencies**
    
    Install the necessary dependencies for your AI assistant development. In the activated virtual environment, run the following commands:
    
    ```
    bashCopy code
    pip install torch
    pip install transformers
    pip install pandas
    pip install wandb
    
    ```
    
5. **Set Up Project Structure**
    
    Create the folder structure for your project. Run the following commands:
    
    ```
    bashCopy code
    mkdir ProjectSAi
    cd ProjectSAi
    mkdir TrainedModels
    mkdir TrainScripts
    mkdir validation
    mkdir wandb
    mkdir Preprocesseddata
    mkdir "Pyscripts for future"
    mkdir results
    
    ```
    
6. **Clone the Project Repository (Optional)**
    
    If you have a project repository hosted on a version control system like GitHub, you can clone it into the **`ProjectSAi`** directory using the following command:
    
    ```
    bashCopy code
    git clone <repository_url>
    
    ```
    
7. **Update File Paths**
    
    Update the file paths in your script to reflect the folder structure you created. Replace the file paths with the appropriate paths starting from the **`ProjectSAi`** directory.
    
8. **Start Development**
    
    You are now ready to start developing your AI assistant! Activate your virtual environment and run your script using the following command:
    
    ```
    bashCopy code
    python train.py
    
    ```
    

##