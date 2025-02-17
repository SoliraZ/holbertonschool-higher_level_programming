#!/usr/bin/python3
""" Task 02: Fetch and print posts from the API """
import requests
import csv


response = requests.get('https://jsonplaceholder.typicode.com/posts')
statuscode = response.status_code


def fetch_and_print_posts():
    print(f"Status Code: {statuscode}")
    if statuscode == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    if statuscode == 200:
        posts = response.json()
        with open('posts.csv', mode='w', newline='') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                filtered_post = {key: post[key] for key in fieldnames}
                writer.writerow(filtered_post)
