#!/bash/bin

function execute_commands () {
   printenv
}

function execute_scripts () {
   bash $1
}

function execute_pyrunner () {
   #test if python is here
   python CI_BASICTESTS_PATH/pkg/pyrunner.py
}

execute_commands
