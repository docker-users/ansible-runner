FROM python:3.11-slim

RUN pip install ansible \
        python-dotenv \
        invoke

# ENTRYPOINT ["/bin/bash"]
CMD ["ansible-playbook"]