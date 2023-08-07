# Hello, tired of useless instagram notifications that your mate "liked" your message? Right door ! 

Here we will make a python automation which will delete those notifications off your Android device every 2 hours, let's go ! 

## Context

Here's how we'll proceed : we'll access the phone through ADB and read notifications, 
when "liked" is encountered, the whole line (which is the whole notification is deleted)
we'll use an infinite loop + the sleep feature of the time library to add an interval
which will result in running the script every two hours (every 7200 seconds)
