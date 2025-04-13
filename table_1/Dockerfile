FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

COPY  ./scripts ./scripts
COPY  ./training_data ./training_data

CMD [ "python", "scripts/dataset_stats.py", "count_objects_quality" ]
