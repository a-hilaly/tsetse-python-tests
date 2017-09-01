#!/bin/bash

#JSON PARSER for pkg configurations


function _extract_from_json () {
    file=$1
    target=$2
    res=$(cat $file | jq -r ".$target")
    echo "$res"
}

_CONFIGFILE=$CI_BASICTESTS_PATH/pkg/config/config.json

function ci_cfg () {
    tar=$1
    star=$2
    sstar=$3
    if [ -z sstar ]; then
        res=$(cat $_CONFIGFILE | jq -r "[0].$tar.$star.$ss_tar.")
    elif [-z star ]; then
        res=$(cat $_CONFIGFILE | jq -r ".$tar.$star")
    elif [ -z tar ]; then
        res=$(cat $_CONFIGFILE | jq -r ".$tar")
    fi
    echo "$res"
}

_PROJECT=$(ci_cfg project)
_LOAD_GITHUB_CONFIG=$(ci_cfg github_config load)

if [ "$_LOAD_GITHUB_CONFIG" = 1 ]; then
    _GITHUB_USER=$(ci_cfg github_config logs user)
    _GITHUB_PASSWORD=$(ci_cfg github_config logs user)
fi

_GITHUB_WORKING_ORG=$(ci_cfg github_config working_on organisation)
_GITHUB_WORKING_REP=$(ci_cfg github_config working_on repository)

TRAVIS_CI_CONFIGURATION=$(ci_cfg configured-ci travis-ci)
CIRCLE_CI_CONFIGURATION=$(ci_cfg configured-ci circle-ci)
PKG_CONFIG_RT=$(ci_cfg pkg_config run_tests)
PKG_CONFIG_WO=$(ci_cfg pkg_config run tests)


$@
