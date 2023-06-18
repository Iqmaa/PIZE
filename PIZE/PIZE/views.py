from django.shortcuts import render
import os
import openai
import requests


def button(request):
    return render(request,'home.html')

def output(request):
    openai.api_key = "sk-"


    # Generating a question about the PDF.
    text = open("gns_1.txt", "r", encoding='utf-8').read()
    
    questions = openai.Completion.create(
        model="text-davinci-003",
        prompt ="generate 10 training multiplechoice questions for me Based on the text in the file: {}".format(text),
        max_tokens=700,
    )

    print(questions.choices[0].text)
    questions=questions.choices[0].text

    return render(request, 'home.html', {'questions': questions})