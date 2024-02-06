n=100
m=n
while(n>=9){
    sum=0
    while(n>0){
        i=n%10
        sum=sum+i
        n=parseInt(n/10)
    }
    n=sum
}

if (n==1){
    document.write(m+" is lucky Number")
}
else{
    document.write(m+" is UnLucky Number")
}