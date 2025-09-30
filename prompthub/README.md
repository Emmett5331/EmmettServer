\# PromptHub



\*\*PromptHub\*\* is a simple Python terminal helper package that makes it easy to create terminal apps and print colored messages.  

You can use it as a \*\*Python package\*\* or build CLI tools with it.



---



\## Features



\- Print colored messages easily:

```python

import prompthub



prompthub.say("Hello!")                # Default green

prompthub.say("Warning!", color="yellow")

prompthub.say("Error!", color="red")



