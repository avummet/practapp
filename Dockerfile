FROM Python:3
maintainer Ananthvummethala

workdir /app
add . /app
RUN pip install -r requirements.txt
CMD ["python", "hello.py"]