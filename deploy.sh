cp .env.prod .env
git add .
git commit -m "deploy"
git push origin main
eb deploy