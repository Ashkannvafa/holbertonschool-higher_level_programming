#!/usr/bin/python3
"""Fetch and process posts from JSONPlaceholder API."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print status code and titles."""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save selected fields into CSV."""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        posts = r.json()

        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
