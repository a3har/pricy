FROM python

COPY requirements.txt /scrapyrt/pricy/

WORKDIR /scrapyrt/pricy/

RUN pip install -r requirements.txt

COPY . /scrapyrt/pricy

CMD ["scrapyrt","-i","0.0.0.0"]