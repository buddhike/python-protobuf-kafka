FROM public.ecr.aws/lambda/python:3.8

COPY *.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["main.handler"]
