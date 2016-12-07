#!/usr/bin/python

import sys
sys.path.append('ref/pipelines')
import kang
from snpdb.models import snpdb
import gzip 
'''
class snpdb(models.Model):
     cardname   = models.CharField(max_length=20)
     chromosome = models.CharField(max_length=20)
     position   = models.IntegerField(default=0)
     reference  = models.CharField(max_length=5)
     var_a      = models.CharField(max_length=20)
     var_t      = models.CharField(max_length=20)
     var_g      = models.CharField(max_length=20)
     var_c      = models.CharField(max_length=20)
'''

vcffile    = '11PM37_samtools.raw.vcf.gz'
samplename = '11PM37'

for line in gzip.open(vcffile):
    if line[0] == '#':
        continue
        cell = line.strip().split('\t')
        # Pepper1.55ch01  9889    .       G       T       14.2    .       DP=5;VDB=4.640000e-02;RPB=5.314005e-01;AF1=0.5;AC1=1;DP4=2,1,2,0;MQ=40;FQ=16.6;PV4=1,1,1,1      GT:PL:DP:GQ     0/1:44,0,53:5:46
        sChr  = cell[0]
        intPos  = int(cell[1])
        refBase = cell[3] 
        varBase = cell[4]
        fQual   = float(cell[5])
        info    = cell[7]
        dicInfo = kang.infoparse(info)
        if varBase.upper() == 'A':
            obj, created = Person.objects.get_or_create(cardname='%s_%d'%(sChr,intPos))
            if created:
                obj.update(chromosome=sChr, position=intPos, reference=refBase, var_a=samplename)
            else:
                obj.update(var_a=samplename)
        elif varBase.upper() == 'T':
            obj, created = Person.objects.get_or_create(cardname='%s_%d'%(sChr,intPos))
            if created:
                obj.update(chromosome=sChr, position=intPos, reference=refBase, var_a=samplename)
            else:
                obj.update(var_a=samplename)
        elif varBase.upper() == 'G':
            obj, created = Person.objects.get_or_create(cardname='%s_%d'%(sChr,intPos))
            if created:
                obj.update(chromosome=sChr, position=intPos, reference=refBase, var_a=samplename)
            else:
                obj.update(var_a=samplename)
        elif varBase.upper() == 'C':
            obj, created = Person.objects.get_or_create(cardname='%s_%d'%(sChr,intPos))
            if created:
                obj.update(chromosome=sChr, position=intPos, reference=refBase, var_a=samplename)
            else:
                obj.update(var_a=samplename)
        obj.publish()



        
            
            
        
