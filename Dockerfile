FROM movecrew/one4ubot:alpine-latest

RUN mkdir /AzumiUserbot && chmod 777 /AzumiUserbot
ENV PATH="/One4uBot/bin:$PATH"
WORKDIR /AzumiUserbot

RUN git clone https://github.com/levina-lab/AzumiUserbot -b sql-extended /AzumiUserbot

#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /One4uBot/

#
# Make open port TCP
#
EXPOSE 80 443

#
# Finalization
#
CMD ["python3","-m","userbot"]
