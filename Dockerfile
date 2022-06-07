FROM python:3.9

RUN apt update
RUN apt install python3

# set the working directory in the container
WORKDIR /Users/tahit/OneDrive/Documents/devopsuno

COPY myweather.py ./

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python3", "./myweather.py" ]