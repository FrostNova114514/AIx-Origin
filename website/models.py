from django.db import models


class Contract(models.Model):
    feishu_record_id = models.CharField('飞书记录ID', max_length=80, unique=True, null=True, blank=True)
    name = models.CharField('姓名', max_length=120)
    phone = models.CharField('手机号', max_length=60)
    email = models.EmailField('电子邮箱', max_length=254)
    identity = models.JSONField('你的身份', default=list, blank=True)
    background = models.TextField('学校背景/工作背景')
    team_method = models.CharField('请选择组队方式', max_length=120, blank=True)
    team_name = models.CharField('若自行组队，请输入队名', max_length=160)
    participation_city = models.CharField('参加方式', max_length=120)
    track_shenzhen = models.CharField('参与赛道（深圳）', max_length=160, blank=True)
    track_hong_kong = models.CharField('参与赛道（香港）', max_length=160, blank=True)
    complete_project = models.CharField('是否参与过完整的创业项目或开发项目', max_length=10, blank=True)
    github_homepage = models.URLField('你的GitHub/个人主页', max_length=500)
    portfolio_resume = models.FileField('你的作品集，简历', upload_to='contracts/portfolios/', blank=True)
    project_description = models.TextField('项目简述', blank=True)
    post_event_followup = models.CharField('赛后是否愿意推进落地', max_length=20)
    skill_programming = models.PositiveSmallIntegerField('编程能力', null=True, blank=True)
    skill_hardware = models.PositiveSmallIntegerField('硬件开发', null=True, blank=True)
    skill_research = models.PositiveSmallIntegerField('产品/用户研究', null=True, blank=True)
    skill_design = models.PositiveSmallIntegerField('设计表达', null=True, blank=True)
    skill_collaboration = models.PositiveSmallIntegerField('项目协作', null=True, blank=True)
    skill_other = models.CharField('技能评价-其他', max_length=255, blank=True)
    hardware_skills = models.JSONField('硬实力 Hardware Skills', default=list, blank=True)
    software_ai_skills = models.JSONField('软实力 Software & AI', default=list, blank=True)
    social_links = models.TextField('最活跃的社交媒体链接', blank=True)
    past_18_months = models.TextField('过去18个月内做过的有趣的事', blank=True)
    public_contact = models.CharField('是否愿意公开联系方式给合作方', max_length=20, blank=True)
    feishu_summary = models.TextField('飞书总结', blank=True)
    feishu_raw_record = models.JSONField('飞书原始记录', default=dict, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'contract'
        verbose_name = '联系表单'
        verbose_name_plural = '联系表单'

    def __str__(self):
        return f'{self.name} - {self.email}'
