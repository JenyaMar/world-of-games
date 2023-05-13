FROM python:3.11-slim
RUN pip install -r requirements.txt
COPY Scores.txt \
     MainScores.py \
     Utils.py \
     templates \
     /Users/jenyamartemyanov/PycharmProjects/chromedriver_mac64/chromedriver \
     ./
CMD python MainScores.py