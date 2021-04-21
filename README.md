# Let's containerize the Flask project!

Our goal is to containerize this application.

## Exercise: Dockerfile

Our goal is to write a Dockerfile for the Flask container.

First, `git clone` this repository, or simple copy the file `app.py`. 

This is a demonstration web server written in Flask (Python). 
To compile Python code, we can use the official image, 
or install Python packages in any of the official base images.

The entire code is in a single source file (`app.py`), 
and should be executed like this:

```
python app.py
```
The port exported by the application is 80

## Test the application

After you have created the Dockerfile, run the follow commands to test it:
```
~$ docker build -t flaskdemo .
~$ docker run -it --rm -p 80:80 flaskdemo
```

Go to http://localhost
You should see `Hello World` in your browser. 

Try running this other version of `docker run`:
```
~$ docker run -it --rm -p 80:80 flaskdemo "Ciao Mondo"
```

Do you see `Ciao Mondo` in your browser?
