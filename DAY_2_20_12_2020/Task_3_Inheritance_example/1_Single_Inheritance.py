class account:
    def __init__(self,acc_num,name):
        self.acc_num = acc_num
        self.name = name
    def acc_details(self):
    	print("Account number : ",self.acc_num)
    	print("Account holder name : ",self.name)

class savings_account(account):
	def __init__(self,acc_num,name,int_rate,acc_type):
		self.int_rate = int_rate
		self.acc_type = acc_type
		account.__init__(self,acc_num,name)
	def acc_type_details(self):
	    print("Account Type : ",self.acc_type)
	    print("Interest rate : ",self.int_rate)

acc1 = savings_account(1234,"Joey",3.0,"Savings Bank")

acc1.acc_details()
acc1.acc_type_details()