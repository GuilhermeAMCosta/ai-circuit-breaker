#!/usr/bin/env bash
export SRC_PATH="$( dirname "${BASE_SOURCE[0]}" )"

export $(cat $SRC_PATH/.env-dev | xargs)