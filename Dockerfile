FROM public.ecr.aws/lambda/python:3.12 

RUN mkdir -p /app
COPY ./mainLogistics.py /app/
COPY ./mainWiki.py /app/
COPY mylib/ /app/mylib/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD ["python", "mainWiki.py"]