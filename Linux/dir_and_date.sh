#!/bin/bash

echo "сортировка по расширению файла"
ls -lX

echo -e "\nсортировка по размеру"
ls -lS

echo -e "\nсортировка по времени изменения"
ls -lt

echo -e "\nсортировку по версиям файлов"
ls -lv

echo -e "\nсортировку в обратном порядке"
ls -lr

curentDate=$(date)
echo -e "\n$curentDate"
