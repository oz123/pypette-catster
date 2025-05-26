###
#  general configuration of the makefile itself
###
SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY: help
help:
	@mh -f $(MAKEFILE_LIST) $(target) || echo "Please install mh from https://github.com/oz123/mh/releases"
ifndef target
	@(which mh > /dev/null 2>&1 && echo -e "\nUse \`make help target=foo\` to learn more about foo.")
endif

PACKAGENAME ?= catster 
VERSION := $(shell python -m setuptools_scm)
REGISTRY ?= docker.io
IMG ?= $(shell basename $(CURDIR))
OPTS :=
ORG := oz123
TAG := $(subst +,-,$(VERSION))
DIST_FILE := dist/$(PACKAGENAME)-$(VERSION).tar.gz

ifneq (,$(wildcard ./.env))
include .env
	export
endif

$(DIST_FILE):
	echo "Build source dist for $(VERSION)"
	python -m build -s

sdist: $(DIST_FILE) ## build a source distribution

docker-build: sdist
	@echo "Building docker image with version $(VERSION)"
	pipenv requirements --categories default,deploy> requirements.txt
	docker build -t $(REGISTRY)/$(ORG)/$(IMG):$(TAG) --build-arg VERSION=$(VERSION) -f docker/Dockerfile .

docker-run:
	docker run --env-file .env -it --rm -p 8080:8080 $(REGISTRY)/$(ORG)/$(IMG):$(TAG) $(OPTS)
