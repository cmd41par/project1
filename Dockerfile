# Dockerfile, Image, Container
# https://www.youtube.com/watch?v=bi0cKgmRuiA
#  above is the youtube video 

# lets use this video for another docker contain - https://www.youtube.com/watch?v=zs3tyVgiBQQ


FROM python:3.10

RUN python3 -m venv .venv

ADD helloworld.py .

RUN pip install pandas
RUN pip install pytest

RUN pip freeze > requirements.txt

CMD ["python", "./helloworld.py"]

