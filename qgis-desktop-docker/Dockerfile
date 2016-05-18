FROM ubuntu:trusty
MAINTAINER Alessandro Pasotti<apasotti@itopen.it>

# Add repository for QGIS
ADD debian-gis.list /etc/apt/sources.list.d/debian-gis.list
# Add the signing key
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key 3FF5FFCAD71472C4

# Install required dependencies and QGIS itself
RUN apt-get -y update
RUN apt-get install -y \
    vim \
    python-qgis \
    qgis \
    xvfb \
    python-pip \
    python-dev \
    supervisor

# Add install script
ADD requirements.txt /usr/local/requirements.txt
ADD install.sh /usr/local/bin/install.sh
RUN chmod +x /usr/local/bin/install.sh
RUN /usr/local/bin/install.sh

# Add qgishome with settings for the testing script
COPY qgishome /qgishome

# Add QGIS test runner
ADD qgis_testrunner.py /usr/bin/qgis_testrunner.py
RUN chmod +x /usr/bin/qgis_testrunner.py


# Add start script
ADD supervisord.conf /etc/supervisor/
ADD supervisor.xvfb.conf /etc/supervisor/supervisor.d/

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
