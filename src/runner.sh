#!/bash/bin

function execute_commands () {
   printenv
}

function execute_scripts () {
   bash $1
}

execute_commands
