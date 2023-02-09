#!/usr/bin/env python
# coding: utf-8

# In[1]:


from constraint import *
def seating_arrangement_before():
    """" Returns solutions to beore seating arrangement with constraint """
    people = ['Alice', 'Bob', 'Charlie', 'Darek', 'Eliza', 'Frank']    # list of people in our problem
    problem = Problem()    # Assigning Problem() class to a variable named problem
    problem.addVariables(people, list(range(6)))   # Adding variables with domain values
    problem.addConstraint(AllDifferentConstraint())   # AllDifferentConstraint makes sure that every single variable and domain are different
    problem.addConstraint(lambda a, b: a == (b+1)%6 or a == (b-1)%6, ('Alice', 'Bob')) # lambda function to specify constraint condition
    problem.addConstraint(lambda c, d: c != (d+1)%6 and c != (d-1)%6, ('Charlie', 'Darek')) # lambda function to specify constraint condition
    problem.addConstraint(lambda a, e: a == (e+3)%6, ('Alice', 'Eliza')) # lambda function to specify constraint condition
    return problem.getSolutions()

def seating_arrangement_after():
    """" Returns solutions to after seating arrangement with constraint """
    people = ['Alice', 'Bob', 'Charlie', 'Darek', 'Eliza', 'Frank'] # list of people in our problem
    problem = Problem() # Assigning Problem() class to a variable named problem
    problem.addVariables(people, list(range(6)))     # Adding variables with domain values 
    problem.addConstraint(AllDifferentConstraint()) # AllDifferentConstraint makes sure that every single variable and domain are different
    problem.addConstraint(lambda a, b: a == (b+1)%6 or a == (b-1)%6, ('Alice', 'Bob')) # lambda function to specify constraint condition
    problem.addConstraint(lambda c, d: c != (d+1)%6 and c != (d-1)%6, ('Charlie', 'Darek')) # lambda function to specify constraint condition
    problem.addConstraint(lambda f, e: f == (e+3)%6, ('Frank', 'Eliza')) # lambda function to specify constraint condition
    return problem.getSolutions()

print('The total number of arrangements before dinner is {} \n'.format(len(seating_arrangement_before()))) # prints number of solutions before dinner
print('The total number of arrangements after dinner is {} \n'.format(len(seating_arrangement_after()))) # prints number of solution after dinner


# In[2]:


seating_arrangement_before()


# In[3]:


seating_arrangement_after()


# In[ ]:




