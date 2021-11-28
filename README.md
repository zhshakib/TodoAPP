<!-- @format -->

## TODO API with FastAPI

**This was my first FastAPI learning with a Project!**

> Learning new thing is always fun!

_Neat and clean `main.py` file!_

```python
from fastapi import FastAPI
from routers.todos import router

app = FastAPI()

app.include_router(router)
```

Everything was structured professionally with comments!

Project Structure:

```
TodoAPP
│
└───models
    │
    └───Todo.py
└───routers
    │
    └───todos.py
└───schemas
    │
    └───Todo.py
│README.md
│.gitignore
│main.py
│requirements.txt
```

<hr>
## How to install or Develop??
<hr/>

<ol>
<li>Clone the repository or Download it.</li>
<li>Cd into the project and run

```properties
virutalenv env
```

it will create Virtual Environment for The project

</li>
<li>After that run bellow command for Activating the env.

```properties
source env/Scripts/activate
```

it will Activate the Virtual Environment for You

</li>
<li>For installing dependencies run this!

```properties
pip install -r requirements.txt
```

</li>

<li>start the project

```properties
uvicorn main:app --reload
```

</li>

</ol>

<hr>

# Enjoy The FastAPI
