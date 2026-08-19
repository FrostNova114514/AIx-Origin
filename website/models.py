from django.db import models


class Contract(models.Model):
    # 问卷基础身份信息
    feishu_record_id = models.CharField('飞书记录ID', max_length=80, unique=True, null=True, blank=True)
    submitter = models.CharField('提交人', max_length=120, blank=True)
    name = models.CharField('姓名', max_length=120)
    remember = models.TextField('你还记得吗', blank=True)
    phone = models.CharField('手机号', max_length=60)
    email = models.EmailField('电子邮箱', max_length=254)
    identity = models.JSONField('你的身份', default=list, blank=True)
    identity_other = models.CharField('你的身份-其他-Text', max_length=255, blank=True)
    background = models.TextField('学校背景/工作背景')

    # 组队与赛道
    team_method = models.CharField('请选择组队方式', max_length=120, blank=True)
    team_method_extra = models.TextField('请选择组队方式（支持 1—5 人/队，允许跨校及跨机构组队）-自行组队（请补充队友姓名/联系方式）-补充内容', blank=True)
    team_name = models.CharField('若自行组队，请输入队名', max_length=160)
    participation_city = models.CharField('参加方式', max_length=120)
    track_shenzhen = models.CharField('参与赛道（深圳）', max_length=160, blank=True)
    track_hong_kong = models.CharField('参与赛道（香港）', max_length=160, blank=True)

    # 项目与作品
    complete_project = models.CharField('是否参与过完整的创业项目或开发项目', max_length=10, blank=True)
    github_homepage = models.URLField('你的GitHub/个人主页', max_length=500)
    portfolio_resume = models.FileField('你的作品集，简历', upload_to='contracts/portfolios/', blank=True)
    project_description = models.TextField('项目简述', blank=True)
    post_event_followup = models.CharField('赛后是否愿意推进落地', max_length=20)
    post_event_followup_other = models.CharField('你是否愿意在赛后将你的优秀项目进一步推进落地？-其他-Text', max_length=255, blank=True)

    # 技能自评
    skill_programming = models.PositiveSmallIntegerField('编程能力', null=True, blank=True)
    skill_hardware = models.PositiveSmallIntegerField('硬件开发', null=True, blank=True)
    skill_research = models.PositiveSmallIntegerField('产品/用户研究', null=True, blank=True)
    skill_design = models.PositiveSmallIntegerField('设计表达', null=True, blank=True)
    skill_collaboration = models.PositiveSmallIntegerField('项目协作', null=True, blank=True)
    skill_other = models.TextField('技能评价-其他', blank=True)
    hardware_skills = models.JSONField('硬实力 Hardware Skills', default=list, blank=True)
    hardware_other = models.CharField('你的“硬”实力 (Hardware Skills)-其他-Text', max_length=255, blank=True)
    software_ai_skills = models.JSONField('软实力 Software & AI', default=list, blank=True)
    software_other = models.CharField('你的“软”实力 (Software & AI)-其他-Text', max_length=255, blank=True)
    social_links = models.TextField('最活跃的社交媒体链接', blank=True)
    past_18_months = models.TextField('过去18个月内做过的有趣的事', blank=True)
    public_contact = models.CharField('是否愿意公开联系方式给合作方', max_length=20, blank=True)

    # 系统保存内容
    feishu_summary = models.TextField('AI总结', blank=True)
    feishu_raw_record = models.JSONField('飞书原始记录', default=dict, blank=True)
    is_approved = models.BooleanField('是否通过审核', default=False)
    approval_email_sent = models.BooleanField('是否发送邮件', default=False)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'contract'
        verbose_name = '联系表单'
        verbose_name_plural = '联系表单'

    def __str__(self):
        return f'{self.name} - {self.email}'

    def save(self, *args, **kwargs):
        if not self.feishu_record_id:
            numeric_ids = [
                int(record_id)
                for record_id in Contract.objects.exclude(feishu_record_id__isnull=True)
                .exclude(feishu_record_id='')
                .values_list('feishu_record_id', flat=True)
                if str(record_id).isdigit()
            ]
            self.feishu_record_id = str((max(numeric_ids) if numeric_ids else 0) + 1)
        super().save(*args, **kwargs)


class EmailLog(models.Model):
    contract = models.ForeignKey(
        Contract,
        verbose_name='申请者',
        related_name='email_logs',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    recipient = models.EmailField('收件邮箱', max_length=254)
    subject = models.CharField('邮件主题', max_length=255)
    body = models.TextField('邮件正文', blank=True)
    attachment_name = models.CharField('附件名称', max_length=255, blank=True)
    sent_at = models.DateTimeField('发送时间', auto_now_add=True)

    class Meta:
        db_table = 'email_log'
        verbose_name = '发送邮件记录'
        verbose_name_plural = '发送邮件记录'
        ordering = ('-sent_at',)

    def __str__(self):
        return f'{self.recipient} - {self.subject}'


class Team(models.Model):
    number = models.PositiveIntegerField('队伍序号', unique=True, null=True, blank=True)
    name = models.CharField('队伍名称', max_length=160, unique=True)
    members = models.ManyToManyField(
        Contract,
        verbose_name='队伍成员',
        related_name='teams',
        blank=True,
    )
    notes = models.TextField('备注', blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'team'
        verbose_name = '队伍分配'
        verbose_name_plural = '队伍分配'
        ordering = ('number', 'name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.number:
            max_number = Team.objects.aggregate(models.Max('number'))['number__max'] or 0
            self.number = max_number + 1
        super().save(*args, **kwargs)
