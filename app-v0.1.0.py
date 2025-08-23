import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import math
import pickle
import os

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('欢迎来到计算王者')
        self.root.geometry('1000x800')
        self.root.resizable(True, True)
        
        # 创建欢迎界面
        self.create_login_interface()
        
    def create_login_interface(self):
        """创建登录界面"""
        # 顶部欢迎区
        header_frame = tk.Frame(self.root, bg='#3498db', height=100)
        header_frame.pack(fill=tk.X)
        
        tk.Label(
            header_frame, 
            text='计算王者训练系统', 
            font=('Micsoft Yahei UI', 20, 'bold'), 
            fg='blue', 
            bg='#3498db'
        ).pack(pady=20)
        
        # 主内容区
        content_frame = tk.Frame(self.root)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 登录表单
        form_frame = tk.Frame(content_frame)
        form_frame.pack(pady=20)
        
        tk.Label(form_frame, text='用户名:', font=('Micsoft Yahei UI', 12)).grid(row=0, column=0, sticky=tk.W, pady=10)
        self.var_usr_name = tk.StringVar()
        self.var_usr_name.set('student')
        entry_usr_name = tk.Entry(form_frame, textvariable=self.var_usr_name, font=('Arial', 12), width=20)
        entry_usr_name.grid(row=0, column=1, padx=10)
        
        tk.Label(form_frame, text='密码:', font=('Micsoft Yahei UI', 12)).grid(row=1, column=0, sticky=tk.W, pady=10)
        self.var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(form_frame, textvariable=self.var_usr_pwd, font=('Micsoft Yahei UI', 12), show='*', width=20)
        entry_usr_pwd.grid(row=1, column=1, padx=10)
        
        # 按钮区域
        btn_frame = tk.Frame(content_frame)
        btn_frame.pack(pady=20)
        
        btn_login = tk.Button(
            btn_frame, 
            text='登录', 
            command=self.usr_login,
            font=('Micsoft Yahei UI', 14),
            width=10,
            bg='#2ecc71',
            fg='white'
        )
        btn_login.pack(side=tk.LEFT, padx=10)
        
        btn_sign_up = tk.Button(
            btn_frame, 
            text='注册', 
            command=self.usr_sign_up,
            font=('Micsoft Yahei UI', 14),
            width=10,
            bg='#3498db',
            fg='white'
        )
        btn_sign_up.pack(side=tk.LEFT, padx=10)
        
        # 版权信息
        tk.Label(
            self.root, 
            text='© 2025 计算王者训练系统 v1.0.0', 
            font=('Micsoft Yahei UI', 10),
            fg='gray'
        ).pack(side=tk.BOTTOM, pady=10)
    
    def usr_login(self):
        """用户登录功能"""
        usr_name = self.var_usr_name.get().strip()
        usr_pwd = self.var_usr_pwd.get().strip()
        
        # 验证输入
        if not usr_name or not usr_pwd:
            messagebox.showerror("错误", "用户名和密码不能为空！")
            return
        
        try:
            # 尝试打开用户信息文件
            if os.path.exists('usrs_info.pickle'):
                with open('usrs_info.pickle', 'rb') as usr_file:
                    usrs_info = pickle.load(usr_file)
            else:
                # 文件不存在则创建默认管理员账户
                usrs_info = {'admin': 'admin', 'student': '123456'}
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(usrs_info, usr_file)
        except Exception as e:
            messagebox.showerror("错误", f"访问用户数据失败: {e}")
            return
        
        # 检查用户名和密码
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                # 登录成功，启动主程序
                self.root.destroy()
                root = tk.Tk()
                app = MathTrainerApp(root)
                root.mainloop()
            else:
                messagebox.showerror('错误', '密码错误，请重试！')
        else:
            # 用户不存在，询问是否注册
            response = messagebox.askyesno('新用户', '用户名不存在，是否注册新账户？')
            if response:
                self.usr_sign_up()
    
    def usr_sign_up(self):
        """用户注册功能"""
        # 创建注册窗口
        window_sign_up = tk.Toplevel(self.root)
        window_sign_up.title('注册新账户')
        window_sign_up.geometry('350x250')
        window_sign_up.resizable(False, False)
        window_sign_up.grab_set()  # 模态窗口
        
        # 居中注册窗口
        window_sign_up.update_idletasks()
        width = window_sign_up.winfo_width()
        height = window_sign_up.winfo_height()
        x = (window_sign_up.winfo_screenwidth() // 2) - (width // 2)
        y = (window_sign_up.winfo_screenheight() // 2) - (height // 2)
        window_sign_up.geometry(f'+{x}+{y}')
        
        # 注册表单
        tk.Label(window_sign_up, text='用户名:', font=('Arial', 12)).place(x=20, y=20)
        new_name = tk.StringVar()
        new_name.set('new_user')
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name, font=('Arial', 12))
        entry_new_name.place(x=120, y=20, width=200)
        
        tk.Label(window_sign_up, text='密码:', font=('Arial', 12)).place(x=20, y=60)
        new_pwd = tk.StringVar()
        entry_new_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*', font=('Arial', 12))
        entry_new_pwd.place(x=120, y=60, width=200)
        
        tk.Label(window_sign_up, text='确认密码:', font=('Arial', 12)).place(x=20, y=100)
        new_pwd_confirm = tk.StringVar()
        entry_new_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*', font=('Arial', 12))
        entry_new_pwd_confirm.place(x=120, y=100, width=200)
        
        # 状态消息
        status_var = tk.StringVar()
        tk.Label(window_sign_up, textvariable=status_var, fg='red').place(x=20, y=140)
        
        # 注册提交函数
        def sign_up_submit():
            username = new_name.get().strip()
            password = new_pwd.get().strip()
            confirm = new_pwd_confirm.get().strip()
            
            # 验证输入
            if not username:
                status_var.set("用户名不能为空！")
                return
            if not password:
                status_var.set("密码不能为空！")
                return
            if len(password) < 4:
                status_var.set("密码长度至少4位！")
                return
            if password != confirm:
                status_var.set("两次输入的密码不一致！")
                return
            
            # 加载现有用户数据
            try:
                if os.path.exists('usrs_info.pickle'):
                    with open('usrs_info.pickle', 'rb') as usr_file:
                        usrs_info = pickle.load(usr_file)
                else:
                    usrs_info = {}
            except Exception as e:
                status_var.set(f"访问用户数据失败: {e}")
                return
            
            # 检查用户名是否已存在
            if username in usrs_info:
                status_var.set("用户名已存在，请选择其他用户名！")
                return
            
            # 添加新用户
            usrs_info[username] = password
            try:
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(usrs_info, usr_file)
                messagebox.showinfo("成功", "账户创建成功！")
                window_sign_up.destroy()
            except Exception as e:
                status_var.set(f"保存用户数据失败: {e}")
        
        # 注册按钮
        btn_confirm = tk.Button(
            window_sign_up, 
            text='注册', 
            command=sign_up_submit,
            font=('Arial', 12),
            width=10,
            bg='#3498db',
            fg='white'
        )
        btn_confirm.place(x=120, y=170)
        
        # 聚焦用户名输入框
        entry_new_name.focus_set()

class MathTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("计算王者训练系统")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # 设置主题
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", font=("Micsoft Yahei UI", 12), padding=5)
        self.style.configure("TLabel", font=("Micsoft Yahei UI", 12), background="#f0f0f0")
        self.style.configure("Title.TLabel", font=("Micsoft Yahei UI", 14, "bold"))
        
        # 初始化变量
        self.current_frame = None
        self.training_mode = ""
        self.operator = ""
        self.question_count = 10
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.start_time = 0
        
        # 几何计算常量
        self.pinum = 3.14159265358979323846
        
        # 创建主菜单
        self.create_main_menu()
    
    # ====================== 几何计算函数 ======================
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

    def vol_ball(self, r, pi):
        """计算球体积"""
        vol = (4 / 3) * r ** 3
        if pi == 0:
            return f"{vol}π"
        elif 0 < pi <= 10:
            return vol * round(self.pinum, pi)
        else:
            return vol * self.pinum

    def vol_prism(self, s, h):
        """计算棱柱体积"""
        return s * h
    
    # ====================== 四则运算训练函数 ======================
    def generate_addition(self):
        """生成加法题目"""
        while True:
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            key = x + y
            if key <= 100:  # 确保总和不超过100
                return x, y, key

    def generate_subtraction(self):
        """生成减法题目"""
        while True:
            x = random.randint(0, 100)
            y = random.randint(0, x)  # 确保结果非负
            key = x - y
            return x, y, key

    def generate_multiplication(self):
        """生成乘法题目（200以内）"""
        x = random.randint(0, 20)
        y = random.randint(0, 10)
        key = x * y
        return x, y, key

    def generate_division(self):
        """生成整数除法题目"""
        while True:
            y = random.randint(1, 20)  # 除数不为0
            quotient = random.randint(1, 20)
            x = y * quotient  # 确保整除
            key = quotient
            return x, y, key
    
    # ====================== 主菜单系统 ======================
    def create_main_menu(self):
        """创建主菜单界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame, 
            text="计算王者训练系统", 
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        desc_label = ttk.Label(
            self.current_frame, 
            text="在这里，你将练成计算大师！",
            font=("Arial", 14)
        )
        desc_label.pack(pady=10)
        
        # 创建训练按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        buttons = [
            ("加法训练", "+"),
            ("减法训练", "-"),
            ("乘法训练", "×"),
            ("除法训练", "÷"),
            ("几何计算", "📐")
        ]
        
        for text, operator in buttons:
            btn = ttk.Button(
                btn_frame,
                text=text,
                width=15,
                command=lambda op=operator: self.select_training_mode(op) if op != "📐" else self.geometry_calculator()
            )
            btn.pack(pady=10, fill=tk.X)
        
        # 退出按钮
        exit_btn = ttk.Button(
            self.current_frame,
            text="退出系统",
            command=self.root.quit
        )
        exit_btn.pack(pady=20, fill=tk.X)
    
    def select_training_mode(self, operator):
        """选择训练模式界面"""
        self.operator = operator
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame, 
            text=f"{operator}训练",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 模式选择按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        free_btn = ttk.Button(
            btn_frame,
            text="自由训练",
            width=16,
            command=lambda: self.start_training("free", operator)
        )
        free_btn.pack(pady=10, fill=tk.X)
        
        exam_btn = ttk.Button(
            btn_frame,
            text="考试模式",
            width=16,
            command=lambda: self.select_question_count(operator)
        )
        exam_btn.pack(pady=10, fill=tk.X)
        
        # 返回按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回主菜单",
            command=self.create_main_menu
        )
        back_btn.pack(pady=20, fill=tk.X)
    
    def select_question_count(self, operator):
        """选择题量界面"""
        self.operator = operator
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame, 
            text="选择题量",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 题量选择
        count_frame = ttk.Frame(self.current_frame)
        count_frame.pack(pady=20)
        
        ttk.Label(count_frame, text="请选择考试题量:").pack(pady=5)
        
        self.question_count = tk.IntVar(value=15)
        counts = [5, 10, 15, 20, 25, 30, 35, 40]
        
        for count in counts:
            rb = ttk.Radiobutton(
                count_frame,
                text=f"{count}题",
                variable=self.question_count,
                value=count
            )
            rb.pack(anchor=tk.W, pady=2)
        
        # 开始考试按钮
        start_btn = ttk.Button(
            count_frame,
            text="开始考试",
            command=lambda: self.start_training("exam", operator)
        )
        start_btn.pack(pady=15, fill=tk.X)
        
        # 返回按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回",
            command=lambda: self.select_training_mode(operator)
        )
        back_btn.pack(pady=10, fill=tk.X)
    
    # ====================== 训练功能 ======================
    def start_training(self, mode, operator):
        """开始训练"""
        self.training_mode = mode
        self.operator = operator
        self.score = 0
        self.current_question = 0
        self.questions = []
        self.start_time = time.time()
        
        # 生成题目
        if operator == "+":
            self.generate_addition_questions()
        elif operator == "-":
            self.generate_subtraction_questions()
        elif operator == "×":
            self.generate_multiplication_questions()
        elif operator == "÷":
            self.generate_division_questions()
        
        # 显示第一题
        self.show_question()
    
    def generate_addition_questions(self):
        """生成加法题目"""
        if self.training_mode == "free":
            # 自由训练生成10题
            count = 10
        else:
            count = self.question_count.get()
        
        for _ in range(count):
            while True:
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                key = x + y
                if key <= 100:  # 确保总和不超过100
                    self.questions.append((x, y, key))
                    break
    
    def generate_subtraction_questions(self):
        """生成减法题目"""
        if self.training_mode == "free":
            count = 10
        else:
            count = self.question_count.get()
        
        for _ in range(count):
            x = random.randint(0, 100)
            y = random.randint(0, x)  # 确保结果非负
            key = x - y
            self.questions.append((x, y, key))
    
    def generate_multiplication_questions(self):
        """生成乘法题目"""
        if self.training_mode == "free":
            count = 10
        else:
            count = self.question_count.get()
        
        for _ in range(count):
            x = random.randint(0, 20)
            y = random.randint(0, 10)
            key = x * y
            self.questions.append((x, y, key))
    
    def generate_division_questions(self):
        """生成除法题目"""
        if self.training_mode == "free":
            count = 10
        else:
            count = self.question_count.get()
        
        for _ in range(count):
            y = random.randint(1, 20)  # 除数不为0
            quotient = random.randint(1, 20)
            x = y * quotient  # 确保整除
            key = quotient
            self.questions.append((x, y, key))
    
    def show_question(self):
        """显示当前题目"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 显示进度
        progress_frame = ttk.Frame(self.current_frame)
        progress_frame.pack(fill=tk.X, pady=10)
        
        if self.training_mode == "exam":
            progress_label = ttk.Label(
                progress_frame,
                text=f"题目: {self.current_question + 1}/{len(self.questions)}"
            )
            progress_label.pack(side=tk.LEFT)
        
        self.timer_label = ttk.Label(progress_frame, text="用时: 0.0秒")
        self.timer_label.pack(side=tk.RIGHT)
        
        # 更新计时器
        self.update_timer()
        
        # 显示题目
        x, y, _ = self.questions[self.current_question]
        question_label = ttk.Label(
            self.current_frame,
            text=f"{x} {self.operator} {y} = ?",
            font=("Arial", 24, "bold")
        )
        question_label.pack(pady=40)
        
        # 答案输入框
        answer_frame = ttk.Frame(self.current_frame)
        answer_frame.pack(pady=20)
        
        self.answer_var = tk.StringVar()
        answer_entry = ttk.Entry(
            answer_frame,
            textvariable=self.answer_var,
            font=("Arial", 18),
            width=10,
            justify=tk.CENTER
        )
        answer_entry.pack()
        answer_entry.focus()
        answer_entry.bind("<Return>", self.check_answer)
        
        # 提交按钮
        submit_btn = ttk.Button(
            self.current_frame,
            text="提交答案",
            command=self.check_answer
        )
        submit_btn.pack(pady=10)
        
        # 自由训练模式下显示退出按钮
        if self.training_mode == "free":
            exit_btn = ttk.Button(
                self.current_frame,
                text="结束训练",
                command=self.show_results
            )
            exit_btn.pack(pady=10)
    
    def update_timer(self):
        """更新计时器显示"""
        if hasattr(self, 'start_time') and self.start_time:
            elapsed_time = round(time.time() - self.start_time, 1)
            self.timer_label.config(text=f"用时: {elapsed_time}秒")
        
        # 每1毫秒更新一次
        if hasattr(self, 'current_frame') and self.current_frame.winfo_exists():
            self.root.after(1, self.update_timer)
    
    def check_answer(self, event=None):
        """检查答案"""
        try:
            user_answer = float(self.answer_var.get())
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数字！")
            return
        
        x, y, correct_answer = self.questions[self.current_question]
        question_time = round(time.time() - self.start_time, 2)
        
        if user_answer == correct_answer:
            self.score += 1
            message = "✓ 正确！"
        else:
            message = f"✗ 错误！正确答案是 {correct_answer}"
        
        # 显示反馈
        feedback = f"{message}\n用时: {question_time}秒"
        messagebox.showinfo("答题结果", feedback)
        
        # 移动到下一题或显示结果
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.start_time = time.time()
            self.answer_var.set("")
            self.show_question()
        else:
            self.show_results()
    
    def show_results(self):
        """显示训练结果"""
        total_time = round(time.time() - self.start_time, 2)
        accuracy = self.score / len(self.questions) * 100 if self.questions else 0
        
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame, 
            text="训练结果",
            style="Title.TLabel"
        )
        title_label.pack(pady=20)
        
        # 显示统计信息
        stats_frame = ttk.Frame(self.current_frame)
        stats_frame.pack(fill=tk.X, pady=10)
        
        stats = [
            ("训练类型", "考试" if self.training_mode == "exam" else "自由训练"),
            ("计算类型", self.operator),
            ("题目数量", len(self.questions)),
            ("答对题数", self.score),
            ("正确率", f"{accuracy:.1f}%" if self.questions else "N/A"),
            ("总用时", f"{total_time}秒"),
            ("平均每题用时", f"{total_time/len(self.questions):.2f}秒" if self.questions else "N/A")
        ]
        
        for i, (label, value) in enumerate(stats):
            ttk.Label(stats_frame, text=label, width=15, anchor=tk.W).grid(row=i, column=0, sticky=tk.W, pady=2)
            ttk.Label(stats_frame, text=value, font=("Arial", 12, "bold")).grid(row=i, column=1, sticky=tk.W, pady=2)
        
        # 星级评价
        stars_frame = ttk.Frame(self.current_frame)
        stars_frame.pack(pady=20)
        
        if accuracy >= 90:
            stars = "★★★★★"
            comment = "太棒了！你是计算王者！"
        elif accuracy >= 70:
            stars = "★★★★"
            comment = "做得很好！继续加油！"
        elif accuracy >= 50:
            stars = "★★★"
            comment = "还不错，多加练习会更棒！"
        else:
            stars = "★"
            comment = "需要更多练习哦！"
        
        ttk.Label(stars_frame, text=stars, font=("Arial", 24)).pack()
        ttk.Label(stars_frame, text=comment, font=("Arial", 14)).pack(pady=5)
        
        # 按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        retry_btn = ttk.Button(
            btn_frame,
            text="再次训练",
            command=lambda: self.start_training(self.training_mode, self.operator)
        )
        retry_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(
            btn_frame,
            text="返回主菜单",
            command=self.create_main_menu
        )
        back_btn.pack(side=tk.LEFT, padx=10)
    
    # == 几何计算功能 =====
    def geometry_calculator(self):
        """几何计算器界面"""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        title_label = ttk.Label(
            self.current_frame, 
            text="几何计算器",
            style="Title.TLabel"
        )
        title_label.pack(pady=10)
        
        # 创建几何计算选项按钮
        btn_frame = ttk.Frame(self.current_frame)
        btn_frame.pack(pady=20)
        
        geometry_options = [
            ("圆面积", self.calculate_circle_area),
            ("矩形面积", self.calculate_rectangle_area),
            ("梯形面积", self.calculate_trapezoid_area),
            ("球体积", self.calculate_ball_volume),
            ("棱柱体积", self.calculate_prism_volume)
        ]
        
        for text, command in geometry_options:
            btn = ttk.Button(
                btn_frame,
                text=text,
                width=15,
                command=command
            )
            btn.pack(pady=10, fill=tk.X)
        
        # 返回按钮
        back_btn = ttk.Button(
            self.current_frame,
            text="返回主菜单",
            command=self.create_main_menu
        )
        back_btn.pack(pady=20)
    
    def create_input_dialog(self, title, fields, calculate_func):
        """创建输入对话框"""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.resizable(False, False)
        dialog.grab_set()  # 模态对话框
        
        # 居中对话框
        dialog.update_idletasks()
        width = 300
        height = 100 + len(fields) * 40
        x = (dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (dialog.winfo_screenheight() // 2) - (height // 2)
        dialog.geometry(f"{width}x{height}+{x}+{y}")
        
        # 创建输入字段
        entries = []
        for i, (label, default) in enumerate(fields):
            tk.Label(dialog, text=label + ":", font=('Micsoft Yahei UI', 11)).place(x=20, y=20 + i*40)
            var = tk.StringVar(value=str(default))
            entry = tk.Entry(dialog, textvariable=var, font=('Micsoft Yahei UI', 11), width=15)
            entry.place(x=120, y=20 + i*40)
            entries.append(var)
        
        # 状态消息
        status_var = tk.StringVar()
        tk.Label(dialog, textvariable=status_var, fg='red').place(x=20, y=height-70)
        
        # 计算按钮
        btn_calculate = tk.Button(
            dialog, 
            text="计算", 
            command=lambda: self.perform_calculation(entries, calculate_func, status_var),
            width=10
        )
        btn_calculate.place(x=100, y=height-40)
        
        # 聚焦第一个输入框
        dialog.after(100, lambda: entries[0].focus_set())
    
    def perform_calculation(self, entries, calculate_func, status_var):
        """执行计算并显示结果"""
        try:
            # 获取输入值并转换为浮点数
            values = [float(var.get()) for var in entries]
            # 调用计算函数
            result = calculate_func(*values)
            # 显示结果
            messagebox.showinfo("计算结果", f"计算结果: {result}")
            # 关闭对话框
            entries[0].master.destroy()
        except ValueError:
            status_var.set("请输入有效的数字！")
        except Exception as e:
            status_var.set(f"计算错误: {str(e)}")
    
    def calculate_circle_area(self):
        """计算圆面积"""
        self.create_input_dialog(
            "计算圆面积", 
            [("半径", 5), ("π精度 (0=符号, 1-10=小数位)", 3.14)],
            lambda r, pi: self.squ_cir(r, int(pi))
        )
    
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
    
    def calculate_ball_volume(self):
        """计算球体积"""
        self.create_input_dialog(
            "计算球体积", 
            [("半径", 5), ("π精度 (0=符号, 1-10=小数位)", 3.14)],
            lambda r, pi: self.vol_ball(r, int(pi))
        )
    
    def calculate_prism_volume(self):
        """计算棱柱体积"""
        self.create_input_dialog(
            "计算棱柱体积", 
            [("底面积", 5), ("高度", 1)],
            self.vol_prism
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
