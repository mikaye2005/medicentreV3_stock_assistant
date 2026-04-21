# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tblaccountclasss(models.Model):
    accountclassid = models.BigAutoField(db_column='AccountClassID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    accounttype = models.SmallIntegerField(db_column='AccountType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblaccountclasss'


class Tblaccounts(models.Model):
    accountid = models.BigAutoField(db_column='AccountID', primary_key=True)  # Field name made lowercase.
    companybranchid = models.ForeignKey('Tblcompanybranchs', models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    accountclassid = models.ForeignKey(Tblaccountclasss, models.DO_NOTHING, db_column='AccountClassID')  # Field name made lowercase.
    accountno = models.IntegerField(db_column='AccountNo')  # Field name made lowercase.
    islocked = models.SmallIntegerField(db_column='IsLocked')  # Field name made lowercase.
    configurationtype = models.SmallIntegerField(db_column='ConfigurationType')  # Field name made lowercase.
    cashflowcategoryid = models.ForeignKey('Tblcashflowcategorys', models.DO_NOTHING, db_column='CashFlowCategoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblaccounts'
        unique_together = (('companybranchid', 'name'),)


class Tbladmissions(models.Model):
    admissionid = models.BigAutoField(db_column='AdmissionID', primary_key=True)  # Field name made lowercase.
    medicalclinicvisitid = models.ForeignKey('Tblmedicalclinicvisits', models.DO_NOTHING, db_column='MedicalClinicVisitID')  # Field name made lowercase.
    admissiondatetime = models.DateTimeField(db_column='AdmissionDateTime')  # Field name made lowercase.
    dischargedatetime = models.DateTimeField(db_column='DischargeDateTime', blank=True, null=True)  # Field name made lowercase.
    isinadmission = models.SmallIntegerField(db_column='IsInAdmission')  # Field name made lowercase.
    admittedbysysuid = models.IntegerField(db_column='AdmittedBySysUID')  # Field name made lowercase.
    admittingdoctor = models.CharField(db_column='AdmittingDoctor', max_length=255)  # Field name made lowercase.
    dischargingdoctor = models.CharField(db_column='DischargingDoctor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dischargetype = models.SmallIntegerField(db_column='DischargeType', blank=True, null=True)  # Field name made lowercase.
    isdischargein = models.SmallIntegerField(db_column='IsDischargeIn')  # Field name made lowercase.
    iscurrentdischargein = models.SmallIntegerField(db_column='IsCurrentDischargeIn')  # Field name made lowercase.
    dischargeindatetimeout = models.DateTimeField(db_column='DischargeInDateTimeOut', blank=True, null=True)  # Field name made lowercase.
    companybranchid = models.ForeignKey('Tblcompanybranchs', models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    admittingdoctorsysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='AdmittingDoctorSysUID', blank=True, null=True)  # Field name made lowercase.
    dischargingdoctorsysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='DischargingDoctorSysUID', related_name='tbladmissions_dischargingdoctorsysuid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbladmissions'


class Tblarinvoices(models.Model):
    arinvoiceid = models.OneToOneField('self', models.DO_NOTHING, db_column='ARInvoiceID', primary_key=True)  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated')  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate')  # Field name made lowercase.
    amountreceivable = models.DecimalField(db_column='AmountReceivable', max_digits=100, decimal_places=2)  # Field name made lowercase.
    ispaid = models.SmallIntegerField(db_column='IsPaid')  # Field name made lowercase.
    invoiceto = models.CharField(db_column='InvoiceTo', max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telephone1 = models.CharField(db_column='Telephone1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telephone2 = models.CharField(db_column='Telephone2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isprocessed = models.SmallIntegerField(db_column='IsProcessed')  # Field name made lowercase.
    totalamountpaid = models.DecimalField(db_column='TotalAmountPaid', max_digits=100, decimal_places=2)  # Field name made lowercase.
    receivablesubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='ReceivableSubAccountID')  # Field name made lowercase.
    depositsubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='DepositSubAccountID', related_name='tblarinvoices_depositsubaccountid_set')  # Field name made lowercase.
    preparedbysysuid = models.IntegerField(db_column='PreparedBySysUID')  # Field name made lowercase.
    coveramount = models.DecimalField(db_column='CoverAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    salesdiscountamount = models.DecimalField(db_column='SalesDiscountAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    haswriteoff = models.SmallIntegerField(db_column='HasWriteOff')  # Field name made lowercase.
    writeoffamount = models.DecimalField(db_column='WriteOffAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    writeoffreason = models.CharField(db_column='WriteOffReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    writeoffbysysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='WriteOffBySysUID', blank=True, null=True)  # Field name made lowercase.
    hasbeencancelled = models.IntegerField(db_column='HasBeenCancelled')  # Field name made lowercase.
    cancelledbysysuid = models.IntegerField(db_column='CancelledBySysUID', blank=True, null=True)  # Field name made lowercase.
    cancellationreason = models.CharField(db_column='CancellationReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creditnoteamount = models.DecimalField(db_column='CreditNoteAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    creditnotereason = models.CharField(db_column='CreditNoteReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='InvoiceNo', max_length=255)  # Field name made lowercase.
    invoiceprefix = models.CharField(db_column='InvoicePrefix', max_length=255, blank=True, null=True)  # Field name made lowercase.
    claimid = models.CharField(db_column='ClaimID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rebateamount = models.DecimalField(db_column='RebateAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    invoicetype = models.SmallIntegerField(db_column='InvoiceType')  # Field name made lowercase.
    covertoarinvoiceid = models.BigIntegerField(db_column='CoverToARInvoiceID', blank=True, null=True)  # Field name made lowercase.
    rebateisreceived = models.SmallIntegerField(db_column='RebateIsReceived')  # Field name made lowercase.
    companybranchid = models.BigIntegerField(db_column='CompanyBranchID')  # Field name made lowercase.
    isclaimed = models.SmallIntegerField(db_column='IsClaimed')  # Field name made lowercase.
    isdispatched = models.SmallIntegerField(db_column='IsDispatched')  # Field name made lowercase.
    dispatchedbysysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='DispatchedBySysUID', related_name='tblarinvoices_dispatchedbysysuid_set', blank=True, null=True)  # Field name made lowercase.
    datetimedispatched = models.DateTimeField(db_column='DateTimeDispatched', blank=True, null=True)  # Field name made lowercase.
    scutimestamp = models.DateTimeField(db_column='SCUTimestamp')  # Field name made lowercase.
    scuserialnumber = models.CharField(db_column='SCUSerialNumber', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    scuinvoicenumber = models.CharField(db_column='SCUInvoiceNumber', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    internaldata = models.CharField(db_column='InternalData', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    receiptsignature = models.CharField(db_column='ReceiptSignature', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    qrcode = models.CharField(db_column='QRCode', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    isetimsinvoice = models.SmallIntegerField(db_column='IsETimsInvoice')  # Field name made lowercase.
    taxableamounta = models.DecimalField(db_column='TaxableAmountA', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamounta = models.DecimalField(db_column='TaxAmountA', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxableamountb = models.DecimalField(db_column='TaxableAmountB', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamountb = models.DecimalField(db_column='TaxAmountB', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxableamountc = models.DecimalField(db_column='TaxableAmountC', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamountc = models.DecimalField(db_column='TaxAmountC', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxableamountd = models.DecimalField(db_column='TaxableAmountD', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamountd = models.DecimalField(db_column='TaxAmountD', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxableamounte = models.DecimalField(db_column='TaxableAmountE', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamounte = models.DecimalField(db_column='TaxAmountE', max_digits=100, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblarinvoices'
        unique_together = (('arinvoiceid', 'covertoarinvoiceid'),)


class Tblbanks(models.Model):
    bankid = models.BigAutoField(db_column='BankID', primary_key=True)  # Field name made lowercase.
    bankcode = models.CharField(db_column='BankCode', max_length=255)  # Field name made lowercase.
    subaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='SubAccountID')  # Field name made lowercase.
    accountno = models.CharField(db_column='AccountNo', max_length=255)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=255)  # Field name made lowercase.
    companybranchid = models.ForeignKey('Tblcompanybranchs', models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblbanks'
        unique_together = (('name', 'companybranchid'),)


class Tblcashflowcategorys(models.Model):
    cashflowcategoryid = models.BigAutoField(db_column='CashFlowCategoryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    companybranchid = models.ForeignKey('Tblcompanybranchs', models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcashflowcategorys'
        unique_together = (('name', 'companybranchid'),)


class Tblcompanybranchitems(models.Model):
    companybranchitemid = models.BigAutoField(db_column='CompanyBranchItemID', primary_key=True)  # Field name made lowercase.
    companybranchid = models.ForeignKey('Tblcompanybranchs', models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    itemid = models.ForeignKey('Tblitems', models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
    assetsubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='AssetSubAccountID', blank=True, null=True)  # Field name made lowercase.
    revenuesubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='RevenueSubAccountID', related_name='tblcompanybranchitems_revenuesubaccountid_set', blank=True, null=True)  # Field name made lowercase.
    costofsalesubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='CostOfSaleSubAccountID', related_name='tblcompanybranchitems_costofsalesubaccountid_set')  # Field name made lowercase.
    vattypeid = models.ForeignKey('Tblvattypes', models.DO_NOTHING, db_column='VATTypeID')  # Field name made lowercase.
    othertaxid = models.ForeignKey('Tblothertaxs', models.DO_NOTHING, db_column='OtherTaxID', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='ItemCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='Barcode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    iteminformationsenttoetims = models.SmallIntegerField(db_column='ItemInformationSentToETims')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcompanybranchitems'
        unique_together = (('itemid', 'companybranchid'),)


class Tblcompanybranchs(models.Model):
    companybranchid = models.BigAutoField(db_column='CompanyBranchID', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey('Tblcompanys', models.DO_NOTHING, db_column='CompanyID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    buildingname = models.CharField(db_column='BuildingName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetname = models.CharField(db_column='StreetName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postaladdress = models.CharField(db_column='PostalAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    townid = models.ForeignKey('Tbltowns', models.DO_NOTHING, db_column='TownID', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telephone1 = models.CharField(db_column='Telephone1', max_length=255)  # Field name made lowercase.
    telephone2 = models.CharField(db_column='Telephone2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telephone3 = models.CharField(db_column='Telephone3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    letterhead = models.CharField(db_column='LetterHead', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ismainbranch = models.SmallIntegerField(db_column='IsMainBranch')  # Field name made lowercase.
    branchlatitude = models.DecimalField(db_column='BranchLatitude', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    branchlongitude = models.DecimalField(db_column='BranchLongitude', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    timezoneoffset = models.CharField(db_column='TimeZoneOffset', max_length=255)  # Field name made lowercase.
    timezone = models.CharField(db_column='TimeZone', max_length=1000)  # Field name made lowercase.
    timezoneoffsetvalue = models.CharField(db_column='TimeZoneOffsetValue', max_length=1000)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcompanybranchs'


class Tblcompanys(models.Model):
    companyid = models.BigAutoField(db_column='CompanyID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationno = models.CharField(db_column='RegistrationNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pinno = models.CharField(db_column='PinNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vatno = models.CharField(db_column='VATNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agentno = models.CharField(db_column='AgentNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    value0 = models.CharField(db_column='Value0', max_length=500, blank=True, null=True)  # Field name made lowercase.
    value1 = models.CharField(db_column='Value1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    value2 = models.CharField(db_column='Value2', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcompanys'


class Tblconsumeditems(models.Model):
    consumeditemid = models.BigAutoField(db_column='ConsumedItemID', primary_key=True)  # Field name made lowercase.
    itemstoragelocationid = models.ForeignKey('Tblitemstoragelocations', models.DO_NOTHING, db_column='ItemStorageLocationID')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdbysysuid = models.IntegerField(db_column='CreatedBySysUID')  # Field name made lowercase.
    hasbeencommittedtostock = models.SmallIntegerField(db_column='HasBeenCommittedToStock')  # Field name made lowercase.
    datetimeconsumed = models.DateTimeField(db_column='DateTimeConsumed')  # Field name made lowercase.
    datetimecommittedtostock = models.DateTimeField(db_column='DateTimeCommittedToStock')  # Field name made lowercase.
    committedbysysuid = models.IntegerField(db_column='CommittedBySysUID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblconsumeditems'


class Tblcustomerbillarinvoices(models.Model):
    customerbillarinvoiceid = models.BigAutoField(db_column='CustomerBillARInvoiceID', primary_key=True)  # Field name made lowercase.
    customerbillid = models.ForeignKey('Tblcustomerbills', models.DO_NOTHING, db_column='CustomerBillID')  # Field name made lowercase.
    arinvoiceid = models.ForeignKey(Tblarinvoices, models.DO_NOTHING, db_column='ARInvoiceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomerbillarinvoices'


class Tblcustomerbillitems(models.Model):
    customerbillitemid = models.BigAutoField(db_column='CustomerBillItemID', primary_key=True)  # Field name made lowercase.
    journalvoucherid = models.ForeignKey('Tbljournalvouchers', models.DO_NOTHING, db_column='JournalVoucherID', blank=True, null=True)  # Field name made lowercase.
    customerbillid = models.ForeignKey('Tblcustomerbills', models.DO_NOTHING, db_column='CustomerBillID')  # Field name made lowercase.
    itemstoragelocationid = models.ForeignKey('Tblitemstoragelocations', models.DO_NOTHING, db_column='ItemStorageLocationID', blank=True, null=True)  # Field name made lowercase.
    arinvoiceid = models.ForeignKey(Tblarinvoices, models.DO_NOTHING, db_column='ARInvoiceID', blank=True, null=True)  # Field name made lowercase.
    datetimebilled = models.DateTimeField(db_column='DateTimeBilled')  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=100, decimal_places=2)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    costamount = models.DecimalField(db_column='CostAmount', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amountbeforediscount = models.DecimalField(db_column='AmountBeforeDiscount', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amountafterdiscount = models.DecimalField(db_column='AmountAfterDiscount', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vattypeid = models.IntegerField(db_column='VATTypeID')  # Field name made lowercase.
    vatamount = models.DecimalField(db_column='VATAmount', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    othertaxid = models.IntegerField(db_column='OtherTaxID', blank=True, null=True)  # Field name made lowercase.
    netamount = models.DecimalField(db_column='NetAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    hasbeenpaidfor = models.SmallIntegerField(db_column='HasBeenPaidFor')  # Field name made lowercase.
    issuedreceiptid = models.ForeignKey('Tblissuedreceipts', models.DO_NOTHING, db_column='IssuedReceiptID', blank=True, null=True)  # Field name made lowercase.
    saletype = models.SmallIntegerField(db_column='SaleType')  # Field name made lowercase.
    createdbysysuid = models.IntegerField(db_column='CreatedBySysUID')  # Field name made lowercase.
    dispensedbysysuid = models.IntegerField(db_column='DispensedBySysUID', blank=True, null=True)  # Field name made lowercase.
    hasbeendispensed = models.SmallIntegerField(db_column='HasBeenDispensed')  # Field name made lowercase.
    customerschemeid = models.ForeignKey('Tblcustomerschemes', models.DO_NOTHING, db_column='CustomerSchemeID', blank=True, null=True)  # Field name made lowercase.
    companybranchitemid = models.ForeignKey(Tblcompanybranchitems, models.DO_NOTHING, db_column='CompanyBranchItemID')  # Field name made lowercase.
    inputitemstoragelocationid = models.ForeignKey('Tblstoragelocations', models.DO_NOTHING, db_column='InputItemStorageLocationID', blank=True, null=True)  # Field name made lowercase.
    schemeid = models.ForeignKey('Tblschemes', models.DO_NOTHING, db_column='SchemeID', blank=True, null=True)  # Field name made lowercase.
    visitrequestedtestitemid = models.ForeignKey('Tblvisitrequestedtestitems', models.DO_NOTHING, db_column='VisitRequestedTestItemID', blank=True, null=True)  # Field name made lowercase.
    visitrequestedexaminationitemid = models.ForeignKey('Tblvisitrequestedexaminationitems', models.DO_NOTHING, db_column='VisitRequestedExaminationItemID', blank=True, null=True)  # Field name made lowercase.
    theatrenoteid = models.ForeignKey('Tbltheatrenotes', models.DO_NOTHING, db_column='TheatreNoteID', blank=True, null=True)  # Field name made lowercase.
    medicalclinicvisitprocedureid = models.ForeignKey('Tblmedicalclinicvisitprocedures', models.DO_NOTHING, db_column='MedicalClinicVisitProcedureID', blank=True, null=True)  # Field name made lowercase.
    wasoffsetfromdeposit = models.SmallIntegerField(db_column='WasOffsetFromDeposit', blank=True, null=True)  # Field name made lowercase.
    prescriptionitemid = models.ForeignKey('Tblprescriptionitems', models.DO_NOTHING, db_column='PrescriptionItemID', blank=True, null=True)  # Field name made lowercase.
    commentondiscount = models.CharField(db_column='CommentOnDiscount', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    discountbysysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='DiscountBySysUID', blank=True, null=True)  # Field name made lowercase.
    drugadminid = models.ForeignKey('Tbldrugadmins', models.DO_NOTHING, db_column='DrugAdminID', blank=True, null=True)  # Field name made lowercase.
    drugadminitemid = models.ForeignKey('Tbldrugadminitems', models.DO_NOTHING, db_column='DrugAdminItemID', blank=True, null=True)  # Field name made lowercase.
    inputitemsreserved = models.SmallIntegerField(db_column='InputItemsReserved')  # Field name made lowercase.
    consultantamount = models.DecimalField(db_column='ConsultantAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    datetimeoffsetfromdeposit = models.DateTimeField(db_column='DateTimeOffsetFromDeposit')  # Field name made lowercase.
    isautomaticallybilled = models.SmallIntegerField(db_column='IsAutomaticallyBilled')  # Field name made lowercase.
    billitemversion = models.SmallIntegerField(db_column='BillItemVersion')  # Field name made lowercase.
    datetimedispensed = models.DateTimeField(db_column='DateTimeDispensed')  # Field name made lowercase.
    hieinterventionname = models.CharField(db_column='HIEInterventionName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hieinterventioncode = models.CharField(db_column='HIEInterventionCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hieschemecode = models.CharField(db_column='HIESchemeCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomerbillitems'


class Tblcustomerbills(models.Model):
    customerbillid = models.BigAutoField(db_column='CustomerBillID', primary_key=True)  # Field name made lowercase.
    visitid = models.ForeignKey('Tblvisits', models.DO_NOTHING, db_column='VisitID')  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated')  # Field name made lowercase.
    totalbillamount = models.DecimalField(db_column='TotalBillAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    totalamountpaid = models.DecimalField(db_column='TotalAmountPaid', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isfinalised = models.SmallIntegerField(db_column='IsFinalised')  # Field name made lowercase.
    finalisedbysysuid = models.IntegerField(db_column='FinalisedBySysUID', blank=True, null=True)  # Field name made lowercase.
    ispatient = models.SmallIntegerField(db_column='IsPatient')  # Field name made lowercase.
    bonus = models.CharField(db_column='Bonus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datetimefinalised = models.DateTimeField(db_column='DateTimeFinalised', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coveramount = models.DecimalField(db_column='CoverAmount', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    depositoffset = models.DecimalField(db_column='DepositOffset', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salesdiscountamount = models.DecimalField(db_column='SalesDiscountAmount', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    writtenoffamount = models.DecimalField(db_column='WrittenOffAmount', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    depositbalance = models.DecimalField(db_column='DepositBalance', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    refund = models.DecimalField(db_column='Refund', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rebateamount = models.DecimalField(db_column='RebateAmount', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    copaymentamount = models.DecimalField(db_column='CopaymentAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    smartbenefitid = models.IntegerField(db_column='SmartBenefitID')  # Field name made lowercase.
    smartbenefitamount = models.DecimalField(db_column='SmartBenefitAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    smartbenefitname = models.CharField(db_column='SmartBenefitName', max_length=5000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomerbills'


class Tblcustomers(models.Model):
    customerid = models.BigAutoField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255)  # Field name made lowercase.
    othernames = models.CharField(db_column='OtherNames', max_length=255)  # Field name made lowercase.
    sex = models.SmallIntegerField(db_column='Sex')  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateOfBirth')  # Field name made lowercase.
    occupationid = models.ForeignKey('Tbloccupations', models.DO_NOTHING, db_column='OccupationID')  # Field name made lowercase.
    residence = models.CharField(db_column='Residence', max_length=255)  # Field name made lowercase.
    postaladdress = models.CharField(db_column='PostalAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    townid = models.ForeignKey('Tbltowns', models.DO_NOTHING, db_column='TownID')  # Field name made lowercase.
    nextofkin = models.CharField(db_column='NextOfKin', max_length=255)  # Field name made lowercase.
    nextofkinrelationship = models.CharField(db_column='NextOfKinRelationship', max_length=255)  # Field name made lowercase.
    nextofkincontact = models.CharField(db_column='NextOfKinContact', max_length=255)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateregistered = models.DateTimeField(db_column='DateRegistered')  # Field name made lowercase.
    idtypeid = models.SmallIntegerField(db_column='IDTypeID')  # Field name made lowercase.
    idnumber = models.CharField(db_column='IDNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outpatientno = models.CharField(db_column='OutPatientNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inpatientno = models.CharField(db_column='InPatientNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telephone1 = models.CharField(db_column='Telephone1', max_length=255)  # Field name made lowercase.
    telephone2 = models.CharField(db_column='Telephone2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nationalityid = models.ForeignKey('Tblnationalitys', models.DO_NOTHING, db_column='NationalityID')  # Field name made lowercase.
    registeredbysysuid = models.IntegerField(db_column='RegisteredBySysUID')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    registeredatcompanybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='RegisteredAtCompanyBranchID')  # Field name made lowercase.
    smartglobalid = models.CharField(db_column='SmartGlobalID', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    inoutpatientnoprefix = models.CharField(db_column='InOutPatientNoPrefix', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('Tblemployees', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  # Field name made lowercase.
    isdependant = models.SmallIntegerField(db_column='IsDependant')  # Field name made lowercase.
    estate = models.CharField(db_column='Estate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hiecrid = models.CharField(db_column='HIECRId', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomers'
        unique_together = (('idnumber', 'nationalityid'),)


class Tblcustomerschemes(models.Model):
    customerschemeid = models.BigAutoField(db_column='CustomerSchemeID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Tblcustomers, models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.
    schemeid = models.ForeignKey('Tblschemes', models.DO_NOTHING, db_column='SchemeID')  # Field name made lowercase.
    isprincipalmember = models.SmallIntegerField(db_column='IsPrincipalMember')  # Field name made lowercase.
    principalmember = models.CharField(db_column='PrincipalMember', max_length=255, blank=True, null=True)  # Field name made lowercase.
    membershipno = models.CharField(db_column='MembershipNo', max_length=255)  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblcustomerschemes'


class Tbldepartments(models.Model):
    departmentid = models.BigAutoField(db_column='DepartmentID', primary_key=True)  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldepartments'
        unique_together = (('name', 'companybranchid'),)


class Tbldiagnosiss(models.Model):
    diagnosisid = models.BigAutoField(db_column='DiagnosisID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    diseasecode = models.CharField(db_column='DiseaseCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldiagnosiss'
        unique_together = (('name', 'diseasecode'),)


class Tbldrugadminitems(models.Model):
    drugadminitemid = models.BigAutoField(db_column='DrugAdminItemID', primary_key=True)  # Field name made lowercase.
    drugadminid = models.ForeignKey('Tbldrugadmins', models.DO_NOTHING, db_column='DrugAdminID')  # Field name made lowercase.
    stateddatetime = models.DateTimeField(db_column='StatedDateTime')  # Field name made lowercase.
    datetimeadministered = models.DateTimeField(db_column='DateTimeAdministered', blank=True, null=True)  # Field name made lowercase.
    administeredbysysuid = models.IntegerField(db_column='AdministeredBySysUID', blank=True, null=True)  # Field name made lowercase.
    hasbeenadministered = models.SmallIntegerField(db_column='HasBeenAdministered')  # Field name made lowercase.
    reasonifnotadministered = models.IntegerField(db_column='ReasonIfNotAdministered', blank=True, null=True)  # Field name made lowercase.
    hasbeendispensed = models.SmallIntegerField(db_column='HasBeenDispensed')  # Field name made lowercase.
    customerbillitemid = models.ForeignKey(Tblcustomerbillitems, models.DO_NOTHING, db_column='CustomerBillItemID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldrugadminitems'


class Tbldrugadmins(models.Model):
    drugadminid = models.BigAutoField(db_column='DrugAdminID', primary_key=True)  # Field name made lowercase.
    itemstoragelocationid = models.ForeignKey('Tblitemstoragelocations', models.DO_NOTHING, db_column='ItemStorageLocationID')  # Field name made lowercase.
    route = models.CharField(db_column='Route', max_length=255, blank=True, null=True)  # Field name made lowercase.
    strength = models.CharField(db_column='Strength', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantitypertime = models.DecimalField(db_column='QuantityPerTime', max_digits=100, decimal_places=2)  # Field name made lowercase.
    dosageunit = models.CharField(db_column='DosageUnit', max_length=255)  # Field name made lowercase.
    dosageform = models.CharField(db_column='DosageForm', max_length=255)  # Field name made lowercase.
    frequencyperday = models.IntegerField(db_column='FrequencyPerDay')  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration')  # Field name made lowercase.
    periodin = models.SmallIntegerField(db_column='PeriodIn')  # Field name made lowercase.
    otherinstructions = models.CharField(db_column='OtherInstructions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    medicalclinicvisitid = models.ForeignKey('Tblmedicalclinicvisits', models.DO_NOTHING, db_column='MedicalClinicVisitID', blank=True, null=True)  # Field name made lowercase.
    isstatdose = models.IntegerField(db_column='IsStatDose')  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated')  # Field name made lowercase.
    datetimestarting = models.DateTimeField(db_column='DateTimeStarting', blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    isbilledanddispensedonce = models.SmallIntegerField(db_column='IsBilledAndDispensedOnce')  # Field name made lowercase.
    admissionid = models.ForeignKey(Tbladmissions, models.DO_NOTHING, db_column='AdmissionID')  # Field name made lowercase.
    customerschemeid = models.ForeignKey(Tblcustomerschemes, models.DO_NOTHING, db_column='CustomerSchemeID')  # Field name made lowercase.
    isdiscontinued = models.SmallIntegerField(db_column='IsDiscontinued')  # Field name made lowercase.
    discontinuedbysysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='DiscontinuedBySysUID', blank=True, null=True)  # Field name made lowercase.
    datetimediscontinued = models.DateTimeField(db_column='DateTimeDiscontinued')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbldrugadmins'


class Tblemployees(models.Model):
    employeeid = models.BigAutoField(db_column='EmployeeID', primary_key=True)  # Field name made lowercase.
    staffno = models.IntegerField(db_column='StaffNo', unique=True, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255)  # Field name made lowercase.
    othernames = models.CharField(db_column='OtherNames', max_length=255)  # Field name made lowercase.
    idtype = models.SmallIntegerField(db_column='IDType')  # Field name made lowercase.
    idno = models.CharField(db_column='IDNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateemployed = models.DateTimeField(db_column='DateEmployed')  # Field name made lowercase.
    departmentid = models.ForeignKey(Tbldepartments, models.DO_NOTHING, db_column='DepartmentID')  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    physicaladdress = models.CharField(db_column='PhysicalAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postaladdress = models.CharField(db_column='PostalAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    townid = models.ForeignKey('Tbltowns', models.DO_NOTHING, db_column='TownID')  # Field name made lowercase.
    telephone1 = models.CharField(db_column='Telephone1', max_length=255)  # Field name made lowercase.
    telephone2 = models.CharField(db_column='Telephone2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.SmallIntegerField(db_column='Sex')  # Field name made lowercase.
    nextofkin = models.CharField(db_column='NextOfKin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nokrelationship = models.CharField(db_column='NOKRelationship', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nokcontact = models.CharField(db_column='NOKContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateOfBirth')  # Field name made lowercase.
    paymentmodeid = models.ForeignKey('Tblpaymentmodes', models.DO_NOTHING, db_column='PaymentModeID')  # Field name made lowercase.
    bankid = models.ForeignKey(Tblbanks, models.DO_NOTHING, db_column='BankID', blank=True, null=True)  # Field name made lowercase.
    bankaccountno = models.CharField(db_column='BankAccountNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    payrollno = models.CharField(db_column='PayRollNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    paymentmoderefno = models.CharField(db_column='PaymentModeRefNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nokplaceofwork = models.CharField(db_column='NOKPlaceOfWork', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nokoccupation = models.CharField(db_column='NOKOccupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nokidtype = models.SmallIntegerField(db_column='NOKIDType')  # Field name made lowercase.
    nokidnumber = models.CharField(db_column='NOKIDNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currentresidence = models.CharField(db_column='CurrentResidence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    streetandhousenumber = models.CharField(db_column='StreetAndHouseNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    employmenttype = models.SmallIntegerField(db_column='EmploymentType')  # Field name made lowercase.
    isterminated = models.SmallIntegerField(db_column='IsTerminated')  # Field name made lowercase.
    maritalstatus = models.SmallIntegerField(db_column='MaritalStatus')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    nationalityid = models.ForeignKey('Tblnationalitys', models.DO_NOTHING, db_column='NationalityID')  # Field name made lowercase.
    systemuserid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='SystemUserID', blank=True, null=True)  # Field name made lowercase.
    portalaccesscode = models.CharField(db_column='PortalAccessCode', max_length=500, blank=True, null=True)  # Field name made lowercase.
    canaccessportal = models.SmallIntegerField(db_column='CanAccessPortal')  # Field name made lowercase.
    terminationdatetime = models.DateTimeField(db_column='TerminationDateTime')  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankbranch = models.CharField(db_column='BankBranch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankbranchcode = models.CharField(db_column='BankBranchCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fingerprint = models.BinaryField(db_column='Fingerprint', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblemployees'


class Tblexaminations(models.Model):
    examinationid = models.BigAutoField(db_column='ExaminationID', primary_key=True)  # Field name made lowercase.
    companybranchitemid = models.ForeignKey(Tblcompanybranchitems, models.DO_NOTHING, db_column='CompanyBranchItemID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblexaminations'
        unique_together = (('name', 'companybranchitemid'),)


class Tblfiscalperiods(models.Model):
    fiscalperiodid = models.BigAutoField(db_column='FiscalPeriodID', primary_key=True)  # Field name made lowercase.
    opendate = models.DateTimeField(db_column='OpenDate')  # Field name made lowercase.
    closedate = models.DateTimeField(db_column='CloseDate')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    isopen = models.SmallIntegerField(db_column='IsOpen')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    fiscalperiodno = models.IntegerField(db_column='FiscalPeriodNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblfiscalperiods'


class Tblinterbranchorderitems(models.Model):
    interbranchorderitemid = models.BigAutoField(db_column='InterbranchOrderItemID', primary_key=True)  # Field name made lowercase.
    interbranchorderid = models.ForeignKey('Tblinterbranchorders', models.DO_NOTHING, db_column='InterbranchOrderID')  # Field name made lowercase.
    itemstoragelocationid = models.ForeignKey('Tblitemstoragelocations', models.DO_NOTHING, db_column='ItemStorageLocationID')  # Field name made lowercase.
    quantityordered = models.DecimalField(db_column='QuantityOrdered', max_digits=10, decimal_places=2)  # Field name made lowercase.
    quantityissued = models.DecimalField(db_column='QuantityIssued', max_digits=10, decimal_places=2)  # Field name made lowercase.
    earliestexpirydate = models.DateTimeField(db_column='EarliestExpiryDate')  # Field name made lowercase.
    issuedtotalpackedquantity = models.DecimalField(db_column='IssuedTotalPackedQuantity', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitofmeasureid = models.ForeignKey('Tblunitofmeasures', models.DO_NOTHING, db_column='UnitOfMeasureID')  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=10, decimal_places=2)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    availableinissuinglocation = models.SmallIntegerField(db_column='AvailableInIssuingLocation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblinterbranchorderitems'


class Tblinterbranchorders(models.Model):
    interbranchorderid = models.BigAutoField(db_column='InterbranchOrderID', primary_key=True)  # Field name made lowercase.
    requestingstoragelocationid = models.ForeignKey('Tblstoragelocations', models.DO_NOTHING, db_column='RequestingStorageLocationID')  # Field name made lowercase.
    issuingstoragelocationid = models.ForeignKey('Tblstoragelocations', models.DO_NOTHING, db_column='IssuingStorageLocationID', related_name='tblinterbranchorders_issuingstoragelocationid_set')  # Field name made lowercase.
    preparedbysysuid = models.IntegerField(db_column='PreparedBySysUID')  # Field name made lowercase.
    approvedbysysuid = models.IntegerField(db_column='ApprovedBySysUID', blank=True, null=True)  # Field name made lowercase.
    orderitemsdispatched = models.SmallIntegerField(db_column='OrderItemsDispatched')  # Field name made lowercase.
    itemsdispatchedbysysuid = models.IntegerField(db_column='ItemsDispatchedBySysUID', blank=True, null=True)  # Field name made lowercase.
    itemsreceived = models.SmallIntegerField(db_column='ItemsReceived')  # Field name made lowercase.
    itemsreceivedbysysuid = models.IntegerField(db_column='ItemsReceivedBySysUID', blank=True, null=True)  # Field name made lowercase.
    datetimedispatched = models.DateTimeField(db_column='DateTimeDispatched')  # Field name made lowercase.
    datetimereceived = models.DateTimeField(db_column='DateTimeReceived')  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated')  # Field name made lowercase.
    orderstatus = models.SmallIntegerField(db_column='OrderStatus', blank=True, null=True)  # Field name made lowercase.
    requestinglocationcomment = models.CharField(db_column='RequestingLocationComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hasbeenapproved = models.SmallIntegerField(db_column='HasBeenApproved')  # Field name made lowercase.
    issuinglocationcomment = models.CharField(db_column='IssuingLocationComment', max_length=500, blank=True, null=True)  # Field name made lowercase.
    hasbeensent = models.SmallIntegerField(db_column='HasBeenSent')  # Field name made lowercase.
    datetimesent = models.DateTimeField(db_column='DateTimeSent')  # Field name made lowercase.
    iscommittedtostock = models.SmallIntegerField(db_column='IsCommittedToStock')  # Field name made lowercase.
    committedbysysuid = models.IntegerField(db_column='CommittedBySysUID', blank=True, null=True)  # Field name made lowercase.
    hasbeencancelled = models.SmallIntegerField(db_column='HasBeenCancelled')  # Field name made lowercase.
    cancellationreason = models.CharField(db_column='CancellationReason', max_length=500, blank=True, null=True)  # Field name made lowercase.
    isstock = models.SmallIntegerField(db_column='IsStock')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    issuingcompanybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='IssuingCompanyBranchID', related_name='tblinterbranchorders_issuingcompanybranchid_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblinterbranchorders'


class Tblinternalorderitems(models.Model):
    internalorderitemid = models.BigAutoField(db_column='InternalOrderItemID', primary_key=True)  # Field name made lowercase.
    internalorderid = models.ForeignKey('Tblinternalorders', models.DO_NOTHING, db_column='InternalOrderID')  # Field name made lowercase.
    itemstoragelocationid = models.ForeignKey('Tblitemstoragelocations', models.DO_NOTHING, db_column='ItemStorageLocationID')  # Field name made lowercase.
    quantityordered = models.DecimalField(db_column='QuantityOrdered', max_digits=100, decimal_places=2)  # Field name made lowercase.
    quantityissued = models.DecimalField(db_column='QuantityIssued', max_digits=100, decimal_places=2)  # Field name made lowercase.
    earliestexpirydate = models.DateTimeField(db_column='EarliestExpiryDate')  # Field name made lowercase.
    issuedtotalpackedquantity = models.DecimalField(db_column='IssuedTotalPackedQuantity', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unitofmeasureid = models.ForeignKey('Tblunitofmeasures', models.DO_NOTHING, db_column='UnitOfMeasureID')  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=100, decimal_places=2)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=100, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblinternalorderitems'


class Tblinternalorders(models.Model):
    internalorderid = models.BigAutoField(db_column='InternalOrderID', primary_key=True)  # Field name made lowercase.
    requestingstoragelocationid = models.ForeignKey('Tblstoragelocations', models.DO_NOTHING, db_column='RequestingStorageLocationID')  # Field name made lowercase.
    issuingstoragelocationid = models.ForeignKey('Tblstoragelocations', models.DO_NOTHING, db_column='IssuingStorageLocationID', related_name='tblinternalorders_issuingstoragelocationid_set')  # Field name made lowercase.
    preparedbysysuid = models.IntegerField(db_column='PreparedBySysUID')  # Field name made lowercase.
    approvedbysysuid = models.IntegerField(db_column='ApprovedBySysUID', blank=True, null=True)  # Field name made lowercase.
    orderitemsdispatched = models.SmallIntegerField(db_column='OrderItemsDispatched')  # Field name made lowercase.
    itemsdispatchedbysysuid = models.IntegerField(db_column='ItemsDispatchedBySysUID', blank=True, null=True)  # Field name made lowercase.
    itemsreceived = models.SmallIntegerField(db_column='ItemsReceived')  # Field name made lowercase.
    itemsreceivedbysysuid = models.IntegerField(db_column='ItemsReceivedBySysUID', blank=True, null=True)  # Field name made lowercase.
    datetimedispatched = models.DateTimeField(db_column='DateTimeDispatched', blank=True, null=True)  # Field name made lowercase.
    datetimereceived = models.DateTimeField(db_column='DateTimeReceived', blank=True, null=True)  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated', blank=True, null=True)  # Field name made lowercase.
    orderstatus = models.SmallIntegerField(db_column='OrderStatus')  # Field name made lowercase.
    requestinglocationcomment = models.CharField(db_column='RequestingLocationComment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hasbeenapproved = models.SmallIntegerField(db_column='HasBeenApproved')  # Field name made lowercase.
    issuinglocationcomment = models.CharField(db_column='IssuingLocationComment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hasbeensent = models.SmallIntegerField(db_column='HasBeenSent')  # Field name made lowercase.
    datetimesent = models.DateTimeField(db_column='DateTimeSent', blank=True, null=True)  # Field name made lowercase.
    iscommittedtostock = models.SmallIntegerField(db_column='IsCommittedToStock')  # Field name made lowercase.
    committedbysysuid = models.IntegerField(db_column='CommittedBySysUID', blank=True, null=True)  # Field name made lowercase.
    hasbeencancelled = models.SmallIntegerField(db_column='HasBeenCancelled')  # Field name made lowercase.
    cancellationreason = models.CharField(db_column='CancellationReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isstock = models.SmallIntegerField(db_column='IsStock')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblinternalorders'


class Tblissuedreceipts(models.Model):
    issuedreceiptid = models.BigAutoField(db_column='IssuedReceiptID', primary_key=True)  # Field name made lowercase.
    datetimeissued = models.DateTimeField(db_column='DateTimeIssued')  # Field name made lowercase.
    amountpaid = models.DecimalField(db_column='AmountPaid', max_digits=100, decimal_places=2)  # Field name made lowercase.
    issuedbysysuid = models.IntegerField(db_column='IssuedBySysUID')  # Field name made lowercase.
    amounttendered = models.DecimalField(db_column='AmountTendered', max_digits=100, decimal_places=2)  # Field name made lowercase.
    changeamount = models.DecimalField(db_column='ChangeAmount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    paidinby = models.CharField(db_column='PaidInBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentfor = models.CharField(db_column='PaymentFor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    issuedto = models.CharField(db_column='IssuedTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typeofsale = models.SmallIntegerField(db_column='TypeOfSale')  # Field name made lowercase.
    customerbillid = models.ForeignKey(Tblcustomerbills, models.DO_NOTHING, db_column='CustomerBillID', blank=True, null=True)  # Field name made lowercase.
    customerbillarinvoiceid = models.ForeignKey(Tblcustomerbillarinvoices, models.DO_NOTHING, db_column='CustomerBillARInvoiceID', blank=True, null=True)  # Field name made lowercase.
    paymentmodeid = models.ForeignKey('Tblpaymentmodes', models.DO_NOTHING, db_column='PaymentModeID')  # Field name made lowercase.
    hasbeencancelled = models.SmallIntegerField(db_column='HasBeenCancelled')  # Field name made lowercase.
    cancellationreason = models.CharField(db_column='CancellationReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cancelledbysysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='CancelledBySysUID', blank=True, null=True)  # Field name made lowercase.
    chequedrawer = models.CharField(db_column='ChequeDrawer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chequeissuingbank = models.CharField(db_column='ChequeIssuingBank', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chequeissuingbranch = models.CharField(db_column='ChequeIssuingBranch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chequeno = models.CharField(db_column='ChequeNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentrefno = models.CharField(db_column='PaymentRefNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chequedate = models.DateTimeField(db_column='ChequeDate', blank=True, null=True)  # Field name made lowercase.
    cardno = models.CharField(db_column='CardNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentisprocessed = models.SmallIntegerField(db_column='PaymentIsProcessed')  # Field name made lowercase.
    isrejected = models.SmallIntegerField(db_column='IsRejected', blank=True, null=True)  # Field name made lowercase.
    rejectionreason = models.CharField(db_column='RejectionReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iscustomerdeposit = models.SmallIntegerField(db_column='IsCustomerDeposit')  # Field name made lowercase.
    isdebtorpayment = models.SmallIntegerField(db_column='IsDebtorPayment')  # Field name made lowercase.
    hasbeenpartiallycancelled = models.SmallIntegerField(db_column='HasBeenPartiallyCancelled')  # Field name made lowercase.
    iscopayment = models.SmallIntegerField(db_column='IsCopayment')  # Field name made lowercase.
    description = models.CharField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    companybranchid = models.BigIntegerField(db_column='CompanyBranchID')  # Field name made lowercase.
    isrefundonadvance = models.SmallIntegerField(db_column='IsRefundOnAdvance')  # Field name made lowercase.
    journalvoucherid = models.ForeignKey('Tbljournalvouchers', models.DO_NOTHING, db_column='JournalVoucherID', blank=True, null=True)  # Field name made lowercase.
    ispartialpayment = models.SmallIntegerField(db_column='IsPartialPayment')  # Field name made lowercase.
    datetimecancelled = models.DateTimeField(db_column='DateTimeCancelled')  # Field name made lowercase.
    discrepancyisfixed = models.SmallIntegerField(db_column='DiscrepancyIsFixed')  # Field name made lowercase.
    scutimestamp = models.DateTimeField(db_column='SCUTimestamp')  # Field name made lowercase.
    scuserialnumber = models.CharField(db_column='SCUSerialNumber', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    scuinvoicenumber = models.CharField(db_column='SCUInvoiceNumber', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    internaldata = models.CharField(db_column='InternalData', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    receiptsignature = models.CharField(db_column='ReceiptSignature', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    qrcode = models.CharField(db_column='QRCode', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    isetimsinvoice = models.SmallIntegerField(db_column='IsETimsInvoice')  # Field name made lowercase.
    taxableamounta = models.DecimalField(db_column='TaxableAmountA', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamounta = models.DecimalField(db_column='TaxAmountA', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxableamountb = models.DecimalField(db_column='TaxableAmountB', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamountb = models.DecimalField(db_column='TaxAmountB', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxableamountc = models.DecimalField(db_column='TaxableAmountC', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamountc = models.DecimalField(db_column='TaxAmountC', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxableamountd = models.DecimalField(db_column='TaxableAmountD', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamountd = models.DecimalField(db_column='TaxAmountD', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxableamounte = models.DecimalField(db_column='TaxableAmountE', max_digits=100, decimal_places=2)  # Field name made lowercase.
    taxamounte = models.DecimalField(db_column='TaxAmountE', max_digits=100, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblissuedreceipts'


class Tblitemcategorys(models.Model):
    itemcategoryid = models.BigAutoField(db_column='ItemCategoryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblitemcategorys'


class Tblitemclasss(models.Model):
    itemclassid = models.BigAutoField(db_column='ItemClassID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    itemclasstype = models.SmallIntegerField(db_column='ItemClassType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblitemclasss'


class Tblitems(models.Model):
    itemid = models.BigAutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    unitofmeasureid = models.ForeignKey('Tblunitofmeasures', models.DO_NOTHING, db_column='UnitOfMeasureID', blank=True, null=True)  # Field name made lowercase.
    itemclassid = models.ForeignKey(Tblitemclasss, models.DO_NOTHING, db_column='ItemClassID', blank=True, null=True)  # Field name made lowercase.
    itemcategoryid = models.ForeignKey(Tblitemcategorys, models.DO_NOTHING, db_column='ItemCategoryID')  # Field name made lowercase.
    appreciatesordepreciates = models.SmallIntegerField(db_column='AppreciatesOrDepreciates', blank=True, null=True)  # Field name made lowercase.
    appreciationdepreciationrate = models.DecimalField(db_column='AppreciationDepreciationRate', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    etimsitemsequencenumber = models.IntegerField(db_column='ETimsItemSequenceNumber')  # Field name made lowercase.
    countryoforigin = models.CharField(db_column='CountryOfOrigin', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblitems'


class Tblitemstoragelocations(models.Model):
    itemstoragelocationid = models.BigAutoField(db_column='ItemStorageLocationID', primary_key=True)  # Field name made lowercase.
    companybranchitemid = models.ForeignKey(Tblcompanybranchitems, models.DO_NOTHING, db_column='CompanyBranchItemID')  # Field name made lowercase.
    storagelocationid = models.ForeignKey('Tblstoragelocations', models.DO_NOTHING, db_column='StorageLocationID')  # Field name made lowercase.
    batch = models.CharField(db_column='Batch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=100, decimal_places=2)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate')  # Field name made lowercase.
    totalquantity = models.DecimalField(db_column='TotalQuantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    availablequantity = models.DecimalField(db_column='AvailableQuantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    isretiredbatch = models.SmallIntegerField(db_column='IsRetiredBatch')  # Field name made lowercase.
    reorderlevel = models.DecimalField(db_column='ReorderLevel', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    datetimeretired = models.DateTimeField(db_column='DateTimeRetired')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblitemstoragelocations'


class Tbljournalvouchers(models.Model):
    journalvoucherid = models.BigAutoField(db_column='JournalVoucherID', primary_key=True)  # Field name made lowercase.
    departmentid = models.ForeignKey(Tbldepartments, models.DO_NOTHING, db_column='DepartmentID', blank=True, null=True)  # Field name made lowercase.
    sourcereference = models.CharField(db_column='SourceReference', max_length=50000)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50000)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=100, decimal_places=2)  # Field name made lowercase.
    isposted = models.SmallIntegerField(db_column='IsPosted')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    fiscalperiodid = models.ForeignKey(Tblfiscalperiods, models.DO_NOTHING, db_column='FiscalPeriodID')  # Field name made lowercase.
    postedbysysuid = models.IntegerField(db_column='PostedBySysUID', blank=True, null=True)  # Field name made lowercase.
    isautomatic = models.SmallIntegerField(db_column='IsAutomatic')  # Field name made lowercase.
    transactiondatetime = models.DateTimeField(db_column='TransactionDateTime')  # Field name made lowercase.
    isperiodclosingjournal = models.SmallIntegerField(db_column='IsPeriodClosingJournal')  # Field name made lowercase.
    reversingjournalvoucherid = models.ForeignKey('self', models.DO_NOTHING, db_column='ReversingJournalVoucherID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbljournalvouchers'


class Tblmedicalclinics(models.Model):
    medicalclinicid = models.BigAutoField(db_column='MedicalClinicID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    departmentid = models.ForeignKey(Tbldepartments, models.DO_NOTHING, db_column='DepartmentID')  # Field name made lowercase.
    isdefaultclinic = models.SmallIntegerField(db_column='IsDefaultClinic')  # Field name made lowercase.
    ishypertensionclinic = models.SmallIntegerField(db_column='IsHypertensionClinic')  # Field name made lowercase.
    isspecialclinic = models.SmallIntegerField(db_column='IsSpecialClinic')  # Field name made lowercase.
    icon = models.CharField(db_column='Icon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    appearonqueuepopup = models.SmallIntegerField(db_column='AppearOnQueuePopup')  # Field name made lowercase.
    servicetype = models.SmallIntegerField(db_column='ServiceType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmedicalclinics'
        unique_together = (('name', 'departmentid'),)


class Tblmedicalclinicvisitprocedures(models.Model):
    medicalclinicvisitprocedureid = models.BigAutoField(db_column='MedicalClinicVisitProcedureID', primary_key=True)  # Field name made lowercase.
    medicalclinicvisitid = models.ForeignKey('Tblmedicalclinicvisits', models.DO_NOTHING, db_column='MedicalClinicVisitID')  # Field name made lowercase.
    seenbysysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='SeenBySysUID')  # Field name made lowercase.
    procedureid = models.ForeignKey('Tblprocedures', models.DO_NOTHING, db_column='ProcedureID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmedicalclinicvisitprocedures'


class Tblmedicalclinicvisits(models.Model):
    medicalclinicvisitid = models.BigAutoField(db_column='MedicalClinicVisitID', primary_key=True)  # Field name made lowercase.
    seenbysysuid = models.IntegerField(db_column='SeenBySysUID')  # Field name made lowercase.
    visitid = models.ForeignKey('Tblvisits', models.DO_NOTHING, db_column='VisitID')  # Field name made lowercase.
    medicalclinicid = models.ForeignKey(Tblmedicalclinics, models.DO_NOTHING, db_column='MedicalClinicID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmedicalclinicvisits'


class Tblnationalitys(models.Model):
    nationalityid = models.BigAutoField(db_column='NationalityID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    countrycode = models.IntegerField(db_column='CountryCode', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblnationalitys'


class Tbloccupations(models.Model):
    occupationid = models.BigAutoField(db_column='OccupationID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbloccupations'


class Tblothertaxs(models.Model):
    othertaxid = models.BigAutoField(db_column='OtherTaxID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    perrate = models.DecimalField(db_column='PerRate', max_digits=100, decimal_places=2)  # Field name made lowercase.
    vatliabsubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='VATLiabSubAccountID')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblothertaxs'
        unique_together = (('name', 'companybranchid'),)


class Tblpaymentmodecategorys(models.Model):
    paymentmodecategoryid = models.BigAutoField(db_column='PaymentModeCategoryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpaymentmodecategorys'


class Tblpaymentmodes(models.Model):
    paymentmodeid = models.BigAutoField(db_column='PaymentModeID', primary_key=True)  # Field name made lowercase.
    paymentmodecategoryid = models.ForeignKey(Tblpaymentmodecategorys, models.DO_NOTHING, db_column='PaymentModeCategoryID')  # Field name made lowercase.
    subaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='SubAccountID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    isdefault = models.SmallIntegerField(db_column='IsDefault')  # Field name made lowercase.
    canbereceived = models.SmallIntegerField(db_column='CanBeReceived')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    api = models.SmallIntegerField(db_column='API')  # Field name made lowercase.
    paymentmodeselectionlevelid = models.ForeignKey('Tblpaymentmodeselectionlevels', models.DO_NOTHING, db_column='PaymentModeSelectionLevelID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpaymentmodes'
        unique_together = (('name', 'subaccountid'),)


class Tblpaymentmodeselectionlevels(models.Model):
    paymentmodeselectionlevelid = models.BigAutoField(db_column='PaymentModeSelectionLevelID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpaymentmodeselectionlevels'


class Tblprescriptionitems(models.Model):
    prescriptionitemid = models.BigAutoField(db_column='PrescriptionItemID', primary_key=True)  # Field name made lowercase.
    prescriptionid = models.ForeignKey('Tblprescriptions', models.DO_NOTHING, db_column='PrescriptionID')  # Field name made lowercase.
    inscription = models.CharField(db_column='Inscription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subscriptionitemstoragelocationid = models.ForeignKey(Tblitemstoragelocations, models.DO_NOTHING, db_column='SubscriptionItemStorageLocationID', blank=True, null=True)  # Field name made lowercase.
    transcription = models.CharField(db_column='Transcription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    quantitypertime = models.DecimalField(db_column='QuantityPerTime', max_digits=100, decimal_places=2)  # Field name made lowercase.
    frequencyperperiod = models.IntegerField(db_column='FrequencyPerPeriod')  # Field name made lowercase.
    periodin = models.SmallIntegerField(db_column='PeriodIn')  # Field name made lowercase.
    dosageduration = models.IntegerField(db_column='DosageDuration')  # Field name made lowercase.
    otherinstructions = models.CharField(db_column='OtherInstructions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unitofmeasureid = models.ForeignKey('Tblunitofmeasures', models.DO_NOTHING, db_column='UnitOfMeasureID', blank=True, null=True)  # Field name made lowercase.
    customerschemeid = models.ForeignKey(Tblcustomerschemes, models.DO_NOTHING, db_column='CustomerSchemeID')  # Field name made lowercase.
    customerbillitemid = models.ForeignKey(Tblcustomerbillitems, models.DO_NOTHING, db_column='CustomerBillItemID', blank=True, null=True)  # Field name made lowercase.
    dosageunit = models.CharField(db_column='DosageUnit', max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    hasbeenbilled = models.SmallIntegerField(db_column='HasBeenBilled')  # Field name made lowercase.
    isdischargeprescription = models.SmallIntegerField(db_column='IsDischargePrescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblprescriptionitems'


class Tblprescriptions(models.Model):
    prescriptionid = models.BigAutoField(db_column='PrescriptionID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    specialinstructions = models.CharField(db_column='SpecialInstructions', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    datetimeofprescription = models.DateTimeField(db_column='DateTimeOfPrescription')  # Field name made lowercase.
    clinician = models.CharField(db_column='Clinician', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblprescriptions'


class Tblprocedures(models.Model):
    procedureid = models.BigAutoField(db_column='ProcedureID', primary_key=True)  # Field name made lowercase.
    companybranchitemid = models.ForeignKey(Tblcompanybranchitems, models.DO_NOTHING, db_column='CompanyBranchItemID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblprocedures'
        unique_together = (('name', 'companybranchitemid'),)


class Tblschemecategorys(models.Model):
    schemecategoryid = models.BigAutoField(db_column='SchemeCategoryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblschemecategorys'


class Tblschemes(models.Model):
    schemeid = models.BigAutoField(db_column='SchemeID', primary_key=True)  # Field name made lowercase.
    schemecategoryid = models.ForeignKey(Tblschemecategorys, models.DO_NOTHING, db_column='SchemeCategoryID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    physicaladdress = models.CharField(db_column='PhysicalAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postaladdress = models.CharField(db_column='PostalAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    townid = models.ForeignKey('Tbltowns', models.DO_NOTHING, db_column='TownID', blank=True, null=True)  # Field name made lowercase.
    telephone1 = models.CharField(db_column='Telephone1', max_length=255)  # Field name made lowercase.
    telephone2 = models.CharField(db_column='Telephone2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currentbalance = models.DecimalField(db_column='CurrentBalance', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='CreditLimit', max_digits=100, decimal_places=2)  # Field name made lowercase.
    periodfromdatetime = models.DateTimeField(db_column='PeriodFromDateTime')  # Field name made lowercase.
    periodtodatetime = models.DateTimeField(db_column='PeriodToDateTime')  # Field name made lowercase.
    receivablesubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='ReceivableSubAccountID')  # Field name made lowercase.
    depositsubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='DepositSubAccountID', related_name='tblschemes_depositsubaccountid_set')  # Field name made lowercase.
    isdefault = models.SmallIntegerField(db_column='IsDefault')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    enforcecreditlimit = models.SmallIntegerField(db_column='EnforceCreditLimit')  # Field name made lowercase.
    enforcecreditlimitinpatient = models.SmallIntegerField(db_column='EnforceCreditLimitInpatient')  # Field name made lowercase.
    underwriterid = models.ForeignKey('Tblunderwriters', models.DO_NOTHING, db_column='UnderwriterID', blank=True, null=True)  # Field name made lowercase.
    isemployeescheme = models.SmallIntegerField(db_column='IsEmployeeScheme')  # Field name made lowercase.
    usessmartcard = models.SmallIntegerField(db_column='UsesSmartCard')  # Field name made lowercase.
    schemecode = models.CharField(db_column='SchemeCode', blank=True, null=True)  # Field name made lowercase.
    pinnumber = models.CharField(db_column='PinNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isshascheme = models.SmallIntegerField(db_column='IsShaScheme')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblschemes'
        unique_together = (('name', 'companybranchid'),)


class Tblstockchanges(models.Model):
    stockchangeid = models.BigAutoField(db_column='StockChangeID', primary_key=True)  # Field name made lowercase.
    storagelocationid = models.ForeignKey('Tblstoragelocations', models.DO_NOTHING, db_column='StorageLocationID')  # Field name made lowercase.
    companybranchitemid = models.ForeignKey(Tblcompanybranchitems, models.DO_NOTHING, db_column='CompanyBranchItemID')  # Field name made lowercase.
    changetypeid = models.SmallIntegerField(db_column='ChangeTypeID')  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantitychanged = models.DecimalField(db_column='QuantityChanged', max_digits=100, decimal_places=2)  # Field name made lowercase.
    isincrement = models.SmallIntegerField(db_column='IsIncrement')  # Field name made lowercase.
    datetimechanged = models.DateTimeField(db_column='DateTimeChanged')  # Field name made lowercase.
    sysuid = models.IntegerField(db_column='SysUID')  # Field name made lowercase.
    itemstoragelocationid = models.ForeignKey(Tblitemstoragelocations, models.DO_NOTHING, db_column='ItemStorageLocationID', blank=True, null=True)  # Field name made lowercase.
    totalcostofchange = models.DecimalField(db_column='TotalCostOfChange', max_digits=100, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblstockchanges'


class Tblstockreserves(models.Model):
    stockreserveid = models.BigAutoField(db_column='StockReserveID', primary_key=True)  # Field name made lowercase.
    itemstoragelocationid = models.ForeignKey(Tblitemstoragelocations, models.DO_NOTHING, db_column='ItemStorageLocationID')  # Field name made lowercase.
    quantityreserved = models.DecimalField(db_column='QuantityReserved', max_digits=100, decimal_places=2)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    datetimereserved = models.DateTimeField(db_column='DateTimeReserved')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    customerbillitemid = models.ForeignKey(Tblcustomerbillitems, models.DO_NOTHING, db_column='CustomerBillItemID', blank=True, null=True)  # Field name made lowercase.
    consumeditemid = models.ForeignKey(Tblconsumeditems, models.DO_NOTHING, db_column='ConsumedItemID', blank=True, null=True)  # Field name made lowercase.
    internalorderitemid = models.ForeignKey(Tblinternalorderitems, models.DO_NOTHING, db_column='InternalOrderItemID', blank=True, null=True)  # Field name made lowercase.
    interbranchorderitemid = models.ForeignKey(Tblinterbranchorderitems, models.DO_NOTHING, db_column='InterbranchOrderItemID', blank=True, null=True)  # Field name made lowercase.
    changedbysysuid = models.BigIntegerField(db_column='ChangedBySysUID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblstockreserves'


class Tblstocktakeitems(models.Model):
    stocktakeitemid = models.BigAutoField(db_column='StockTakeItemID', primary_key=True)  # Field name made lowercase.
    stocktakeid = models.ForeignKey('Tblstocktakes', models.DO_NOTHING, db_column='StockTakeID')  # Field name made lowercase.
    itemstoragelocationid = models.ForeignKey(Tblitemstoragelocations, models.DO_NOTHING, db_column='ItemStorageLocationID')  # Field name made lowercase.
    vattypeid = models.ForeignKey('Tblvattypes', models.DO_NOTHING, db_column='VATTypeID')  # Field name made lowercase.
    adjustedbysysuid = models.IntegerField(db_column='AdjustedBySysUID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unitcost = models.DecimalField(db_column='UnitCost', max_digits=100, decimal_places=2)  # Field name made lowercase.
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=100, decimal_places=2)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    unitofmeasureid = models.ForeignKey('Tblunitofmeasures', models.DO_NOTHING, db_column='UnitOfMeasureID', blank=True, null=True)  # Field name made lowercase.
    reorderlevel = models.DecimalField(db_column='ReorderLevel', max_digits=100, decimal_places=2)  # Field name made lowercase.
    packedquantityunit = models.CharField(db_column='PackedQuantityUnit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packedquantity = models.DecimalField(db_column='PackedQuantity', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    totalpackedquantity = models.DecimalField(db_column='TotalPackedQuantity', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hasbeenadjusted = models.SmallIntegerField(db_column='HasBeenAdjusted')  # Field name made lowercase.
    newquantity = models.DecimalField(db_column='NewQuantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    newtotalpackedquantity = models.DecimalField(db_column='NewTotalPackedQuantity', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    datetimeadjusted = models.DateTimeField(db_column='DateTimeAdjusted')  # Field name made lowercase.
    minunitprice = models.DecimalField(db_column='MinUnitPrice', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tradeunitprice = models.DecimalField(db_column='TradeUnitPrice', max_digits=100, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hasbeencommittedtostock = models.SmallIntegerField(db_column='HasBeenCommittedToStock')  # Field name made lowercase.
    committedbysysuid = models.IntegerField(db_column='CommittedBySysUID', blank=True, null=True)  # Field name made lowercase.
    assetsubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='AssetSubAccountID')  # Field name made lowercase.
    incomesubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='IncomeSubAccountID', related_name='tblstocktakeitems_incomesubaccountid_set')  # Field name made lowercase.
    expensessubaccountid = models.ForeignKey('Tblsubaccounts', models.DO_NOTHING, db_column='ExpensesSubAccountID', related_name='tblstocktakeitems_expensessubaccountid_set')  # Field name made lowercase.
    newunitcost = models.DecimalField(db_column='NewUnitCost', max_digits=100, decimal_places=2)  # Field name made lowercase.
    newcostchange = models.DecimalField(db_column='NewCostChange', max_digits=100, decimal_places=2)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='ExpiryDate')  # Field name made lowercase.
    newexpirydate = models.DateTimeField(db_column='NewExpiryDate')  # Field name made lowercase.
    newbatch = models.CharField(db_column='NewBatch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    newreorderlevel = models.DecimalField(db_column='NewReorderLevel', max_digits=100, decimal_places=2)  # Field name made lowercase.
    newname = models.CharField(db_column='NewName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    newvattypeid = models.ForeignKey('Tblvattypes', models.DO_NOTHING, db_column='NewVATTypeID', related_name='tblstocktakeitems_newvattypeid_set')  # Field name made lowercase.
    newunitofmeasureid = models.ForeignKey('Tblunitofmeasures', models.DO_NOTHING, db_column='NewUnitOfMeasureID', related_name='tblstocktakeitems_newunitofmeasureid_set', blank=True, null=True)  # Field name made lowercase.
    errormessage = models.CharField(db_column='ErrorMessage', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    erroroccured = models.SmallIntegerField(db_column='ErrorOccured')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblstocktakeitems'


class Tblstocktakes(models.Model):
    stocktakeid = models.BigAutoField(db_column='StockTakeID', primary_key=True)  # Field name made lowercase.
    createdbysysuid = models.IntegerField(db_column='CreatedBySysUID')  # Field name made lowercase.
    storagelocationid = models.ForeignKey('Tblstoragelocations', models.DO_NOTHING, db_column='StorageLocationID')  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated')  # Field name made lowercase.
    hasbeencommittedtostock = models.SmallIntegerField(db_column='HasBeenCommittedToStock', blank=True, null=True)  # Field name made lowercase.
    committedbysysuid = models.IntegerField(db_column='CommittedBySysUID', blank=True, null=True)  # Field name made lowercase.
    datetimecommittedtostock = models.DateTimeField(db_column='DateTimeCommittedToStock', blank=True, null=True)  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    isfrozen = models.SmallIntegerField(db_column='IsFrozen')  # Field name made lowercase.
    frozenbysysuid = models.ForeignKey('Tblsystemusers', models.DO_NOTHING, db_column='FrozenBySysUID', blank=True, null=True)  # Field name made lowercase.
    datetimefrozen = models.DateTimeField(db_column='DateTimeFrozen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblstocktakes'


class Tblstoragelocations(models.Model):
    storagelocationid = models.BigAutoField(db_column='StorageLocationID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isdefaultsellpoint = models.SmallIntegerField(db_column='IsDefaultSellPoint')  # Field name made lowercase.
    departmentid = models.ForeignKey(Tbldepartments, models.DO_NOTHING, db_column='DepartmentID')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    isopticalshop = models.SmallIntegerField(db_column='IsOpticalShop')  # Field name made lowercase.
    isdefaultinpatientstore = models.SmallIntegerField(db_column='IsDefaultInpatientStore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblstoragelocations'
        unique_together = (('name', 'departmentid'),)


class Tblsubaccounts(models.Model):
    subaccountid = models.BigAutoField(db_column='SubAccountID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    accountid = models.ForeignKey(Tblaccounts, models.DO_NOTHING, db_column='AccountID')  # Field name made lowercase.
    currentbalance = models.DecimalField(db_column='CurrentBalance', max_digits=100, decimal_places=2)  # Field name made lowercase.
    islocked = models.SmallIntegerField(db_column='IsLocked')  # Field name made lowercase.
    configurationtype = models.SmallIntegerField(db_column='ConfigurationType')  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsubaccounts'
        unique_together = (('name', 'accountid'),)


class Tblsystemusers(models.Model):
    systemuserid = models.BigAutoField(db_column='SystemUserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=1000)  # Field name made lowercase.
    accountisdisabled = models.SmallIntegerField(db_column='AccountIsDisabled')  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    othernames = models.CharField(db_column='OtherNames', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isemployee = models.SmallIntegerField(db_column='IsEmployee')  # Field name made lowercase.
    accountislocked = models.SmallIntegerField(db_column='AccountIsLocked')  # Field name made lowercase.
    lockoutdate = models.DateTimeField(db_column='LockoutDate', blank=True, null=True)  # Field name made lowercase.
    unlockdate = models.DateTimeField(db_column='UnlockDate', blank=True, null=True)  # Field name made lowercase.
    hasscheduledlockout = models.SmallIntegerField(db_column='HasScheduledLockout', blank=True, null=True)  # Field name made lowercase.
    accountisblocked = models.SmallIntegerField(db_column='AccountIsBlocked')  # Field name made lowercase.
    passwordhasbeenreset = models.SmallIntegerField(db_column='PasswordHasBeenReset', blank=True, null=True)  # Field name made lowercase.
    logonattempts = models.IntegerField(db_column='LogonAttempts', blank=True, null=True)  # Field name made lowercase.
    haslimitedattempts = models.SmallIntegerField(db_column='HasLimitedAttempts')  # Field name made lowercase.
    canaccessallbranches = models.SmallIntegerField(db_column='CanAccessAllBranches')  # Field name made lowercase.
    canloginfromanywhere = models.SmallIntegerField(db_column='CanLoginFromAnywhere')  # Field name made lowercase.
    issuperuser = models.SmallIntegerField(db_column='IsSuperUser')  # Field name made lowercase.
    accesscode = models.CharField(db_column='AccessCode', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    numberoflogins = models.IntegerField(db_column='NumberOfLogins', blank=True, null=True)  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated')  # Field name made lowercase.
    lastlogindate = models.DateTimeField(db_column='LastLoginDate')  # Field name made lowercase.
    issecondtiersuperuser = models.SmallIntegerField(db_column='IsSecondTierSuperUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblsystemusers'


class Tbltestcategorys(models.Model):
    testcategoryid = models.BigAutoField(db_column='TestCategoryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltestcategorys'


class Tbltests(models.Model):
    testid = models.BigAutoField(db_column='TestID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companybranchitemid = models.ForeignKey(Tblcompanybranchitems, models.DO_NOTHING, db_column='CompanyBranchItemID')  # Field name made lowercase.
    testcategoryid = models.ForeignKey(Tbltestcategorys, models.DO_NOTHING, db_column='TestCategoryID')  # Field name made lowercase.
    testspecimenid = models.ForeignKey('Tbltestspecimens', models.DO_NOTHING, db_column='TestSpecimenID')  # Field name made lowercase.
    ispanel = models.SmallIntegerField(db_column='IsPanel')  # Field name made lowercase.
    interpretation = models.CharField(db_column='Interpretation', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    equipment = models.CharField(db_column='Equipment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    limitations = models.CharField(db_column='Limitations', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    methodology = models.CharField(db_column='Methodology', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    machine = models.SmallIntegerField(db_column='Machine')  # Field name made lowercase.
    testcode = models.CharField(db_column='TestCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    printallreferencerangesonlabreport = models.SmallIntegerField(db_column='PrintAllReferenceRangesOnLabReport')  # Field name made lowercase.
    referenceranges = models.CharField(db_column='ReferenceRanges', max_length=20000, blank=True, null=True)  # Field name made lowercase.
    isactive = models.SmallIntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltests'
        unique_together = (('name', 'companybranchitemid'),)


class Tbltestspecimens(models.Model):
    testspecimenid = models.BigAutoField(db_column='TestSpecimenID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltestspecimens'


class Tbltheatrenotes(models.Model):
    theatrenoteid = models.BigAutoField(db_column='TheatreNoteID', primary_key=True)  # Field name made lowercase.
    medicalclinicvisitid = models.ForeignKey(Tblmedicalclinicvisits, models.DO_NOTHING, db_column='MedicalClinicVisitID')  # Field name made lowercase.
    datetimecreated = models.DateTimeField(db_column='DateTimeCreated')  # Field name made lowercase.
    surgeon = models.CharField(db_column='Surgeon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    asssurgeon = models.CharField(db_column='AssSurgeon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anaesthesist = models.CharField(db_column='Anaesthesist', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scrubnurse = models.CharField(db_column='ScrubNurse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    anaesthesia = models.CharField(db_column='Anaesthesia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    theatreoperationid = models.ForeignKey('Tbltheatreoperations', models.DO_NOTHING, db_column='TheatreOperationID')  # Field name made lowercase.
    diagnosisid = models.ForeignKey(Tbldiagnosiss, models.DO_NOTHING, db_column='DiagnosisID', blank=True, null=True)  # Field name made lowercase.
    incision = models.CharField(db_column='Incision', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    biopsyspecimen = models.CharField(db_column='BiopsySpecimen', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    theatreprocedure = models.CharField(db_column='TheatreProcedure', max_length=1000000, blank=True, null=True)  # Field name made lowercase.
    complications = models.CharField(db_column='Complications', max_length=1000000, blank=True, null=True)  # Field name made lowercase.
    estbloodloss = models.CharField(db_column='EstBloodLoss', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doctor = models.CharField(db_column='Doctor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sysuid = models.IntegerField(db_column='SysUID')  # Field name made lowercase.
    theatrecount = models.CharField(db_column='TheatreCount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hasbeencompleted = models.SmallIntegerField(db_column='HasBeenCompleted')  # Field name made lowercase.
    hasbeencancelled = models.SmallIntegerField(db_column='HasBeenCancelled')  # Field name made lowercase.
    cancelledbysysuid = models.ForeignKey(Tblsystemusers, models.DO_NOTHING, db_column='CancelledBySysUID', blank=True, null=True)  # Field name made lowercase.
    datetimecancelled = models.DateTimeField(db_column='DateTimeCancelled')  # Field name made lowercase.
    anaestheticnotes = models.CharField(db_column='AnaestheticNotes', max_length=1000000, blank=True, null=True)  # Field name made lowercase.
    specificoperation = models.CharField(db_column='SpecificOperation', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltheatrenotes'


class Tbltheatreoperations(models.Model):
    theatreoperationid = models.BigAutoField(db_column='TheatreOperationID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    companybranchitemid = models.ForeignKey(Tblcompanybranchitems, models.DO_NOTHING, db_column='CompanyBranchItemID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltheatreoperations'
        unique_together = (('name', 'companybranchitemid'),)


class Tbltowns(models.Model):
    townid = models.BigAutoField(db_column='TownID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbltowns'


class Tblunderwriters(models.Model):
    underwriterid = models.BigAutoField(db_column='UnderwriterID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblunderwriters'
        unique_together = (('name', 'companybranchid'),)


class Tblunitofmeasures(models.Model):
    unitofmeasureid = models.BigAutoField(db_column='UnitOfMeasureID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=255)  # Field name made lowercase.
    issmallestunit = models.SmallIntegerField(db_column='IsSmallestUnit')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=100, decimal_places=2)  # Field name made lowercase.
    isdiscrete = models.SmallIntegerField(db_column='IsDiscrete')  # Field name made lowercase.
    dosageunit = models.CharField(db_column='DosageUnit', max_length=255)  # Field name made lowercase.
    iscomputable = models.SmallIntegerField(db_column='IsComputable')  # Field name made lowercase.
    prescriptionverb = models.CharField(db_column='PrescriptionVerb', max_length=255)  # Field name made lowercase.
    measurementunit = models.SmallIntegerField(db_column='MeasurementUnit')  # Field name made lowercase.
    packagingunit = models.SmallIntegerField(db_column='PackagingUnit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblunitofmeasures'


class Tblvattypes(models.Model):
    vattypeid = models.BigAutoField(db_column='VATTypeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    perrate = models.DecimalField(db_column='PerRate', max_digits=100, decimal_places=2)  # Field name made lowercase.
    vatliabsubaccountid = models.ForeignKey(Tblsubaccounts, models.DO_NOTHING, db_column='VATLiabSubAccountID')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    etimstaxcode = models.CharField(db_column='ETimsTaxCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblvattypes'
        unique_together = (('name', 'companybranchid'),)


class Tblvisitrequestedexaminationitems(models.Model):
    visitrequestedexaminationitemid = models.BigAutoField(db_column='VisitRequestedExaminationItemID', primary_key=True)  # Field name made lowercase.
    visitrequestedexaminationid = models.ForeignKey('Tblvisitrequestedexaminations', models.DO_NOTHING, db_column='VisitRequestedExaminationID')  # Field name made lowercase.
    examinationid = models.ForeignKey(Tblexaminations, models.DO_NOTHING, db_column='ExaminationID')  # Field name made lowercase.
    isdone = models.SmallIntegerField(db_column='IsDone')  # Field name made lowercase.
    isinternal = models.SmallIntegerField(db_column='IsInternal')  # Field name made lowercase.
    datetimedone = models.DateTimeField(db_column='DateTimeDone', blank=True, null=True)  # Field name made lowercase.
    examiner = models.CharField(db_column='Examiner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    centre = models.CharField(db_column='Centre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    techniqueprocedure = models.CharField(db_column='TechniqueProcedure', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    findings = models.CharField(db_column='Findings', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    impression = models.CharField(db_column='Impression', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    reasonnotdone = models.CharField(db_column='ReasonNotDone', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    savedbysysuid = models.IntegerField(db_column='SavedBySysUID', blank=True, null=True)  # Field name made lowercase.
    radiologist = models.CharField(db_column='Radiologist', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblvisitrequestedexaminationitems'


class Tblvisitrequestedexaminations(models.Model):
    visitrequestedexaminationid = models.BigAutoField(db_column='VisitRequestedExaminationID', primary_key=True)  # Field name made lowercase.
    visitid = models.ForeignKey('Tblvisits', models.DO_NOTHING, db_column='VisitID')  # Field name made lowercase.
    datetimerequested = models.DateTimeField(db_column='DateTimeRequested')  # Field name made lowercase.
    requestedbysysuid = models.IntegerField(db_column='RequestedBySysUID')  # Field name made lowercase.
    isselfrequest = models.SmallIntegerField(db_column='IsSelfRequest')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblvisitrequestedexaminations'


class Tblvisitrequestedtestitems(models.Model):
    visitrequestedtestitemid = models.BigAutoField(db_column='VisitRequestedTestItemID', primary_key=True)  # Field name made lowercase.
    visitrequestedtestid = models.ForeignKey('Tblvisitrequestedtests', models.DO_NOTHING, db_column='VisitRequestedTestID')  # Field name made lowercase.
    testid = models.ForeignKey(Tbltests, models.DO_NOTHING, db_column='TestID')  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(db_column='History', max_length=100000, blank=True, null=True)  # Field name made lowercase.
    isreadystatus = models.SmallIntegerField(db_column='IsReadyStatus')  # Field name made lowercase.
    sampleid = models.CharField(db_column='SampleID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblvisitrequestedtestitems'


class Tblvisitrequestedtests(models.Model):
    visitrequestedtestid = models.BigAutoField(db_column='VisitRequestedTestID', primary_key=True)  # Field name made lowercase.
    visitid = models.ForeignKey('Tblvisits', models.DO_NOTHING, db_column='VisitID')  # Field name made lowercase.
    datetimerequested = models.DateTimeField(db_column='DateTimeRequested')  # Field name made lowercase.
    isoutpatient = models.SmallIntegerField(db_column='IsOutPatient')  # Field name made lowercase.
    isdone = models.SmallIntegerField(db_column='IsDone')  # Field name made lowercase.
    isinternal = models.SmallIntegerField(db_column='IsInternal')  # Field name made lowercase.
    datetimedone = models.DateTimeField(db_column='DateTimeDone', blank=True, null=True)  # Field name made lowercase.
    isselfrequest = models.SmallIntegerField(db_column='IsSelfRequest')  # Field name made lowercase.
    technologist = models.CharField(db_column='Technologist', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reasonnotdone = models.CharField(db_column='ReasonNotDone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    requestedbysysuid = models.IntegerField(db_column='RequestedBySysUID')  # Field name made lowercase.
    ispartiallydone = models.SmallIntegerField(db_column='IsPartiallyDone')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    referringdoctor = models.CharField(db_column='ReferringDoctor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isapproved = models.SmallIntegerField(db_column='IsApproved')  # Field name made lowercase.
    approvedbysysuid = models.ForeignKey(Tblsystemusers, models.DO_NOTHING, db_column='ApprovedBySysUID', blank=True, null=True)  # Field name made lowercase.
    datetimeapproved = models.DateTimeField(db_column='DateTimeApproved')  # Field name made lowercase.
    donebysysuid = models.ForeignKey(Tblsystemusers, models.DO_NOTHING, db_column='DoneBySysUID', related_name='tblvisitrequestedtests_donebysysuid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblvisitrequestedtests'


class Tblvisits(models.Model):
    visitid = models.BigAutoField(db_column='VisitID', primary_key=True)  # Field name made lowercase.
    datetimeofvisit = models.DateTimeField(db_column='DateTimeOfVisit')  # Field name made lowercase.
    companybranchid = models.ForeignKey(Tblcompanybranchs, models.DO_NOTHING, db_column='CompanyBranchID')  # Field name made lowercase.
    customerid = models.ForeignKey(Tblcustomers, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.
    createdbysysuid = models.IntegerField(db_column='CreatedBySysUID')  # Field name made lowercase.
    iswalkin = models.SmallIntegerField(db_column='IsWalkin')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isrevisit = models.SmallIntegerField(db_column='IsRevisit')  # Field name made lowercase.
    visitdefaultscheme = models.IntegerField(db_column='VisitDefaultScheme', blank=True, null=True)  # Field name made lowercase.
    smartsessionid = models.CharField(db_column='SmartSessionID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblvisits'
