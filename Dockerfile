FROM vckyouuu/geezprojects:buster

# movecrew/one4ubot:alpine-latest

RUN mkdir /AzumiUserbot && chmod 777 /AzumiUserbot
ENV PATH="/AzumiUserbot/bin:$PATH"
WORKDIR /AzumiUserbot

RUN git clone https://github.com/levina-lab/AzumiUserbot -b main /AzumiUserbot

#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /AzumiUserbot/

#
# Make open port TCP
#
EXPOSE 80 443

#
# Finalization
#
CMD ["python3","-m","userbot"]
