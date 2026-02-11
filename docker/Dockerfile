# ------------------------------------------------------------------------------
# PHS reusable R CI image
# - Base: rocker/r-ver
# - Adds: Pandoc, git, qpdf, curl, gpg, rsync
# - Pre-installs: pkgdown, styler, roxygen2, desc, rcmdcheck, covr, xml2
# - Uses Posit Package Manager (PPM) binaries for speed/reproducibility
# ------------------------------------------------------------------------------

FROM rocker/r-ver:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      pandoc \
      pandoc-citeproc \
      git \
      qpdf \
      curl \
      gpg \
      rsync \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN R -q -e "install.packages('pak', repos = 'https://r-lib.github.io/p/pak/stable')"

RUN R -q -e "pak::pkg_install(c( \
      'pkgdown', \
      'styler', \
      'roxygen2', \
      'desc', \
      'rcmdcheck', \
      'covr', \
      'xml2' \
      'tinytex' \
    ))"

RUN R -q -e "tinytex::install_tinytex()"
