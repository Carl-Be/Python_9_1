"""
Carl Bechie
CIS 185
ex 9.1
"""


class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)


    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
        
    # Write method definitions here
   
    def __eq__(self, other):
        """Returns equal to inequality comparision"""

        return self.getName() == other.getName()


    def __lt__(self, other):
        """Returns less than inequality comparision"""

        return self.getName() < other.getName()

   
    def __ge__(self, other):
      """Returns greater than or eaual to inequality comparision"""

      return self.getName() >= other.getName() 

def main():
    """A simple test."""
    studentOne = Student("Carl", 5)
    studentTwo = Student("Ken", 7)
    studentThree = Student("Carl", 5)
    
    print("EQ: ", studentOne == studentThree)
    print("LT: ", studentOne < studentTwo)
    print("GE: ", studentOne >= studentThree)

if __name__ == "__main__":
    main()