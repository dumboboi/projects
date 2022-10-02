from numpy import array
m=array([[" "]*3]*3)

def restart_game(m):
    for i in range(3):
        for j in range(3):
            m[i,j]=" "

def Fill_square( m , s , v ):
    if (s==1):
        m[0,0] = v
    elif (s==2):
        m[0,1]=v
    elif (s==3):
        m[0,2]=v
    elif (s==4):
        m[1,0]=v
    elif (s==5):
        m[1,1]=v
    elif (s==6):
        m[1,2]=v
    elif (s==7):
        m[2,0]=v
    elif (s==8):
        m[2,1]=v
    elif (s==9):
        m[2,2]=v
def R_diag_check( m , c):
    ch=""
    for i in range(3):
        ch+=m[i,i]
    if (c=="X"):
        return ch=="XXX"
    else:
        return ch=="OOO"
def L_diag_check( m , c):
    ch=""
    j=2
    for i in range(3):
        ch+=m[i,j]
        j-=1
    if (c=="X"):
        return ch=="XXX"
    else:
        return ch=="OOO"
def line_check( m , c , l ):
    ch=""
    for j in range(3):
        ch+=m[l,j]
    if (c=="X"):
        return ch=="XXX"
    else:
        return ch=="OOO"
def column_check( m, c, col):
    ch=""
    for i in range(3):
        ch+=m[i,col]
    if (c=="X"):
        return ch=="XXX"
    else:
        return ch=="OOO"

def Game_Status( m ):
    PL = True
    if PL:
        if (L_diag_check(m,"O") or R_diag_check(m,"O")):
            print("-------------------------------------------------------------                    ------------------------------------------------------------------------------------")
            print("                                                             |-> PLAYER 2 WON <-|         ")
            print("-------------------------------------------------------------                    ------------------------------------------------------------------------------------")
            PL = False
        elif (L_diag_check(m,"X") or R_diag_check(m,"X")):
            print("-------------------------------------------------------------                    ------------------------------------------------------------------------------------")
            print("                                                             |-> PLAYER 1 WON <-|         ")
            print("-------------------------------------------------------------                    ------------------------------------------------------------------------------------")
            PL = False
        else:
            i=0
            while (i<3):
                if (line_check( m , "O",  i) or column_check( m , "O",i )):
                    print("-------------------------------------------------------------                    ------------------------------------------------------------------------------------")
                    print("                                                             |-> PLAYER 2 WON <-|         ")
                    print("-------------------------------------------------------------                    ------------------------------------------------------------------------------------")
                    PL = False
                elif (line_check( m, "X" , i)or column_check(m,"X",i)):
                    print("-------------------------------------------------------------                    ------------------------------------------------------------------------------------")
                    print("                                                             |-> PLAYER 1 WON <-|         ")
                    print("-------------------------------------------------------------                    ------------------------------------------------------------------------------------")
                    PL = False
                i+=1
    return PL

def check_empty( m):
    ok=False
    i=0
    while (i<3) and not(ok):
        j=0
        while (j<3) and not(ok):
            if (m[i,j]==" "):
                ok=True
            j+=1
        i+=1
    return ok

def PRINT_XO(m):
    for i in range(3):
        for j in range(3):
            if (j==0):
                print('                                                                ',m[i,j],end="")
            else:
                print(' |',m[i,j],end="")
        print('\n')


def valid_square( m , s):
    val=True
    if (s==1):
        if(m[0,0]!=" "):
           val = False
    elif (s==2):
        if(m[0,1]!=" "):
            val = False
    elif (s==3):
        if(m[0,2]!=" "):
            val = False
    elif (s==4):
        if(m[1,0]!=" "):
            val = False
    elif (s==5):
        if(m[1,1]!=" "):
            val = False
    elif (s==6):
        if(m[1,2]!=" "):
            val = False
    elif (s==7):
        if(m[2,0]!=" "):
            val = False
    elif (s==8):
        if(m[2,1]!=" "):
            val = False
    elif (s==9):
        if(m[2,2]!=" "):
            val = False
    return val

def Game(m):
    sq="X"
    c=1
    G_ST = True
    while (G_ST):
        v=input("                                                           Enter a square (1..9): ")
        while not("1"<=v<="9") or not(valid_square(m,int(v))):
            print("                                                          !! ENTER A VALID SQUARE !! ")
            v=input('                                                                      ')
        Fill_square(m,int(v),sq)
        PRINT_XO(m)
        print('                                                          -------------------------')
        c = c* -1
        if (c>0):
            sq="X"
        else:
            sq="O"
        G_ST = Game_Status(m)
        if ((not(check_empty(m))) and (G_ST)) :
            print("-------------------------------------------------------------       DRAW         -------------------------------------------------------------------------------------")
            G_ST = False

def PLAY():
    print('                                                                 WELCOME :D\n')
    PRINT_XO(m)
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    PL = True
    while (PL):
        Game(m)
        AN=input('                                                              KEEP PLAYING?(Y/N): ')
        while (AN.upper()!='Y' and AN.upper()!='N'):
            AN=input("                                                       Press Y/y for Yes - N/n for No : ")
        if (AN.upper()=='N'):
            PL = False
        else:
            restart_game(m)
            PRINT_XO(m)

    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')
    print('                                                            <3  THANKS FOR PLAYING <3                                           \n')
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')

PLAY()
