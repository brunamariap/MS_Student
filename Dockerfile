FROM python:latest

LABEL author="Bruna"

WORKDIR /

RUN pip install --upgrade pip

COPY . /

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Adicione o script de inicialização
EXPOSE 8003
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

# Defina o comando CMD para executar o script de inicialização
CMD ["/entrypoint.sh"]