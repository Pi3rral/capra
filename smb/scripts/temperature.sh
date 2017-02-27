#!/bin/bash

function send_temp {
    ELEMENT=$1
    TEMP=$2
    #echo "${ELEMENT} = ${TEMP}"
    curl -s -o /dev/null -X POST -H "Content-Type: application/json" -d "{\"temperature\":\"${TEMP}\", \"element\":\"${ELEMENT}\"}" "http://127.0.0.1:8000/smb/temperatures/"
}

CPU_TEMP=`sensors | grep "CPU Temp" | cut -d'+' -f2 | cut -d'.' -f1`
send_temp "CPU" "${CPU_TEMP}"

MB_TEMP=`sensors | grep "MB Temp" | cut -d'+' -f2 | cut -d'.' -f1`
send_temp "MB" "${MB_TEMP}"

C0_TEMP=`sensors | grep "Core 0" | cut -d'+' -f2 | cut -d'.' -f1`
send_temp "Core0" "${C0_TEMP}"

C1_TEMP=`sensors | grep "Core 1" | cut -d'+' -f2 | cut -d'.' -f1`
send_temp "Core1" "${C1_TEMP}"

HDD1_TEMP=`/usr/sbin/hddtemp /dev/sda | cut -d' ' -f4 | sed 's|[^0-9]||g'`
send_temp "HDD1" "${HDD1_TEMP}"

HDD2_TEMP=`/usr/sbin/hddtemp /dev/sdb | cut -d' ' -f4 | sed 's|[^0-9]||g'`
send_temp "HDD2" "${HDD2_TEMP}"
