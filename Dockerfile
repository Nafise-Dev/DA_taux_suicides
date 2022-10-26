FROM python:3.10

#dossier de travail
WORKDIR /code

#dépendances
COPY requirements.txt .
COPY master.csv .
COPY taux_suicides.py .
#Installe les dépendances
RUN pip3 install -r requirements.txt


ENTRYPOINT [ "streamlit", "run", "taux_suicides.py", "--server.port=8501", "--server.address=0.0.0.0" ]