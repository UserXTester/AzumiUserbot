# Using Python Slim-Buster
FROM biansepang/weebproject:buster

# Clone repo and prepare working directory
RUN git clone -b main https://github.com/levina-lab/AzumiUserbot /home/azumiuserbot/ \
    && chmod 777 /home/azumiuserbot \
    && mkdir /home/azumiuserbot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/azumiuserbot/

# Setup Working Directory
WORKDIR /home/azumiuserbot/

# Finalization
CMD ["python3","-m","userbot"]
