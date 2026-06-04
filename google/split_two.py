def split_two_types(gems):
     n = len(gems)
     if n%2 != 0 :
         return False

     h = n//2

     totalD = gems.count('D')
     totalR = n - totalD

     if totalD%2 != 0 or totalR%2 !=0:
         return False
     targetD = totalD //2
     targetR = totalR //2

     countD = 0
     countR = 0

     for i in range(h):
         if gems[i] == 'D':
             countD+=1
         else:
             countR+=1
     if countD == targetD and countR == targetR:
         return True

     for i in range(n-h):
         if gems[i] == 'D':
             countD-=1
         else:
             countR-=1

         if gems[i+h] == 'R':
             countR+=1
         else:
             countD+=1

         if countD == targetD and countR == targetR:
             return True
     return False

gems = ['D','R','D','D','R','D','R','R']
print(split_two_types(gems))