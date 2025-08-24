"""这是来自登入程序的子程序
版本号：V0.1.1"""
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('欢迎来到计算王者')
        self.root.geometry('1000x800')
        self.root.resizable(True, True)
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
            text='© 2025 计算王者训练系统 v0.1.1-beta01', 
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
            if len(password) < 6:
                status_var.set("密码长度至少6位！")
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
