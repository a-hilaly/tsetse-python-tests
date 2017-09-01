#!/bash/bin


function _pre_compile () {
    srcc=$1
    source $srcc
    echo "[INFO] ... Sourcing pre "
}

function _execute_script_shell () {
    echo "[INFO] ... Starting executing"
    bash $CI_BASICTESTS_PATH/src/runner.sh --script $1
}

function _execute_command_shell () {
    bash $CI_BASICTESTS_PATH/src/runner.sh --command $1
}

function _execute_script_pythonic () {
    echo "[INFO] ... Starting executing"
    python $CI_BASICTESTS_PATH/src/pyrunner.py --file $1
}

function _execute_command_pythonic () {
    python $CI_BASICTESTS_PATH/src/pyrunner --command $1
}


# Choose python or shell running mode
_RMODE=$1
_ORDER_TYPE=$2
_TARGET=$3

if [ $_ORDER_TYPE = "command" ] || [ $_ORDER_TYPE = "cmd" ]; then
    if [ $_RMODE = "python" ]; then
        _execute_command_pythonic $_TARGET
    elif [ $_RMODE = "shell" ]; then
        _execute_command_shell $_TARGET
    fi
elif [ $_TARGET ] || []; then
    if [ $_RMODE = "python" ]; then
        _execute_script_pythonic $_TARGET
    elif [ $_RMODE = "shell" ]; then
        _execute_script_shell $_TARGET
    fi
fi
