"""面积计算函数
form：version 0.1.0
"""
def squ_cir(self, r, pi):
        """计算圆面积"""
        squ = r * r
        if pi == 0:
            return f"{squ}π"
        elif 0 < pi <= 10:
            return squ * round(self.pinum, pi)
        else:
            return squ * self.pinum

def squ_square(self, a, b):
        """计算矩形面积"""
        return a * b

def squ_trapezoid(self, a, b, h):
        """计算梯形面积"""
        return (a + b) * h * 0.5

def calculate_rectangle_area(self):
        """计算矩形面积"""
        self.create_input_dialog(
            "计算矩形面积", 
            [("长度", 10), ("宽度", 5)],
            self.squ_square
        )
    
def calculate_trapezoid_area(self):
        """计算梯形面积"""
        self.create_input_dialog(
            "计算梯形面积", 
            [("上底", 5), ("下底", 10), ("高度", 2)],
            self.squ_trapezoid
        )
