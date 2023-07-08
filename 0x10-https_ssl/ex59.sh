#!/bin/bash
JUST_A_SECOND=1
funky ()
{
    echo "this is a funky function."
    echo "Now exiting funky function."
}
funky

fun ()
{
    i=0
    REPEATS=30
    echo
    echo "And now the fun really begins."
    echo
    sleep $JUST_A_SECOND
    while [ $i -lt $REPEATS ]
    do 
        echo "Don't let the past decide your future."
        echo "Make sure what comes next is what you do today."
        echo "Don't ever give up and move forward."
        let "i+=1"
    done
}
fun
exit