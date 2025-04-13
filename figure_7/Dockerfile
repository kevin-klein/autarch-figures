FROM python:3.12-bookworm

RUN apt update
RUN apt install ruby --yes

RUN pip install matplotlib numpy pandas

COPY ./experiment ./experiment
COPY analyze.rb .
COPY box_plot.py .
COPY user_map.json .
COPY run.sh .

CMD ["sh", "run.sh"]
