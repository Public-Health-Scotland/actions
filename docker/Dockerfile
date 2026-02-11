FROM rocker/r-ver:latest

# Install system packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        pandoc \
        pandoc-citeproc \
        git \
        qpdf \
        curl \
        gpg \
        rsync && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install R packages you use in multiple workflows
RUN R -e "install.packages(c('pkgdown', 'styler', 'roxygen2', 'desc', 'rcmdcheck', 'covr', 'xml2'))"

# Keep the image lean
RUN rm -rf /var/lib/apt/lists/*
