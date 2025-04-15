FROM python:3.12-bookworm

RUN apt install curl
RUN python -m pip install scipy numpy matplotlib scikit-learn

COPY grave_orientation.py .
COPY run.sh .

CMD [ "sh", "run.sh" ]

