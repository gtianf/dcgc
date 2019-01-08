from django.db import models

# Create your models here.


#定义源基础数据表
class Raw_data(models.Model):
	id = models.AutoField(primary_key=True)
	rom_id = models.CharField(max_length=30, null=False)
	time = models.DateTimeField()
	pressure = models.IntegerField()
	temperature = models.IntegerField()
	s_volt = models.FloatField()
	s_press = models.IntegerField()
	s_temp = models.IntegerField()
	s_data = models.CharField(max_length=30)

#对原有数据表进行关联
class Corectedsurveydata(models.Model):
    recordid = models.IntegerField(db_column='RecordID', blank=True, null=True)  # Field name made lowercase.
    pointid = models.IntegerField(db_column='PointID', blank=True, null=True)  # Field name made lowercase.
    correctedvalue = models.FloatField(db_column='CorrectedValue', blank=True, null=True)  # Field name made lowercase.
    runtime = models.DateTimeField(db_column='Runtime', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'corectedsurveydata'


class Datadescription(models.Model):
    dataid = models.IntegerField(db_column='DataID', blank=True, null=True)  # Field name made lowercase.
    occurrencetime = models.DateTimeField(db_column='OccurrenceTime', blank=True, null=True)  # Field name made lowercase.
    phenomenon = models.CharField(db_column='Phenomenon', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    analysis = models.CharField(db_column='Analysis', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    deal = models.CharField(db_column='Deal', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    operatetime = models.DateTimeField(db_column='OperateTime', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.TextField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'datadescription'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class Grades(models.Model):
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='GradeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gradedescription = models.CharField(db_column='GradeDescription', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'grades'


class Levelmetercoefficient(models.Model):
    romid = models.CharField(db_column='RomId', max_length=16, blank=True, null=True)  # Field name made lowercase.
    intercept = models.FloatField(db_column='Intercept', blank=True, null=True)  # Field name made lowercase.
    p = models.FloatField(db_column='P', blank=True, null=True)  # Field name made lowercase.
    pp = models.FloatField(db_column='PP', blank=True, null=True)  # Field name made lowercase.
    t = models.FloatField(db_column='T', blank=True, null=True)  # Field name made lowercase.
    tp = models.FloatField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    a = models.FloatField(blank=True, null=True)
    b = models.FloatField(blank=True, null=True)
    rangeid = models.IntegerField(db_column='RangeID', blank=True, null=True)  # Field name made lowercase.
    temperaturerangeid = models.IntegerField(db_column='TemperatureRangeID', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    stdg = models.FloatField(db_column='StdG', blank=True, null=True)  # Field name made lowercase.
    stdtemperature = models.FloatField(db_column='StdTemperature', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'levelmetercoefficient'


class Memberprojectrole(models.Model):
    memberprojectroleid = models.IntegerField(db_column='MemberProjectRoleId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='ProjectId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'memberprojectrole'


class Memberrole(models.Model):
    memberroleid = models.IntegerField(db_column='MemberRoleId', blank=True, null=True)  # Field name made lowercase.
    memberid = models.TextField(db_column='MemberId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'memberrole'


class Members(models.Model):
    memberid = models.TextField(db_column='MemberId', blank=True, null=True)  # Field name made lowercase.
    loginname = models.CharField(db_column='LoginName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=512, blank=True, null=True)  # Field name made lowercase.
    truename = models.CharField(db_column='TrueName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=300, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='MobilePhone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'members'


class NAnglepoint(models.Model):
    pointid = models.IntegerField(db_column='PointId', blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    pointname = models.CharField(db_column='PointName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    romid = models.CharField(db_column='RomId', max_length=16, blank=True, null=True)  # Field name made lowercase.
    operationorder = models.IntegerField(db_column='OperationOrder', blank=True, null=True)  # Field name made lowercase.
    serialno = models.IntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    sensorlangth = models.FloatField(db_column='SensorLangth', blank=True, null=True)  # Field name made lowercase.
    location = models.FloatField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.
    visible = models.IntegerField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'n_anglepoint'


class NDatarevised(models.Model):
    datano = models.IntegerField(db_column='DataNo', blank=True, null=True)  # Field name made lowercase.
    pointid = models.IntegerField(db_column='PointID', blank=True, null=True)  # Field name made lowercase.
    pointstatus = models.CharField(db_column='PointStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    revisedmethod = models.CharField(db_column='RevisedMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parameters = models.CharField(db_column='Parameters', max_length=500, blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'n_datarevised'


class NLineaext(models.Model):
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    linelength = models.FloatField(db_column='LineLength', blank=True, null=True)  # Field name made lowercase.
    alpha = models.FloatField(db_column='Alpha', blank=True, null=True)  # Field name made lowercase.
    beta = models.FloatField(db_column='Beta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'n_lineaext'


class NLinesext(models.Model):
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    liquid = models.IntegerField(db_column='Liquid', blank=True, null=True)  # Field name made lowercase.
    g = models.FloatField(db_column='G', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'n_linesext'


class NSurveyline(models.Model):
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    linename = models.CharField(db_column='LineName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rtuid = models.CharField(db_column='RtuId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    measuringtype = models.CharField(db_column='MeasuringType', max_length=4, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    linestatus = models.CharField(db_column='LineStatus', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'n_surveyline'


class Plcregister(models.Model):
    pointid = models.IntegerField(db_column='PointId', blank=True, null=True)  # Field name made lowercase.
    addressno = models.IntegerField(db_column='AddressNo', blank=True, null=True)  # Field name made lowercase.
    plcaddress = models.CharField(db_column='PLCAddress', max_length=16, blank=True, null=True)  # Field name made lowercase.
    plcvalue = models.CharField(db_column='PLCValue', max_length=16, blank=True, null=True)  # Field name made lowercase.
    receivetime = models.DateTimeField(db_column='ReceiveTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'plcregister'


class Projecttree(models.Model):
    nodeid = models.IntegerField(db_column='NodeId', blank=True, null=True)  # Field name made lowercase.
    nodename = models.CharField(db_column='NodeName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nodetype = models.IntegerField(db_column='NodeType', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='ProjectId', blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.
    visible = models.IntegerField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'projecttree'


class Ranges(models.Model):
    rangeid = models.IntegerField(db_column='RangeId', blank=True, null=True)  # Field name made lowercase.
    rangename = models.CharField(db_column='RangeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    minvalue = models.FloatField(db_column='MinValue', blank=True, null=True)  # Field name made lowercase.
    maxvalue = models.FloatField(db_column='MaxValue', blank=True, null=True)  # Field name made lowercase.
    rangetype = models.IntegerField(db_column='RangeType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ranges'


class Relevance(models.Model):
    relevanceid = models.IntegerField(db_column='RelevanceID', blank=True, null=True)  # Field name made lowercase.
    firstid = models.IntegerField(db_column='FirstID', blank=True, null=True)  # Field name made lowercase.
    secondid = models.IntegerField(db_column='SecondID', blank=True, null=True)  # Field name made lowercase.
    thirdid = models.IntegerField(db_column='ThirdID', blank=True, null=True)  # Field name made lowercase.
    fourthid = models.IntegerField(db_column='FourthID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    mode = models.CharField(db_column='Mode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    operatetime = models.DateTimeField(db_column='OperateTime', blank=True, null=True)  # Field name made lowercase.
    operatorid = models.IntegerField(db_column='OperatorID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'relevance'


class Role(models.Model):
    roleid = models.IntegerField(db_column='RoleId', blank=True, null=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'role'


class Settlementdata(models.Model):
    datano = models.IntegerField(db_column='DataNo', blank=True, null=True)  # Field name made lowercase.
    sampletime = models.DateTimeField(db_column='SampleTime', blank=True, null=True)  # Field name made lowercase.
    pointid = models.IntegerField(db_column='PointId', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    currentvalue = models.FloatField(db_column='CurrentValue', blank=True, null=True)  # Field name made lowercase.
    totalizevalue = models.FloatField(db_column='TotalizeValue', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'settlementdata'


class Surveydatas(models.Model):
    datano = models.IntegerField(db_column='DataNo', blank=True, null=True)  # Field name made lowercase.
    sampletime = models.DateTimeField(db_column='SampleTime', blank=True, null=True)  # Field name made lowercase.
    pointid = models.IntegerField(db_column='PointId', blank=True, null=True)  # Field name made lowercase.
    voltage = models.FloatField(db_column='Voltage', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    deltah = models.FloatField(db_column='DeltaH', blank=True, null=True)  # Field name made lowercase.
    totalize = models.FloatField(db_column='Totalize', blank=True, null=True)  # Field name made lowercase.
    correctedvalue = models.FloatField(db_column='CorrectedValue', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'surveydatas'


class Surveylines(models.Model):
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    linename = models.CharField(db_column='LineName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rtuid = models.CharField(db_column='RtuId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    benchmark = models.IntegerField(db_column='BenchMark', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    liquid = models.IntegerField(db_column='Liquid', blank=True, null=True)  # Field name made lowercase.
    g = models.FloatField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    linegroup = models.CharField(db_column='LineGroup', max_length=10, blank=True, null=True)  # Field name made lowercase.
    linestatus = models.IntegerField(db_column='LineStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'surveylines'


class Surveypoints(models.Model):
    pointid = models.IntegerField(db_column='PointId', blank=True, null=True)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineId', blank=True, null=True)  # Field name made lowercase.
    pointname = models.CharField(db_column='PointName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    serialno = models.IntegerField(db_column='SerialNo', blank=True, null=True)  # Field name made lowercase.
    isbenchmark = models.IntegerField(db_column='IsBenchMark', blank=True, null=True)  # Field name made lowercase.
    romid = models.CharField(db_column='RomId', max_length=16, blank=True, null=True)  # Field name made lowercase.
    isvalid = models.IntegerField(db_column='IsValid', blank=True, null=True)  # Field name made lowercase.
    visible = models.IntegerField(db_column='Visible', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'surveypoints'


class Surveyrod(models.Model):
    rodid = models.IntegerField(db_column='RodId', blank=True, null=True)  # Field name made lowercase.
    rodname = models.CharField(db_column='RodName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    rtuid = models.CharField(db_column='RtuId', max_length=8, blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    rodlength = models.FloatField(db_column='RodLength', blank=True, null=True)  # Field name made lowercase.
    rodstatus = models.IntegerField(db_column='RodStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'surveyrod'


class Userlogin(models.Model):
    logid = models.IntegerField(db_column='LogId', blank=True, null=True)  # Field name made lowercase.
    userid = models.TextField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    onlinetime = models.DateTimeField(db_column='OnlineTime', blank=True, null=True)  # Field name made lowercase.
    ipadders = models.CharField(db_column='IpAdders', max_length=15, blank=True, null=True)  # Field name made lowercase.
    loginkey = models.CharField(db_column='LoginKey', max_length=512, blank=True, null=True)  # Field name made lowercase.
    macadders = models.CharField(db_column='MacAdders', max_length=50, blank=True, null=True)  # Field name made lowercase.
    browser = models.CharField(db_column='Browser', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'userlogin'