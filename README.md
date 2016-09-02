# What are we having for dinner? (Wawhfd)

My wife and I have a hard time planning what to have to dinner. I created a little Django/React app to help us out. I wanted a place where we could save meals and recipes and then assign them to one of the next several days.

![](docs/screenshot.png)

Basically, you fill the sidebar with recipes and/or meals, and then drag and drop them onto days.

#### Amazing features!
- Add new recipes
- Edit existing recipes
- Delete recipes you never want to eat again
- Search for recipes


## Setup

##### Prequisites:
- Python 3
- virualenv
- Postgres

##### Installation
1. Clone the repo: `git clone git@github.com:calebrash/wawhfd.git && cd wawhfd`
2. Create a virtualenv: `mkvirtualenv -ppython3 wawhfd`
3. Create database and install dependencies: `make init`
4. Run migrations: `make migrate`
5. Run the server: `make server`

Want to make changes? You'll need to install webpack (`npm install -g webpack`) and then run `make dev` to build static files.
