public int reverse(int x)
{//x=332
    int result = 0;

    while (x != 0)
    {//tail = 2
        int tail = x % 10;
        //newResult=0*10+2=2
        int newResult = result * 10 + tail;
        if ((newResult - tail) / 10 != result){
         return 0;
        }
        //result=2
        result = newResult;
        //x=332/10=33 loop continues
        x = x / 10;
    }

    return result;
}