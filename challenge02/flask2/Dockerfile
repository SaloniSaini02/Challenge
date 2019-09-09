FROM centos:7
RUN yum -y install epel-release && yum clean all
RUN yum -y install python-pip && yum clean all
RUN yum -y install python-devel && yum clean all
RUN yum -y groupinstall 'development tools' && yum clean all
COPY . /app
WORKDIR /app
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN yum install -y python-pandas
RUN pip list
CMD [ "python", "./Flask-App.py" ]
