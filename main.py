DOCKERFILE_CONTENT="
FROM python:3
RUN pip install numpy scipy pandas
CMD [\"python\", \"./main.py\"]
"
echo "$DOCKERFILE_CONTENT" > Dockerfile
HASH_OUTPUT=$(sha1sum Dockerfile | awk '{print $1}')
echo "$HASH_OUTPUT Dockerfile"
