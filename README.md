# Random-usernames

Simple website that generates docker-like random names. Useful for for when you register on a website/game and don't know what name to put

[random-usernames-website](https://i.imgur.com/TQPLuYl.png

You can visit a preview here https://random-names.skydreamy.com/

## 30 seconds start

1. Clone the project
1. Open a terminal on the root of the project and type `docker-compose up`
1. Go to localhost:8080 on your browser

## Additional notes

Project uses the following libraries:

- FastApi and Jinja2 for serving and creating the html
- Slowapi to limit the number of requests a client can make per second
- randomname to generate the random words
