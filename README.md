# Python Learn/Test server

This ubuntu server can be used to test out and to learn how to use Python for the web.
This server will use wsgi and apache. wsgi is the interface that will sit between your apache server and your actual python code.

# How to use 

You'll need ***vagrant*** to get this working so head over to vagrantup.com
and follow the installation steps on their website.

# Start server

Once you have vagrant installed the only thing you need to do is 

>vagrant up

and you are ready to start writing some awesome Python code

# Logs

* access.log: These are the regular apache access logs
* error.log: When your Python scripts give a 500 error take a look in this file. It will give you more information about what is going wrong with your script.

# Note

Keep in mind that Python is completely new to me so I can't garantee that this is the best way of getting started.
