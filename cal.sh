#!/bin/bash

read num1 < num1.txt
read num2 < num2.txt
let Add=$num1+$num2                                                                                                                                          let Sub=$num1-$num2                                                                                                                                          let Mul=$num1*$num2                                                                                                                                          let Div=$num1/$num2 

if [ $# -lt 1 ]; then                                                                                                                                         echo "...none operator parameter...."
 PS3="select menu: "
 select op in "add" "sub" "div" "mul"
 do
    echo
    echo 'num1: '$num1
    echo 'num2: '$num2
    case $op in
    add) echo "op: add"
      echo "result: "$Add;;
    sub) echo "op: sub"
     echo "result: "$Sub;;
    div) echo "op: div"
     echo "result: "$Div;;
    mult) echo "op:mul"
     echo "result: "$Mul;;
    esac  
    break
 done
 
else
 echo
 echo 'num1: '$num1
 echo 'num2: '$num2
 case $1 in
  add) echo "op: add"
    echo "result: "$Add;;
  sub) echo "op: sub"
    echo "result: "$Sub;;
  div) echo "op: div"
    echo "result: "$Div;;
  mul) echo "op:mul"
    echo "result: "$Mul;;
esac
fi



