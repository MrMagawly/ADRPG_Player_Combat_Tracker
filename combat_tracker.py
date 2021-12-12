


class Tracker:
    
    def __init__(self, hp, ar, sk):
        self.max_health = int(hp)
        self.max_armor = int(ar)
        self.max_soak = int(sk)
        self.current_health = self.max_health
        self.current_armor = self.max_armor
        self.current_soak = self.max_soak
    
    def __repr__(self):
        self.str_rep = 'stats: H[{}/{}] A[{}/{}] S[{}/{}]\n'.format(self.current_health, self.max_health,
                                                                    self.current_armor, self.max_armor,
                                                                    self.current_soak, self.max_soak)
        if self.current_health <= 0 and self.current_health > -10:
            self.str_rep += 'IMMOBILIZED!\n'
        
        if self.current_health <= -10:
            self.str_rep += 'DEAD!\n'
        
        return self.str_rep
    
    #Takes care of the damage, armor, and soak caculations.
    def damage(self, dam, soak_dam=0):
        if soak_dam <= 0:
            soak_dam = dam

        self.current_soak -= soak_dam

        while self.current_soak <= 0:
            if self.current_armor > 0:
	            self.current_armor -= 1
            self.current_soak += self.max_soak

        if dam > self.current_armor:
            self.current_health -= dam - self.current_armor
    
    # Returns a tuple containing the max values of each stat.
    def get_max_stats(self):
        return (self.max_health, self.max_armor, self.max_soak)
    
    # Returns a tuple of the current value of each stat.
    def get_stats(self):
        return (self.current_health, self.current_armor, self.current_soak)
    
    # Increases current_health by the value passed to amount. 
    def heal(self, amount):
        if amount < 0:
            amount = 0
            
        self.current_health += amount
        
        if self.current_health > self.max_health:
            self.current_health = self.max_health
    
    # Sets the current stats values to the max_values.
    def reset_stats(self):
        self.current_health = self.max_health
        self.current_armor = self.max_armor
        self.current_soak = self.max_soak
    
    # Sets the current stats to the values of the arguments,
    # and prevents the current values from exceeding the max_values.
    def set_current_stats(self, hp, ar, sk):
        self.current_health = hp
        self.current_armor = ar
        self.current_soak = sk
        
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        
        if self.current_armor > self.max_armor:
            self.current_armor = self.max_armor
        
        if self.current_soak > self.max_soak:
            self.current_soak = self.max_soak
    
    def set_max_stats(self, hp, ar, sk):
        self.max_health = hp
        self.max_armor = ar
        self.max_soak = sk
        self.current_health = self.max_health
        self.current_armor = self.max_armor
        self.current_soak = self.max_soak
