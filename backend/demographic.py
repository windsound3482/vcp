# Demographic data processing

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
import json

# read file in Attributes fold
file_name = 'Participants.csv'
path = './VAST-Challenge-2022/Datasets/Attributes/' + file_name
participants = pd.read_csv('./Participants.csv')

def plot_joviality_education():
    # prepare data for educational level in different age groups
    i = 18
    education_level_nums = []
    labels = ['18-24', '25-31', '32-38', '39-45', '46-52','53-60']
    while(i <= 46):
        age_interval =  (i <= participants.age) & (participants.age <= i + 6)
        education_level_num = participants[(age_interval)].educationLevel.value_counts()
        education_level_nums.append(education_level_num)
        i += 7
    education_level_num_53to60 = participants[(participants.age >= 53) & (participants.age <= 60)].educationLevel.value_counts()
    education_level_nums.append(education_level_num_53to60)

    high_school = []
    bachelors = []
    graduate = []
    low = []

    i = 0
    while(i<6):
        temp=education_level_nums[i]
        high_school.append(temp[0])
        bachelors.append(temp[1])
        graduate.append(temp[2])
        low.append(temp[3])
        i += 1

    # prepare data for joviality in different age groups
    i = 18
    joviality_mean = []
    while(i <= 46):
        age_interval =  (i <= participants.age) & (participants.age <= i + 6)
        joviality = participants[(age_interval)]['joviality']
        mean = joviality.mean()
        joviality_mean.append(mean)
        i += 7

    joviality_mean.append(participants[(53 >= participants.age) & (participants.age <= 60)]['joviality'].mean())
    joviality_mean = np.asarray(joviality_mean)


    # plot 
    labels = ['18-24', '25-31', '32-38', '39-45', '46-52','53-60']
    fig, ax = plt.subplots(ncols=2, sharey=True, figsize= (20,8))
    y = range(0, 6)

    # plot educational level in different age groups
    ax[1].barh(y, high_school,align='center',label='HighSchoolOrCollege')
    ax[1].barh(y, bachelors,left=high_school, label='Bachelors')
    ax[1].barh(y, graduate,left=(np.array(high_school)+np.array(bachelors)), label='Graduate')
    ax[1].barh(y, graduate,left=(np.array(high_school)+np.array(bachelors)+np.array(graduate)), label='Low')
    ax[1].set_title('Educational Level')
    ax[1].legend()
    ax[1].grid()

    # plot mean joviality values in different age groups
    ax[0].set_title("Joviality Values")
    ax[0].set_ylabel("Age Groups")
    ax[0].barh(y,joviality_mean,color='purple')
    ax[0].set(yticks=y, yticklabels = labels)
    ax[0].invert_xaxis()
    ax[0].grid()
    title = 'Javiality Values and Educational Level in different Age Groups'
    plt.figtext(.5,.9, title, fontsize=15, ha='center')
    plt.savefig('./static/joviality_education')
    #plt.show()
