class Manipulator:
    state = [
        "             |             ",
        "================",
        " |           |             ",
        "/ \          |             ",
        "             |             ",
        "             |             ",
        "             |             ",
        "             |             ",
    ]
         
    kr_d = False
    kr_g = True
    kr_l = True
    kr_p = False
    kr_o = True
    kr_z = False
    chwytak = False
    w_gore = False
    w_dol = False
    w_lewo = False
    w_prawo = False
    start = False
    stop = False
    
    MAX_Y_LVL = 5
    MIN_Y_LVL = 1
    MAX_X_LVL = 10
    MIN_X_LVL = 1
    
    arm_y = 1
    arm_x = 1
    message = ""
    
    def __str__(self) -> str:
        output = "\n".join(self.state)
        output += '\nmessage:' + str(self.message)
        output += '\nkr_d:' + str(self.kr_d)
        output += '\nkr_g:' + str(self.kr_g)
        output += '\nkr_l:' + str(self.kr_l)
        output += '\nkr_p:' + str(self.kr_p)
        output += '\nkr_o:' + str(self.kr_o)
        output += '\nkr_z:' + str(self.kr_z)
        output += '\nw_gore:' + str(self.w_gore)
        output += '\nw_dol:' + str(self.w_dol)
        output += '\nw_lewo:' + str(self.w_lewo)
        output += '\nw_prawo:' + str(self.w_prawo)
        output += '\nstart:' + str(self.start)
        output += '\nstop:' + str(self.stop)
        output += '\nchwytak:' + str(self.chwytak)
        output += '\narm_x:' + str(self.arm_x)
        output += '\narm_y:' + str(self.arm_y)
        return output
    
    def make_move(self):
        if self.w_gore == True: 
            self.go_up()
        
        if self.w_dol == True:
            self.go_down()
        
        if self.w_lewo == True: 
            self.go_left()
        
        if self.w_prawo == True: 
            self.go_right()
        
        if self.chwytak == True: 
            self.close_gripper()
        else: self.open_gripper()
    
    def close_gripper(self):
        self.state[self.arm_y+2] = self.state[self.arm_y+2].replace("/ \\", "| |")
        self.kr_o = False
        self.kr_z = True
    
    def open_gripper(self):
        self.state[self.arm_y+2] = self.state[self.arm_y+2].replace("| |", "/ \\")
        self.kr_o = True
        self.kr_z = False
    
    def go_down(self):
        if self.arm_y < self.MAX_Y_LVL:
            replaced_level = self.arm_y + 3
            segment = self.state.pop(replaced_level)
            self.state.insert(0, segment)
            self.arm_y += 1
            self.kr_g = False
        else: self.kr_d = True
            
    def go_up(self):
        if self.arm_y > self.MIN_Y_LVL:
            segment = self.state.pop(0)
            self.state.append(segment)
            self.arm_y -= 1
            self.kr_d = False
        else: self.kr_g = True
    
    def go_right(self):
        if self.arm_x < self.MAX_X_LVL:
            for x in range (self.arm_y, self.arm_y+3):
                char_list = list(self.state[x])
                symbol = char_list.pop(12)
                char_list.insert(0, " ")
                if symbol == "=": char_list.insert(12, "=")
                self.state[x] = "".join(char_list)
            self.arm_x += 1
            self.kr_l = False
        else: self.kr_p = True
            
    def go_left(self):
        if self.arm_x > self.MIN_X_LVL:
            for x in range (self.arm_y, self.arm_y+3):
                char_list = list(self.state[x])
                char_list.pop(0)
                if x != self.arm_y: char_list.insert(12, " ")
                self.state[x] = "".join(char_list)
            self.arm_x -= 1
            self.kr_p = False
        else: self.kr_l = True
            
