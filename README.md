# Longest-Subsrting-without-repeating-
we use the sliding window with a hashset to store the substring, and making two pointer to iterate the string to check the valid substring without repeating.

# Apporach to solve the problem 
1. we make the  empty hasset to store the unique letter of the string to get result,we use hashset because hashet follow the property of set to store the unique character  and  make variable ans=1.
2. then add the first char of string to set by assuming it unoque .
3. then make two iterater pointer i=0 from start index and j=1 from 1 index to traverse the string till last.
4.apply the while loop by check the condition and run till the given get false
5.use nested while to check the inner while condtion after outer loop get true, inner while loop check the condtion that after traversing the char are in the seet or not
6. If the  char in set then remove s[i] form set and  make i one step ahead by i=i+1
7. if if false then add the s[j] into set and make j =j+1 here we move the j pointer to next char
8. we run the loop till condtion false and get the ans
9. return the ans by max of ans and j-i means after traverse we get the unique char len like "abcabcbb", we get i=0 and j=3 and our condtion get false then we return the len of j-i
10. j=3 and i=0 3-0=3
11. so the answer is 3

# space complexit use to solve is O(n) by using extra spce hashset to store unique char

# time complexity O(n) 

#   DRY RUN
   ----------

   we have s="abcabcbb"
   step1 :
   
   i=0 and j=0
   set1={a} <<<< we set set1[0]=s[0]
   check j <n <<<< True 
   then  check s[j] in set1 <<<< it give True 
   i+=1
   ans =1 # lenght of srting to get final ans


   step2:

  i=0 and j=1
   set1={a,b} <<<< we set set1[0]=s[0]
   check j <n <<<< True 
   then  check s[j] in set1 <<<< it give False 
   we add set1 me "b"
   and j+=1
   ans =2

   step 3:

  i=0 and j=2
   set1={a,b} 
   check j <n <<<< True 
   then  check s[j] in set1 <<<< it give False 
   j+=1
   we add "c" in set1 
   ans =3

   step 4:
    i=1 and j=3
   set1={'a'} <<<< we set set1[0]=s[0]
   check j <n <<<< True 
   then  check s[j] in set1 <<<< it give True 
   i+=1

   step 5:
   
  i=2 and j=4
   set1={'a'} <<<< we set set1[0]=s[0]
   check j <n <<<< True 
   then  check s[j] in set1 <<<< it give True 
   i+=1

   again we get same result until end of string because repeated char comes then final result is "abc" and its lengh is 3.
   
   
