FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

RUN pip install --upgrade pip

# __pychache__ を出力しない
# .env ファイルに移動
#ENV PYTHONDONTWRITEBYTECODE=1

# 必要なライブラリをインストール
COPY ./app/requirements.txt .
RUN pip install -r ./requirements.txt
