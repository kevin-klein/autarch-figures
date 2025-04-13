FROM python:3.12-bookworm

RUN python -m pip install scipy numpy matplotlib scikit-learn

COPY *.json .
COPY grave_orientation.py .
COPY run.sh .

CMD [ "sh", "run.sh" ]

