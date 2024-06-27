class calculator():
    def __init__(self,name):
        print('','-'*(44 + len(name)))
        print('| Welcome,',name,'for using the Console calculator |')
        print('','-'*(44 + len(name)))
        self.cal_look()

    def calculate(self,equation):
        answer = str(eval(equation))
        print(' '*15,'-'*(len(answer) +2))
        print('Your answer is |', answer,'|')
        print(' '*15,'-'*(len(answer) +2))
        val = input('Now you work calculate again...(y/n) or else press enter:')
        if val =='y' or val =='Y' or val == '':
            self.cal_look()
        else:
            del self

    def cal_look(self):
        try:
            equation = input('Enter Your operation:')
            self.calculate(equation)
        except:
            print(f"'{equation}'is not valid to operate the equation")
            print('Enter Only Valid number and symbol')
            self.cal_look()
    
    def __del__(self):
        print('Thank you for using the console calculator')

if __name__ == "__main__":
    user = input('Enter Your Name:')
    if user == '':
        user = 'User'
    calculator(user)
    