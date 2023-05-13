FROM python:3.11-slim
RUN pip3 install -r ./requirements.txt
COPY ./Scores.txt ./MainScores.py ./Utils.py ./templates ./
CMD python ./MainScores.py