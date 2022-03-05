#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob
from flask import Flask
from flask import render_template,request


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        s = TextBlob(text).sentiment
        return(render_template("index.html", results=s))
    else:
        return(render_template("index.html", results="2"))


# In[4]:


if __name__=="__main__":
    app.run()


# In[ ]:





# In[ ]:




