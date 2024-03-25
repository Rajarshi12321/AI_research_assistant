FROM python:3.10-slim

WORKDIR /app

COPY . /app


RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        netbase \
        && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

ARG GEMINI_API_KEY1
ENV GEMINI_API_KEY=$GEMINI_API_KEY1

ARG PINECONE_API_KEY1
ENV PINECONE_API_KEY=$PINECONE_API_KEY1

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]