FROM python:3.12-bookworm

RUN python -m pip install pyefd matplotlib scikit-learn awkward
COPY figure5.py .

CMD [ "python", "figure5.py" ]
