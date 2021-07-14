FROM biansepang/weebproject:buster

RUN git clone -b main https://github.com/levina-lab/AzumiUserbot /home/azumiuserbot/ \
    && chmod 777 /home/azumiuserbot \
    && mkdir /home/azumiuserbot/bin/

COPY ./sample_config.env ./config.env* /home/azumiuserbot/

WORKDIR /home/azumiuserbot/

RUN pip3 install -r https://raw.githubusercontent.com/levina-lab/AzumiUserbot/main/requirements.txt

CMD ["python3","-m","userbot"]
