#Batch Clone git repositories from Canvas Download

#Import Libraries
import tkinter
from tkinter import filedialog
import os
from bs4 import BeautifulSoup
import subprocess

#Use file explorer to select the download location of the submissions
tkinter.Tk().withdraw()
folder = filedialog.askdirectory()

submitList = os.listdir(folder)

#Retrieve the github repo link from each html file
for file in submitList:
    with open(folder + "/" + file, 'r') as File:
        html_content = File.read() #open the file so that beautifulsoup can read it

    soup = BeautifulSoup(html_content, 'html.parser') #setup the parser

    #get link form document
    link = next((a.get('href') for a in soup.find_all('a') if a.get('href') is not None), None)

    #Change the active directory to the folder and assign the students name to their repo folder
    os.chdir(folder)
    folder_name = file.split("_", 1)[0].upper()

    #Attempt cloning the repo
    try:
        subprocess.run(['git', 'clone', link, folder_name], check=True)
        print("Repository cloned successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to clone repository. Error:", e)

