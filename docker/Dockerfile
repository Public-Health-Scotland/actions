# ------------------------------------------------------------------------------
# PHS reusable R CI image
# - Base: rocker/r-ver
# - Adds: Pandoc, git, qpdf, curl, gpg, rsync
# - Pre-installs: pkgdown, styler, roxygen2, desc, rcmdcheck, covr, xml2, tinytex
# - Installs TinyTeX for package manuals and other PDF output
# - Uses Posit Public Package Manager binaries where available
# ------------------------------------------------------------------------------

FROM rocker/r-ver:4.6.1

ENV DEBIAN_FRONTEND=noninteractive

# Package versions are managed through the repositories associated with the
# pinned Rocker base image rather than being individually pinned here.
# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        pandoc \
        git \
        qpdf \
        curl \
        gpg \
        rsync \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN R -q -e "install.packages( \
      'pak', \
      repos = 'https://r-lib.github.io/p/pak/stable' \
    ); \
    pak::pkg_install(c( \
      'pkgdown', \
      'styler', \
      'roxygen2', \
      'desc', \
      'rcmdcheck', \
      'covr', \
      'xml2', \
      'tinytex' \
    ))"

# Keep this separate because TinyTeX is relatively large and slow to install.
# hadolint ignore=DL3059
RUN R -q -e "tinytex::install_tinytex()"
