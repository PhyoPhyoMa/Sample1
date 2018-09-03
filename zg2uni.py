# -*- coding: utf-8 -*-
import re


def replace(input):

	output = input

	output = output.replace(u'\u106A', u'\u1009')
	output = re.sub(u'\u1025(?=[\u1039\u102C])', u'\u1009', output)#nya lay-24
	output = re.sub(u'[\u103D\u1087]', u'\u103E',output)#hahtoe
	output = re.sub(u'\u103C', u'\u103D',output)#waswe
	output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]',u'\u103C',output)#yayit
	output = re.sub(u'[\u103A\u107D]',u'\u103B',output)#yapint
	output = re.sub(u'[\u106B]',u'\u100A',output)#nya
	output = re.sub(u'[\u108F]',u'\u1014',output)#na
	output = re.sub(u'\u1097', u'\u100B',output)#tatalinjade
	output = re.sub(u'\u1092', u'\u100C',output)#htawonbae
	output = re.sub(u'\u1090', u'\u101B',output)#yakaut
	output = re.sub(u'\u1033', u'\u102F',output)#ta_chaung_ngin
	output = re.sub(u'\u1034', u'\u1030',output)#2chaung_ngin
	output = re.sub(u'\u1086', u'\u103F',output)#tagyi
	output = re.sub(u'\u104E', u'\u104E\u1004\u103A\u1038',output)#laguang
	output = re.sub(u'\u1039', u'\u103A',output)#nga_tat
	output = re.sub(u'[\u1037\u1094\u1095]', u'\u1037',output)#aut_myit
	output = re.sub(u'\u1086', u'\u103F',output)#tagyi
	output = re.sub(u'\u1039', u'\u103A',output)#athat
	output = re.sub(u'\u105A', u'\u102B\u103A',output)#yay_cha_athat
	output = re.sub(u'\u108A', u'\u103D\u103E',output)#waswe_hahtoe
	output = re.sub(u'\u1088', u'\u103E\u102F',output)#hahtoe_1chaung
	output = re.sub(u'\u1089', u'\u103E\u1030',output)#hahtoe_2chaung
	output = re.sub(u'\u104E', u'\u104E\u1004\u103A\u1038',output)#la_guang

	return output

def visual2logical(input):
	output = input
	#place
	output = re.sub(u'((?:\u1031)?)((?:\u103C)?)([\u1000-\u1021])((?:\u103D)?)((?:\u103B)?)((?:\u103E)?)((?:\u102C)?)', u"\\3\\2\\5\\4\\6\\1\\7",output);
	return output

def decompose(input):
	output = input
	#pa_sint
	output = re.sub(u'\u1060', u'\u1039\u1000',output)#kagyi
	output = re.sub(u'\u1061', u'\u1039\u1001',output)#ka_kway
	output = re.sub(u'\u1062', u'\u1039\u1002',output)#ga_nge
	output = re.sub(u'\u1063', u'\u1039\u1003',output)#gagyi
	output = re.sub(u'\u1065', u'\u1039\u1005',output)#sa_lone
	output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006',output)#sa_lane
	output = re.sub(u'\u1068', u'\u1039\u1007',output)#za_gwe
	output = re.sub(u'\u1069', u'\u1039\u1008',output)#za_myin_zwe
	output = re.sub(u'\u106C', u'\u1039\u100B',output)#tatalinjade
	output = re.sub(u'\u106D', u'\u1039\u100C',output)#htawonbae
	output = re.sub(u'\u106E', u'\u100D\u1039\u100D',output)#dayinkaut
	output = re.sub(u'\u106F', u'\u100E\u1039\u100D',output)#dayinmot
	output = re.sub(u'\u1070', u'\u1039\u100F',output)#nagyi
	output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010',output)#da_won_bu
	output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011',output)#hta_sin_htoo
	output = re.sub(u'\u1075', u'\u1039\u1012',output)#da_dwe
	output = re.sub(u'\u1076', u'\u1039\u1013',output)#da_ot_chite
	output = re.sub(u'\u1077', u'\u1039\u1014',output)#na
	output = re.sub(u'\u1078', u'\u1039\u1015',output)#pa_south
	output = re.sub(u'\u1079', u'\u1039\u1016',output)#fa_ot_htoke
	output = re.sub(u'\u107A', u'\u1039\u1017',output)#ba_lat_chite
	output = re.sub(u'[\u107B\u1093]', u'\u1039\u1018',output)#ba_gone
	output = re.sub(u'\u107C', u'\u1039\u1019',output)#ma
	output = re.sub(u'\u1085', u'\u1039\u101C',output)#la
	#ngr_sint
	output = re.sub(u'([\u1000-\u1021])\u1064', u'\u1064\\1',output)
	output = re.sub(u'\u1064', u'\u1004\u103A\u1039',output)
	output = re.sub(u'([\u1000-\u1021])\u108b', u'\u1064\\1\u102d', output)#with lone_gyi_tin
	output = re.sub(u'([\u1000-\u1021])\u108c', u'\u1064\\1\u102e', output)#with lone_gyi_tin_san_khat
	output = re.sub(u'([\u1000-\u1021])\u108d', u'\u1064\\1\u1036', output)#with ta_ta_tin
	output = re.sub(u'\u108e', u'\u102d\u1036', output)#lone_gyi_tin_ta_ta_tin
	return output

def convert(input):
	output = input
	output = replace(output)
	output = decompose(output)
	output = visual2logical(output)
	return output
