# pip freeze > requirements.txt
# remove pypiwin32==223 from requirements.txt
# remove pywin32==306 from requirements.txt

cp .env.prod .env
git add .
git commit -m "deploy"
git push origin main
eb deploy