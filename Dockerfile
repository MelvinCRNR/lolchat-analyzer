FROM python:3.10.9
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5002
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]