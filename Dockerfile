FROM python:3.8

# dossier de travail
WORKDIR /code

# dependances
COPY requirements.txt .
COPY streamlite.py .
COPY lovoo_v3_users_api-results.csv .
# installer les dependances
RUN pip install -r requirements.txt


ENTRYPOINT ["streamlit","run","streamlite.py"]
# start 
CMD streamlit run streamlite.py