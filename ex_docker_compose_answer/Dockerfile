# Partir de l'image python:3.6-alpine
FROM python:3.6-alpine

# Copier le fichier requirements.txt dans le conteneur dans /app
ADD requirements.txt /app/

# Installer les packages de /app/requirements.txt grâce à la commande pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exécuter par défaut un serveur HTTP basique
CMD ["python", "-m", "http.server"]