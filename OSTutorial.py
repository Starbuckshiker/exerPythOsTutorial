#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


print(dir(os))


# In[3]:


print(os.getcwd())


# In[9]:


os.chdir('/Users/dlist/OneDrive/Desktop')


# In[10]:


os.listdir('/Users/dlist/OneDrive/Desktop')


# In[18]:


os.mkdir('OS-Demo-2/Sub-Dir-1')


# In[16]:


os.makedirs('OS-Demo-2/Sub-Dir-1')
           


# In[19]:


os.rmdir('OS-Demo-2/Sub-Dir-1')


# In[21]:


os.mkdir('OS-Demo-2/Sub-Dir-1')


# In[22]:


os.removedirs('OS-Demo-2/Sub-Dir-1')


# In[26]:


os.mkdir('OS-Demo-2')


# In[29]:


os.rename('OS-Demo-2', 'Test')


# In[30]:


print(os.stat('Test'))


# In[31]:


from datetime import datetime


# In[37]:


mod_time = os.stat('Test').st_mtime


# In[38]:


print(datetime.fromtimestamp(mod_time))


# In[76]:


for dirpath, dirnames, filenames in os.walk('/Users/dlist/Desktop/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('File:', filenames)
    print()


# In[65]:


home_dir =os.environ['username']


# In[66]:


print(os.environ.get('username'))


# In[68]:


file_path = os.path.join('username'),'test.txt'


# In[69]:


print(file_path)


# In[72]:


file_path = os.path.join(os.environ.get('username'),'test.txt')


# In[73]:


print(file_path)


# In[77]:


os.path.basename('/tmp/test.txt')


# In[78]:


print(os.path.basename('/tmp/test.txt'))


# In[79]:


print(os.path.split('/tmp/test.txt'))


# In[80]:


os.path.exists('/tmp/test.txt')


# In[83]:


os.path.isdir('/tmp/test')


# In[82]:


os.path.isfile('/tmp/test')


# In[89]:


os.path.splitext('/tmp/test')


# In[90]:


print(os.path.splitext('/tmp/test.txt'))


# In[94]:


https://docs.python.org/3/tutorial/index.html 


# In[ ]:


https://www.askpython.com/python/environment-variables-in-python

