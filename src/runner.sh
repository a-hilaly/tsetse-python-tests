#!/bash/bin

function execute_commands () {
   $1
}

function execute_scripts () {
   bash $1
}

$1
