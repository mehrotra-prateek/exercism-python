FROM python:3.7.4-alpine as base

FROM base as builder

RUN pip install --upgrade pip

ARG work_dir
ENV workdir=${work_dir}

RUN mkdir /install
WORKDIR /install

COPY ${workdir}/requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt

FROM base

ARG work_dir
ENV workdir=${work_dir}

ARG test_file
ENV testfile=$test_file"_test.py"

COPY --from=builder /install /usr/local

COPY . /develop

WORKDIR /develop/${workdir}

CMD ["sh", "-c", "pytest $testfile"]