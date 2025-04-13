FROM python:3.12-bookworm

RUN python -m pip install basemap adjustText contextily cartopy basemap-data-hires
COPY map.py .

CMD [ "python", "map.py" ]
