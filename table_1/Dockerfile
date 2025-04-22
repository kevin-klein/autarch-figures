FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

RUN pip install prettytable

COPY  ./scripts ./scripts

CMD [ "python", "scripts/dataset_stats.py", "count_objects_quality" ]
