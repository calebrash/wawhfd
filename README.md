# What are we having for dinner? (Wawhfd)

My wife and I have a hard time planning what to have to dinner. I created a little Flask/React app to help us out. I wanted a place where we could save meals and recipes and then assign them to one of the next several days.

![](docs/screenshot.png)

Basically, you fill the sidebar with recipes and/or meals, and then drag and drop them onto days.

#### Amazing features!
- Add new recipes
- Edit existing recipes
- Delete recipes you never want to eat again
- Search for recipes


## Setup

Note, Wawhfd uses Python 3 and (virtualenv)[https://virtualenv.pypa.io/en/stable/].

1. Clone the repo: `git clone ... && cd wawhfd`
2. Create a virtualenv: `mkvirtualenv -ppython3 wawhfd`
3. Create a database: `psql -c 'CREATE DATABASE wawhfd'`
4. Build everything: `make build`
5. Run everything: `make server`

Want to make changes? You'll need to install webpack (`npm install -g webpack`) and then run `make dev` to build static files.


## FAQ

Anticipatorily, anyway...

#### Does it support multiple users?
It supports _no_ users! I built this to run on an old laptop on my local netowrk.

#### Is it really fast?
Probably not!

#### Is this a good example for learning Flask or React?
No! I don't really know what I'm doing. This is probably filled with bad ideas.

#### Why didn't you use Redux (or some other kind of Flux)?
I started to use Redux. I wanted to use Redux. After a couple of hours trying to make sense of the docs, I decided it was better to start making progress than to continue trying to setup Redux.
