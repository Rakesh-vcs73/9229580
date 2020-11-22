"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input

BANANA
Sample Output

Stuart 12
"""


def coun(string,temp):
    count=0
    for i in range(0,len(string)):
        if(string[i]==temp[0]):
            j=1
            q=i+1
            flag=0
            while(j<len(temp)):
                if(q<len(string)):
                    if(string[q]!=temp[j]):
                        flag=1
                else:
                    flag=1        
                q+=1
                j+=1
            if(flag==0):
                count+=1
                    
                
    return count
                

def minion_game(string):
    # your code goes here
    staurt_score=0
    kevin_score=0
    staurt_dic=[]
    kevin_dic=[]
    for j in range(0,len(string)):
        if(string[j]!='A' and string[j]!='E' and string[j]!='I' and string[j]!='O' and string[j]!='U'):
            temp=""
            for i in range(j,len(string)):
                temp+=string[i]
                if(temp not in staurt_dic):
                    staurt_dic.append(temp)
                    #print(temp)
                    staurt_score+=coun(string,temp)
                    #print(staurt_score)
        else:
            temp=""
            for i in range(j,len(string)):
                temp+=string[i]
                if(temp not in kevin_dic):
                    kevin_dic.append(temp)
                    #print(temp)
                    kevin_score+=coun(string,temp)
                    #print(kevin_score)
    if(kevin_score>staurt_score):
        print("Kevin",kevin_score)
    elif(kevin_score<staurt_score):
        print("Stuart",staurt_score)
    else:
        print("Draw")
            
        
        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)