This repository lists various scripts that are useful while working with XLD

exposeDeploymentVariables.ftl
=============================
The code snippet in this script can be copied into a script that is used with XLD artifacts as a createScript. It can be used with generic plugin and with XL-rules and any other plugins that have execution scripts specified such that they show up under plan analyzer can be opened.

This script would expose all the variables and the properties with them. It works recursively so you can specify the what level of depth you want to go to.
eg.

base depth is 0. so with depth=1, it will show properties like deployed.container.os.

It prints the value of literal properties, also lists the methods available with objects is captureMethod=true. 