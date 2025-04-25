FROM python:3.12-bookworm

RUN python -m pip install pyefd matplotlib scikit-learn awkward scikit-image
COPY figure5.py .
COPY format_data.py .

CMD [ "python", "figure5.py" ]
