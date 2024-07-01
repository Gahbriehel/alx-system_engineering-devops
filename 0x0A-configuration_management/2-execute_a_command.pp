# This script kills a process called killmenow
exec {'killmenow':
    command => '/usr/bin/pkill -f killmenow'
}
