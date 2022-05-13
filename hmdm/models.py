from django.db import models
    
class AddonGeneral(models.Model):
    code=models.CharField(max_length=10, help_text='功能代码')
    desc=models.CharField(max_length=20, help_text='功能描述', default='')

    def __str__(self):  
        return self.code    

class AKC(models.Model):
    po_number=models.CharField(max_length=10, help_text='该AKC的订单号')
    serial_number=models.CharField(max_length=15, help_text='该AKC的序列号')
    salesman=models.CharField(max_length=3, help_text='销售人员姓名')
    client=models.CharField(max_length=10, help_text='客户名称')
    addon=models.CharField(choices=[('DM22005', 'DM22005'), ('DM22009', 'DM22009')], max_length=10)

    def __str__(self):
        return self.serial_number