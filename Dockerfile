FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirement.txt /code/
RUN pip install https://github.com/darklow/django-suit/tarball/v2 & pip install -r requirement.txt
COPY . /code/
EXPOSE 7000
CMD ["/code/run.sh"]
