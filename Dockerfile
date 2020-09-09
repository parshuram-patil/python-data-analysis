FROM python:3

LABEL maintainer="parshuram.patil@outlook.in"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
#RUN export PYTHONPATH=.
#RUN echo $PYTHONPATH

CMD [ "python", "./data_analysis_titanic.py" ]