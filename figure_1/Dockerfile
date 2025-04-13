FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime

COPY  ./scripts ./scripts

CMD [ "python", "scripts/create_ml_result_image.py", "scripts/dobes_2013_page_13.png", "output/result.png" ]
