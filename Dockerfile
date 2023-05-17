FROM python:3.11-slim

RUN pip install ansible python-dotenv invoke toml \
    && pip cache purne

ADD entrypoint.py /entrypoint.py
RUN chmod +x /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]
CMD ["ansible-playbook"]