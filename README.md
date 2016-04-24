# lbi.joker

##通过配置定时任务，可定时发送图文笑话给你心仪的Ta

配置信息在config.py进行配置

    # 邮箱配置
    mail_host = 'smtp.qq.com'
    mail_user = 'xxxx@qq.com'
    mail_password = 'xxxx'
    
    # 邮件接收人
    receivers=['xxxx@icloud.com']
    
    # redis配置
    redis_config={
        'host':'xx.xx.xx.xx',
        'port':6379,
        'db':0
    }
