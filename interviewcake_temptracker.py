"""Write a class TempTracker with these methods:

insert()
get_max()
get_min()
get_mean()
get_mode()
Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.

get_mean() should return a float, but the rest of the getter methods can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..110.

If there is more than one mode, return any of the modes."""

class TempTracker(object):
    def __init__(self,temp_list=None):
        #self.new_temp = new_temp
        #self.temp_list = temp_list
        if temp_list is None:
            self.temp_list = []
        else:
            self.temp_list = temp_list

    def insert(self, new_temp):
        print "SELF.TEMPLIST IS " + str(type(self.temp_list)) # WHY IS THIS NOT A LIST?
        self.temp_list.append(new_temp)
        return temp_list

    def get_max(self):
        return max(temp_list) # O(n) operation

    def get_min(self):
        return min(temp_list) # O(n) operation

    def get_mean(self): # O(n) operation
        sum_temps = 0
        for i in self.temp_list:
            sum_temps += i
        return float(sum_temps/len(self.temp_list))

    def get_mode(self): # what if no most common? or if it's tied?
        mode_dict = {}
        
        for temp in self.temp_list:
            if temp not in mode_dict:
                mode_dict[temp] = 1
            else:
                mode_dict[temp] += 1
        mode_value = max(mode_dict.values())
        for temp_key in mode_dict:
            if mode_dict[temp_key] == mode_value:
                return temp_key

new_tracker = TempTracker("new")
new_tracker.insert(47)
new_tracker.insert(50)
new_tracker.insert(47)
new_tracker.insert(58)

print new_tracker.temp_list



