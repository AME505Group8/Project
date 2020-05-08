# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Start.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.GUI_RsltFltPln import Ui_GUI_RsltFltPln
from GUI_Predict_Function import gui_predict_function

# Inputs lists
InputsMonth = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']
InputsTOD = ['', 'Dawn', 'Day', 'Dusk', 'Night']
InputsState = ['', 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN',
               'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
               'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI',
               'WV', 'WY']
InputsAirport = ['', '00C', '00M', '00OI', '01G', '02C', '04W', '05C', '06D', '06FA', '06N', '07F', '07FA', '08C',
                 '09J', '09LA', '09N', '09R', '0A9', '0B8', '0G6', '0IL1', '0LA7', '0M5', '0MSO', '0NC4', '0PS2',
                 '0Q4', '0Q5', '0S9', '0TX1', '0V6', '11A', '12N', '12V', '12Y', '14G', '15TE', '17N', '17XS', '18GA',
                 '1A9', '1AZ0', '1B1', '1B2', '1B9', '1C5', '1C9', '1F0', '1F5', '1G0', '1G3', '1G4', '1H0', '1I5',
                 '1I9', '1J9', '1KY4', '1KY5', '1M9', '1MO3', '1N7', '1O2', '1O3', '1O6', '1Q5', '1R8', '1S6  ', '1T8',
                 '1TE6', '1U7', '1V0', '20E', '20N', '20V', '21D', '23S', '24LA', '24VA', '26A', '26N', '28J', '28NJ',
                 '2A0', '2A5', '2B7', '2F0', '2G1', '2G2', '2G4', '2I0', '2IS', '2J9', '2LA0', '2LS0', '2M8', '2MO1',
                 '2MU1', '2N8', '2O1', '2R2', '2R4', '2R9', '2S1', '2W2', '2W6', '2WA1', '32S', '33N', '33R', '33V  ',
                 '34VA', '35D', '35ME', '36U', '37KY', '38TE', '39N', '3A2', '3B0', '3CK', '3CL0', '3CM', '3D2', '3EX',
                 '3F7', '3FD1', '3FU', '3G3', '3G9', '3GV', '3I2', '3J7', '3LF', '3M7', '3M9', '3MI2', '3MY', '3NJ6',
                 '3O1', '3R7', '3R9', '3S7', '3S8', '3T0', '3T3', '3T5', '3T7', '3TR', '3W2', '3W3', '3W9', '3XS2',
                 '41AZ', '41C', '42B', '42J', '42PN', '44G', '44N', '45FA', '45LA', '46MO', '46N', '48A', '48D', '49B',
                 '4A2', '4A7', '4AC', '4B0', '4B8', '4D0', '4D1', '4G1  ', '4G4', '4G7', '4I3', '4I9', '4IA2', '4KY7',
                 '4LA4', '4LA6', '4M1', '4M3', '4M7', '4M9', '4MS6', '4N1', '4O4', '4R5', '4R9', '4TN4', '4V0', '4V1',
                 '4WI0', '4WI9', '50F', '50R', '50VA', '53OI', '54F', '54J', '56S', '57AZ', '57B', '57D', '57Y',
                 '58KY', '59B', '5A1', '5B2', '5B6', '5C1', '5G0', '5G8', '5KE', '5KY3', '5LA4', '5T6', '5TS9', '5TX0',
                 '5TX7', '5W5', '6.00E+05', '60F', '61FL', '61S', '63C', '64OG', '65G', '66R', '67S', '6A1', '6A2',
                 '6B6', '6B9', '6D6', '6D9', '6FL0', '6G5', '6J0', '6K5', '6L4', '6M2', '6N5', '6OI8', '6PA6', '6S8',
                 '70N', '70S', '71J', '72F', '72VA', '74S', '74TX', '75MO', '77MI', '77S', '79J', '79KY', '7A5', '7B2',
                 '7D5', '7D6', '7F7', '7FL6', '7G8', '7K5', '7LS1', '7LS3', '7LS4', '7M3', '7M4', '7M6', '7MI3', '7S3',
                 '7S5', '7V2', '80D', '81OK', '820H', '82J', '82TX', '82WN', '83D', '87I', '87MO', '87Y', '88R', '89D',
                 '8A1', '8A4', '8A6', '8B8', '8D4', '8D7', '8LA1', '8S1', '8S4', '8TN7', '8U2', '8W2', '90WA', '98D',
                 '99Y', '9A7', '9B1', '9D1', '9D2', '9D4', '9G0', '9G2', '9N1', '9TA7', '9WI8', '9Z4', 'A29', 'A32',
                 'A63', 'AK28', 'AZ75', 'BKPR', 'C09', 'C20', 'C29', 'C35', 'C43', 'C47', 'C56', 'C62', 'C65', 'C66',
                 'C81', 'C83', 'C91', 'CA51', 'CA52', 'CA92', 'CKU', 'CL33', 'CO49', 'CO80', 'CO90', 'CT60', 'CYAG',
                 'CYBR', 'CYEG', 'CYET', 'CYGW', 'CYHM', 'CYHU', 'CYHZ', 'CYJT', 'CYKF', 'CYKZ', 'CYLJ', 'CYMX',
                 'CYOW', 'CYQA', 'CYQB', 'CYQG', 'CYQR', 'CYQT', 'CYQX', 'CYSB', 'CYSN', 'CYUL', 'CYVR', 'CYWG',
                 'CYWH', 'CYXE', 'CYXU', 'CYYC', 'CYYJ', 'CYYR', 'CYYT', 'CYYZ', 'D00', 'D09', 'D25', 'D38', 'D60',
                 'D68', 'D73', 'D80', 'D95', 'DAAG', 'DIAP', 'DM2', 'DNMM', 'E11', 'E16', 'E27', 'E38', 'E45', 'E63',
                 'E91', 'EBBR', 'EBLG', 'EBOS', 'EDDF', 'EDDK', 'EDDL', 'EDDM', 'EDDN', 'EDDP', 'EDDS', 'EDDT', 'EDFH',
                 'EFHK', 'EGAA', 'EGBB', 'EGBE', 'EGBJ', 'EGBP', 'EGCC', 'EGGD', 'EGGW', 'EGHI', 'EGJA', 'EGJB',
                 'EGJJ', 'EGKA', 'EGKB', 'EGKK', 'EGLF', 'EGLK', 'EGLL', 'EGLS', 'EGMD', 'EGNJ', 'EGNX', 'EGPE',
                 'EGPH', 'EGPK', 'EGSS', 'EGSX', 'EGTO', 'EGUL', 'EHAM', 'EIDW', 'EINN', 'EKCH', 'ELLX', 'ENFB',
                 'EPWA', 'ESMS', 'ESSA', 'ETAR', 'F10', 'F22', 'F31', 'F35', 'F44', 'F45', 'F62', 'F70', 'F72', 'F87',
                 'F99', 'FA40', 'FA61', 'FA81', 'FACT', 'FAOR', 'FEFB', 'FL17', 'FL59', 'FWKI', 'G05', 'GA04', 'GA20',
                 'GMME', 'GOOY', 'H2O', 'H34', 'H68', 'H71', 'H75', 'HECA', 'HI01', 'HKHO', 'HKJK', 'I18', 'I19',
                 'I23', 'I39', 'I40', 'I41', 'I62', 'I64', 'I66', 'I68', 'I69', 'I95', 'IA24', 'IA66', 'IA82', 'JY17',
                 'K15', 'K18', 'K38', 'K44D', 'K68', 'K81', 'KAAA', 'KAAF', 'KAAO', 'KABE', 'KABI', 'KABQ', 'KABR',
                 'KABY', 'KACB', 'KACK', 'KACT', 'KACV', 'KACY', 'KADC', 'KADF', 'KADG', 'KADH', 'KADM', 'KADS',
                 'KADW', 'KAEG', 'KAEL', 'KAEX', 'KAFJ', 'KAFP', 'KAFW', 'KAGC', 'KAGO', 'KAGS', 'KAHN', 'KAIA',
                 'KAID', 'KAIK', 'KAIT', 'KAIZ', 'KAKR', 'KALB', 'KALN', 'KALO', 'KALS', 'KALW', 'KALX', 'KAMA',
                 'KAMN', 'KAMW', 'KANB', 'KAND', 'KANE', 'KANJ', 'KANP', 'KANQ', 'KAOH', 'KAOO', 'KAPA', 'KAPC',
                 'KAPF', 'KAPN', 'KAPT', 'KAQO', 'KAQR', 'KARA', 'KARB', 'KARG', 'KARM', 'KARR', 'KART', 'KARV',
                 'KARW', 'KASD', 'KASE', 'KASG', 'KASH', 'KASL', 'KAST', 'KASW', 'KASX', 'KATL', 'KATW', 'KATY',
                 'KAUG', 'KAUM', 'KAUN', 'KAUO', 'KAUS', 'KAUW', 'KAVC', 'KAVK', 'KAVL', 'KAVP', 'KAVQ', 'KAWM',
                 'KAWO', 'KAXH', 'KAXN', 'KAXS', 'KAZO', 'KB10', 'KB19', 'KBAD', 'KBAF', 'KBAK', 'KBAX', 'KBAZ',
                 'KBBG', 'KBCB', 'KBCT', 'KBDE', 'KBDG', 'KBDH', 'KBDL', 'KBDN', 'KBDR', 'KBDU', 'KBEC', 'KBED',
                 'KBEH', 'KBFD', 'KBFF', 'KBFI', 'KBFL', 'KBFM', 'KBFR', 'KBGE', 'KBGM', 'KBGR', 'KBHB', 'KBHM',
                 'KBID', 'KBIH', 'KBIJ', 'KBIL', 'KBIS', 'KBIV', 'KBJC', 'KBJI', 'KBJJ', 'KBKF', 'KBKL', 'KBKN',
                 'KBKS', 'KBKV', 'KBKW', 'KBKX', 'KBLI', 'KBLM', 'KBLV', 'KBMC', 'KBMG', 'KBMI', 'KBML', 'KBMQ',
                 'KBNA', 'KBNO', 'KBOI', 'KBOS', 'KBOW', 'KBPG', 'KBPI', 'KBPT', 'KBQK', 'KBRD', 'KBRL', 'KBRO',
                 'KBST', 'KBTA', 'KBTF', 'KBTL', 'KBTM', 'KBTN', 'KBTR', 'KBTV', 'KBUB', 'KBUF', 'KBUR', 'KBUY',
                 'KBVI', 'KBVO', 'KBVS', 'KBVU', 'KBVY', 'KBWC', 'KBWD', 'KBWG', 'KBWI', 'KBXA', 'KBXK', 'KBXM',
                 'KBYH', 'KBYI', 'KBZN', 'KCAD', 'KCAE', 'KCAK', 'KCAO', 'KCBE', 'KCBF', 'KCBK', 'KCCO', 'KCCR',
                 'KCDC', 'KCDH', 'KCDI', 'KCDK', 'KCDR', 'KCDW', 'KCEC', 'KCEF', 'KCEU', 'KCEV', 'KCEW', 'KCEZ',
                 'KCFD', 'KCFJ', 'KCGC', 'KCGE', 'KCGF', 'KCGI', 'KCGS', 'KCGX', 'KCGZ', 'KCHA', 'KCHD', 'KCHN',
                 'KCHO', 'KCHS', 'KCHT', 'KCIC', 'KCID', 'KCIU', 'KCJR', 'KCKB', 'KCKN', 'KCKP', 'KCKV', 'KCKZ',
                 'KCLE', 'KCLI', 'KCLL', 'KCLM', 'KCLS', 'KCLT', 'KCMA', 'KCMD', 'KCMH ', 'KCMI', 'KCMR', 'KCMX',
                 'KCNH', 'KCNI', 'KCNM', 'KCNO', 'KCNW', 'KCNY', 'KCOD', 'KCOE', 'KCOF', 'KCOI', 'KCOS', 'KCOU',
                 'KCPK ', 'KCPM', 'KCPR', 'KCPS', 'KCPT', 'KCQF', 'KCQX', 'KCRE', 'KCRG', 'KCRP', 'KCRQ', 'KCRS',
                 'KCRW', 'KCRZ', 'KCSG', 'KCSM', 'KCSV', 'KCTB', 'KCTJ', 'KCTY', 'KCUB', 'KCUT', 'KCVC', 'KCVG',
                 'KCVH', 'KCVN', 'KCVO', 'KCWA', 'KCWC', 'KCWF', 'KCWS', 'KCWV', 'KCXO', 'KCXP', 'KCXW', 'KCXY',
                 'KCYO', 'KCYS', 'KCYW', 'KDAB', 'KDAG', 'KDAL', 'KDAN', 'KDAW', 'KDAY', 'KDBN', 'KDBQ', 'KDCA',
                 'KDCU', 'KDDC', 'KDEC', 'KDED', 'KDEN', 'KDEN*', 'KDET', 'KDEW', 'KDFW', 'KDGW', 'KDHN', 'KDIJ',
                 'KDIK', 'KDKB', 'KDKK', 'KDKX', 'KDLH', 'KDLL', 'KDLO', 'KDLS', 'KDLZ', 'KDMA', 'KDMN', 'KDMW',
                 'KDNL', 'KDNS', 'KDNV', 'KDOV', 'KDPA', 'KDQH', 'KDRI', 'KDRM', 'KDRO', 'KDRT', 'KDSM', 'KDTL',
                 'KDTN', 'KDTO', 'KDTS', 'KDTW', 'KDUA', 'KDUC', 'KDUG', 'KDUH', 'KDUJ', 'KDVL', 'KDVO', 'KDVT',
                 'KDWA', 'KDWH', 'KDWU', 'KDWX', 'KDXE', 'KDXR', 'KDYA', 'KDYL', 'KDYR', 'KDYT', 'KDZB', 'KEAR',
                 'KEAT', 'KEAU', 'KEBG', 'KECG', 'KECP', 'KEDC', 'KEDE', 'KEDU', 'KEDW', 'KEEN', 'KEFD', 'KEGE',
                 'KEGV', 'KEHA', 'KEHR', 'KEKA', 'KEKM', 'KEKO', 'KEKX', 'KEKY', 'KELM', 'KELP', 'KELY', 'KEMT',
                 'KENV', 'KENW', 'KEOK', 'KEOP', 'KEOS', 'KEPH', 'KEQA', 'KEQY', 'KERI', 'KERR', 'KERV', 'KESC',
                 'KESF', 'KESN', 'KEST', 'KETB', 'KEUF', 'KEUG', 'KEUL', 'KEVB', 'KEVV', 'KEVW', 'KEVY', 'KEWB',
                 'KEWK', 'KEWN', 'KEWR', 'KEXX', 'KEYE', 'KEYW', 'KEZF', 'KEZM', 'KEZS', 'KFAM', 'KFAR', 'KFAT',
                 'KFAY', 'KFCH', 'KFCI', 'KFCM', 'KFDK', 'KFDR', 'KFDW', 'KFDY', 'KFES', 'KFET ', 'KFFA', 'KFFC',
                 'KFFM', 'KFFO', 'KFFZ', 'KFHB', 'KFHR', 'KFHU', 'KFIN', 'KFIT', 'KFKL', 'KFLD', 'KFLG', 'KFLL',
                 'KFLO', 'KFLP', 'KFLV', 'KFLY', 'KFME', 'KFMH', 'KFMN', 'KFMY', 'KFNB', 'KFNL', 'KFNT', 'KFOD',
                 'KFOE', 'KFOK', 'KFOT', 'KFPK', 'KFPR', 'KFRG', 'KFRH', 'KFRM', 'KFRR', 'KFSD', 'KFSM', 'KFSU',
                 'KFTG', 'KFTW', 'KFTY', 'KFUL', 'KFVX', 'KFWA', 'KFWB', 'KFWQ', 'KFWS', 'KFXE', 'KFYJ', 'KFYV',
                 'KFZI ', 'KFZY', 'KGAD', 'KGAF', 'KGAI', 'KGAO', 'KGAS', 'KGBD', 'KGBG', 'KGBR', 'KGCC', 'KGCD',
                 'KGCK', 'KGCM', 'KGCN', 'KGDB', 'KGDV', 'KGED', 'KGEG', 'KGEU', 'KGEV', 'KGFK', 'KGFL', 'KGGE',
                 'KGGG', 'KGGW', 'KGHG', 'KGHM', 'KGHW', 'KGIC', 'KGIF', 'KGJT', 'KGKJ', 'KGKY', 'KGLD', 'KGLE',
                 'KGLH', 'KGLR', 'KGLS', 'KGLW', 'KGMU', 'KGNF', 'KGNT', 'KGNV', 'KGOK', 'KGON', 'KGOO', 'KGPH',
                 'KGPI', 'KGPM', 'KGPT', 'KGPZ', 'KGRB', 'KGRD', 'KGRI', 'KGRK', 'KGRR', 'KGSH', 'KGSO', 'KGSP',
                 'KGTB', 'KGTE', 'KGTF', 'KGTR', 'KGTU', 'KGUC', 'KGUS', 'KGUY', 'KGVL', 'KGVQ', 'KGVT', 'KGVW',
                 'KGWB', 'KGWO', 'KGWR', 'KGXY', 'KGYH', 'KGYI', 'KGYR', 'KGYY', 'KGZS', 'KHAF', 'KHAI', 'KHAO',
                 'KHBG', 'KHBV', 'KHBZ', 'KHCD', 'KHDC', 'KHDN', 'KHDO', 'KHEF', 'KHEG', 'KHEZ', 'KHFD', 'KHFJ',
                 'KHFY', 'KHGR', 'KHHR', 'KHHW', 'KHIB', 'KHIE', 'KHIF', 'KHIG', 'KHII', 'KHIO', 'KHKA', 'KHKS',
                 'KHKY', 'KHLG', 'KHLN', 'KHMT', 'KHNB', 'KHND', 'KHOB', 'KHOC', 'KHON', 'KHOT', 'KHOU', 'KHPN',
                 'KHQM', 'KHQU', 'KHQZ', 'KHRL', 'KHRO', 'KHRT', 'KHSA', 'KHSD', 'KHST', 'KHSV', 'KHTO', 'KHTS',
                 'KHUA', 'KHUF', 'KHUM', 'KHUT', 'KHVN', 'KHVR', 'KHWD', 'KHWO', 'KHWY', 'KHXD', 'KHYA', 'KHYI',
                 'KHYR', 'KHYS', 'KHYW', 'KHZY', 'KIAB', 'KIAD', 'KIAG', 'KIAH', 'KICL', 'KICT', 'KIDA', 'KIDI ',
                 'KIDP', 'KIFA', 'KIFP', 'KIGM', 'KIGQ', 'KIGX', 'KIJD', 'KIJX', 'KIKG', 'KIKK', 'KIKV', 'KIKW',
                 'KILE', 'KILG', 'KILL', 'KILM', 'KILN', 'KIMM', 'KIMS', 'KIMT', 'KIND', 'KINF', 'KINL', 'KINT',
                 'KIOW', 'KIPL', 'KIPT', 'KIRK', 'KIRS', 'KISM', 'KISN', 'KISO', 'KISP', 'KISW', 'KISZ', 'KITH',
                 'KITR', 'KIWA', 'KIWD', 'KIWH', 'KIWS', 'KIXD', 'KIZG', 'KJAC', 'KJAN', 'KJAS', 'KJAX', 'KJBR',
                 'KJEF', 'KJFK', 'KJGG', 'KJHW', 'KJKA', 'KJKL', 'KJLN', 'KJMR', 'KJMS', 'KJNX', 'KJQF', 'KJRB',
                 'KJSO', 'KJST', 'KJSY', 'KJVL', 'KJVW', 'KJVY', 'KJWN', 'KJWY', 'KJXI', 'KJXN', 'KJYL', 'KJYO',
                 'KJZI', 'KJZP', 'KKLS', 'KLAA', 'KLAF', 'KLAL', 'KLAN', 'KLAR', 'KLAS', 'KLAW', 'KLAX', 'KLBB',
                 'KLBE', 'KLBF', 'KLBL', 'KLBO', 'KLBX', 'KLCG', 'KLCH', 'KLCI', 'KLCK', 'KLCQ', 'KLDJ', 'KLDM',
                 'KLEB', 'KLEE', 'KLEW', 'KLEX', 'KLFI', 'KLFK', 'KLFT', 'KLGA', 'KLGB', 'KLGC', 'KLGD', 'KLGU',
                 'KLHM', 'KLHQ', 'KLHX', 'KLIT', 'KLKR', 'KLKU', 'KLLQ', 'KLLR', 'KLMO', 'KLMT', 'KLNA', 'KLNC',
                 'KLND', 'KLNK', 'KLNL', 'KLNN', 'KLNQ', 'KLNR ', 'KLNS', 'KLOM', 'KLOT', 'KLOU', 'KLOZ', 'KLPR',
                 'KLQK', 'KLRD', 'KLRO', 'KLRU', 'KLRY', 'KLSE', 'KLSN', 'KLUG', 'KLUK', 'KLUL', 'KLVJ', 'KLVK',
                 'KLVM', 'KLVN', 'KLVS ', 'KLWB', 'KLWC', 'KLWD', 'KLWM', 'KLWS', 'KLXT', 'KLXV', 'KLYH', 'KLZD',
                 'KLZU', 'KMAC', 'KMAF', 'KMAI', 'KMBL', 'KMBO', 'KMBS', 'KMBT', 'KMCB', 'KMCC', 'KMCD', 'KMCE',
                 'KMCF', 'KMCI', 'KMCK', 'KMCN', 'KMCO', 'KMCW', 'KMCX', 'KMDD', 'KMDH', 'KMDQ', 'KMDT', 'KMDW',
                 'KMEI', 'KMEM', 'KMER', 'KMEZ', 'KMFD', 'KMFE', 'KMFI', 'KMFR', 'KMGC', 'KMGE', 'KMGJ', 'KMGM',
                 'KMGN', 'KMGR', 'KMGW', 'KMGY', 'KMHE', 'KMHK', 'KMHL', 'KMHR', 'KMHT', 'KMHV', 'KMIA', 'KMIC',
                 'KMIE', 'KMIV', 'KMIW', 'KMJX', 'KMKC', 'KMKE', 'KMKG', 'KMKL', 'KMKN', 'KMKO', 'KMKT', 'KMKY',
                 'KMLB', 'KMLC', 'KMLE', 'KMLI', 'KMLJ', 'KMLS', 'KMLU', 'KMMH', 'KMMI', 'KMMK', 'KMML', 'KMMU',
                 'KMMV', 'KMNE', 'KMNM', 'KMNN', 'KMOB', 'KMOD', 'KMOP', 'KMOT', 'KMPO', 'KMPV', 'KMQB', 'KMQI',
                 'KMQJ', 'KMQS', 'KMQT', 'KMQY', 'KMRB', 'KMRC', 'KMRH', 'KMRJ', 'KMRY', 'KMSL', 'KMSN', 'KMSO',
                 'KMSP', 'KMSS', 'KMSV', 'KMSY', 'KMTC', 'KMTH', 'KMTJ', 'KMTN', 'KMTO', 'KMTP', 'KMTV', 'KMTW',
                 'KMUI', 'KMUT', 'KMVC', 'KMVN', 'KMVY', 'KMWA', 'KMWC', 'KMWH', 'KMWK', 'KMWL', 'KMWO', 'KMYF',
                 'KMYL', 'KMYR', 'KMYV', 'KMZJ', 'KNBC', 'KNEW', 'KNFW', 'KNGP', 'KNGU', 'KNHK', 'KNIP', 'KNKT',
                 'KNQA', 'KNTU', 'KNUC', 'KNUQ', 'KNVD', 'KNYG', 'KNYL', 'KNZY', 'KOAJ', 'KOAK', 'KOAR', 'KOBE',
                 'KOBI', 'KOCF', 'KOCW', 'KODO', 'KOEO', 'KOFK', 'KOFP', 'KOGD', 'KOGS', 'KOIC', 'KOJC', 'KOKB',
                 'KOKC', 'KOKH', 'KOKK', 'KOKM', 'KOKV', 'KOLF', 'KOLM', 'KOLS', 'KOLU', 'KOLV', 'KOLY', 'KOMA',
                 'KOMH', 'KOMK', 'KOMN', 'KONA', 'KONL', 'KONO', 'KONP', 'KONT', 'KONX', 'KONZ', 'KOPF', 'KOPL',
                 'KOPN', 'KOQN', 'KOQU', 'KORB', 'KORD', 'KORF', 'KORG', 'KORH', 'KORK', 'KORL', 'KORS', 'KOSH',
                 'KOSU', 'KOTG', 'KOTH', 'KOTM', 'KOUN', 'KOWA', 'KOWB', 'KOWD', 'KOXB', 'KOXC', 'KOXD', 'KOXR',
                 'KOXV', 'KOZS', 'KOZW', 'KPAE', 'KPAH', 'KPAN', 'KPAO', 'KPBG', 'KPBH', 'KPBI', 'KPBX', 'KPCM',
                 'KPCW', 'KPCZ', 'KPDK', 'KPDT', 'KPDX', 'KPEA', 'KPEO', 'KPEQ', 'KPFN', 'KPGA', 'KPGD', 'KPGV',
                 'KPHF', 'KPHK', 'KPHL', 'KPHN', 'KPHP', 'KPHX', 'KPIA', 'KPIB', 'KPIE', 'KPIH', 'KPIR', 'KPIT',
                 'KPJC', 'KPJY', 'KPKB', 'KPKD', 'KPLB', 'KPLD', 'KPLK', 'KPLN', 'KPLU', 'KPMD', 'KPMH', 'KPMP',
                 'KPMU', 'KPNC', 'KPNE', 'KPNM', 'KPNS', 'KPOC', 'KPOF', 'KPOU', 'KPOV', 'KPPF', 'KPPQ', 'KPQI',
                 'KPRB', 'KPRC', 'KPRG ', 'KPRX', 'KPSC', 'KPSF', 'KPSM', 'KPSN', 'KPSO', 'KPSP', 'KPSX', 'KPTB',
                 'KPTD', 'KPTK', 'KPTN', 'KPTS', 'KPTV', 'KPTW', 'KPUB', 'KPUJ', 'KPUW', 'KPVC', 'KPVD', 'KPVF',
                 'KPVG', 'KPVU', 'KPVW', 'KPWA', 'KPWC', 'KPWG', 'KPWK', 'KPWM', 'KPWT', 'KPYM', 'KRAC', 'KRAL',
                 'KRAP', 'KRBD', 'KRBG', 'KRBL', 'KRBO', 'KRCM', 'KRCR', 'KRDD', 'KRDG', 'KRDM', 'KRDU', 'KRED',
                 'KREI', 'KRFD', 'KRFG', 'KRFI', 'KRGK', 'KRHI', 'KRHV', 'KRIC', 'KRID', 'KRIL', 'KRIU', 'KRIV',
                 'KRIW', 'KRKD', 'KRKP', 'KRKR', 'KRKS', 'KRLD', 'KRME', 'KRMG', 'KRMN', 'KRMY', 'KRNH', 'KRNM',
                 'KRNO', 'KRNP', 'KRNT', 'KRNV', 'KROA', 'KROC', 'KROG', 'KROS', 'KROW', 'KROX', 'KRPB', 'KRPD',
                 'KRPH', 'KRQB', 'KRQO', 'KRRL', 'KRRQ', 'KRRT', 'KRSN', 'KRST', 'KRSW', 'KRTS', 'KRUE', 'KRUQ',
                 'KRUT', 'KRVS', 'KRWF', 'KRWI', 'KRWL', 'KRWN', 'KRYN', 'KRYV', 'KRYW', 'KRYY', 'KRZL', 'KSAC',
                 'KSAF', 'KSAN', 'KSAR', 'KSAT', 'KSAV', 'KSAW', 'KSBA', 'KSBD', 'KSBM', 'KSBN', 'KSBP', 'KSBS',
                 'KSBY', 'KSCH', 'KSCK', 'KSDF', 'KSDL', 'KSDM', 'KSDY', 'KSEA', 'KSEE', 'KSEF', 'KSEP', 'KSER',
                 'KSET', 'KSEZ', 'KSFB', 'KSFF', 'KSFM', 'KSFO', 'KSFQ', 'KSFZ', 'KSGF', 'KSGH', 'KSGJ', 'KSGR',
                 'KSGS', 'KSGT', 'KSGU', 'KSHD', 'KSHR', 'KSHV', 'KSIF', 'KSIK', 'KSJC', 'KSJS', 'KSJT', 'KSJX',
                 'KSKF', 'KSKI', 'KSKY', 'KSLC', 'KSLE', 'KSLH', 'KSLI', 'KSLK', 'KSLN', 'KSLR', 'KSMD', 'KSME',
                 'KSMF', 'KSMO', 'KSMS', 'KSMX', 'KSNA', 'KSNC', 'KSNK', 'KSNL', 'KSNS', 'KSNY', 'KSOA', 'KSOP',
                 'KSOW', 'KSPA', 'KSPB', 'KSPG', 'KSPH', 'KSPI', 'KSPK', 'KSPS', 'KSPW', 'KSPX', 'KSPZ', 'KSQL',
                 'KSRB', 'KSRC', 'KSRE', 'KSRQ', 'KSRR', 'KSSF', 'KSSI', 'KSSQ', 'KSTC', 'KSTE', 'KSTF', 'KSTJ',
                 'KSTL', 'KSTP', 'KSTS', 'KSUA', 'KSUE', 'KSUN', 'KSUS', 'KSUT', 'KSUU', 'KSUW', 'KSUX', 'KSUZ',
                 'KSVC', 'KSVE', 'KSVH', 'KSWF', 'KSWO', 'KSXL', 'KSXU', 'KSYM', 'KSYR', 'KSZT', 'KSZY', 'KTAN',
                 'KTBN', 'KTBR', 'KTCC', 'KTCL', 'KTCM', 'KTCY', 'KTDF', 'KTDW', 'KTDZ', 'KTEB', 'KTEL', 'KTEX',
                 'KTGI', 'KTHA', 'KTHV', 'KTIP', 'KTIW', 'KTIX', 'KTKC', 'KTKI', 'KTKV', 'KTKX', 'KTLH', 'KTLR',
                 'KTMB', 'KTME', 'KTNT', 'KTOA', 'KTOI', 'KTOL', 'KTOP', 'KTPA', 'KTPF', 'KTPH', 'KTPL', 'KTQK',
                 'KTRI', 'KTRK', 'KTRM', 'KTRX', 'KTSO', 'KTSP', 'KTTA', 'KTTD', 'KTTF', 'KTTN', 'KTTS', 'KTUL',
                 'KTUP', 'KTUS', 'KTVC', 'KTVF', 'KTVI', 'KTVL', 'KTVR', 'KTVY', 'KTWF', 'KTXK', 'KTYQ', 'KTYR',
                 'KTYS', 'KTZR', 'KUAO', 'KUBX', 'KUCA', 'KUCP', 'KUCY', 'KUDD', 'KUDG', 'KUES', 'KUGN', 'KUIN',
                 'KUIZ', 'KUKF', 'KUKI', 'KULM ', 'KUMP', 'KUNI', 'KUNO', 'KUNV', 'KUOS', 'KUTA', 'KUTS', 'KUUU',
                 'KUUV', 'KUVA', 'KUXL', 'KUYF', 'KUZA', 'KVAD', 'KVAY', 'KVBG', 'KVBT', 'KVCB', 'KVCT', 'KVCV',
                 'KVDF', 'KVEL', 'KVER', 'KVGC', 'KVGT', 'KVIH', 'KVIS', 'KVJI', 'KVKX', 'KVLD', 'KVLL', 'KVMR',
                 'KVNC', 'KVNY', 'KVOK', 'KVPS', 'KVPZ', 'KVQQ', 'KVRB', 'KVSF', 'KVTA', 'KVTI', 'KVTN', 'KVUJ',
                 'KVUO', 'KWAL', 'KWAY', 'KWDG', 'KWDR', 'KWHP', 'KWJF', 'KWLD', 'KWLW', 'KWRI', 'KWRL', 'KWST',
                 'KWVI', 'KWVL', 'KWWD', 'KWWR', 'KWYS', 'KXBP', 'KXLL', 'KXNA', 'KXNX ', 'KXSA', 'KYIP', 'KYKM',
                 'KYKN', 'KYNG', 'KZER', 'KZPH', 'KZZV', 'L26', 'L35', 'L38', 'L45', 'L52', 'L66', 'L83', 'LA09',
                 'LA28', 'LBBG', 'LEBL', 'LEMD', 'LEMG', 'LERT', 'LEVC', 'LEZG', 'LFBO', 'LFCO', 'LFMN', 'LFPG',
                 'LFPO', 'LFSB', 'LGAV', 'LGKM', 'LGTS', 'LHBP', 'LICZ', 'LIMC', 'LIPA', 'LIPH', 'LIPZ', 'LIRA',
                 'LIRF', 'LIRN', 'LIRP', 'LKPR', 'LL10', 'LL22', 'LLBG', 'LOWW', 'LPAZ', 'LPLA', 'LPPT', 'LQTZ',
                 'LRCK', 'LROP', 'LS99', 'LSGG', 'LSZH', 'LTAG', 'LTBA', 'LTBJ', 'M05', 'M17', 'M19', 'M20', 'M21',
                 'M22', 'M31', 'M33', 'M34', 'M37', 'M46', 'M48', 'M54', 'M59', 'M83', 'MA39', 'MBPV', 'MD24', 'MD71',
                 'MD99', 'MDJB', 'MDLR', 'MDPC', 'MDPP', 'MDSD', 'MDST', 'ME19', 'ME79', 'MGGT', 'MHLM', 'MHTG',
                 'MI32', 'MKJP', 'MKJS', 'MMAA', 'MMAN', 'MMAS', 'MMBT', 'MMCU', 'MMCZ', 'MMGL', 'MMGM', 'MMHO',
                 'MMLM', 'MMLO', 'MMMG', 'MMMX', 'MMMY', 'MMMZ', 'MMPB', 'MMPR', 'MMQT', 'MMSD', 'MMSP', 'MMTC',
                 'MMTO', 'MMUN', 'MMVR', 'MMZC', 'MMZH', 'MN56', 'MNMG', 'MO09', 'MO28', 'MO3', 'MO63', 'MO91', 'MPHO',
                 'MPTO', 'MRLB', 'MROC', 'MSLP', 'MTPP', 'MU02', 'MUHA', 'MUSC', 'MUVR', 'MWCR', 'MYAK', 'MYAM',
                 'MYAT', 'MYBS', 'MYEF ', 'MYEH', 'MYGF', 'MYNN', 'MYSM', 'MZBZ', 'N03', 'N07', 'N14', 'N40', 'N51',
                 'N57', 'N66', 'N72', 'N81', 'N87', 'NC14', 'NC30', 'NC92', 'NE41', 'NFFN', 'NFNA', 'NH16', 'NSTU',
                 'NTAA', 'NV57', 'NV74', 'NY0', 'NY22', 'NZAA', 'O03', 'O07', 'O22', 'O41', 'O43', 'O60', 'O69', 'O6A',
                 'O85', 'O86', 'O88', 'OAIX', 'OAKB', 'OBBI', 'OEAH', 'OEDR', 'OEHL', 'OEJF', 'OERY', 'OETN', 'OG30',
                 'OH77', 'OI65', 'OKBK', 'OMDB', 'OPRN', 'OR81', 'OTBD', 'P08', 'P10', 'P19', 'P72', 'PABE', 'PABG',
                 'PABR', 'PABV', 'PACD', 'PACK', 'PACM', 'PACV', 'PADK', 'PADL', 'PADQ', 'PADU', 'PADY', 'PAED',
                 'PAEE', 'PAEM', 'PAEN', 'PAEW', 'PAFA', 'PAFE', 'PAGA', 'PAGM', 'PAGS', 'PAGY', 'PAHL', 'PAHO',
                 'PAJN', 'PAKD', 'PAKI', 'PAKN', 'PAKT', 'PAKU', 'PAKW', 'PAKY', 'PALH', 'PAML', 'PAMR', 'PANC',
                 'PANI', 'PAOH', 'PAOM', 'PAOO', 'PAOT', 'PAPB', 'PAPG', 'PAPH', 'PAQT', 'PASC', 'PASD', 'PASI',
                 'PASK', 'PASN', 'PASO', 'PASV', 'PASX', 'PASY', 'PATK', 'PAUM', 'PAUT', 'PAVD', 'PAWD', 'PAWG',
                 'PAYA', 'PCUW', 'PFCL', 'PFKA', 'PFNO', 'PGM', 'PGRO', 'PGSN', 'PGUM', 'PGWT', 'PHDH', 'PHHN', 'PHJH',
                 'PHJR', 'PHKO', 'PHLI', 'PHLU', 'PHMK', 'PHMU', 'PHNL', 'PHNY', 'PHOG', 'PHPA', 'PHTO', 'PJON',
                 'PKMJ', 'PKWA', 'PLPA', 'PMDY', 'PTPN', 'PTRO', 'PTYA', 'PVT', 'PWAK', 'R47', 'RCKH', 'RCTP', 'RIGG',
                 'RJAA', 'RJBB', 'RJCC', 'RJNA', 'RJOI', 'RJTQ', 'RJTT', 'RJTY', 'RKJK', 'RKPK', 'RKSI', 'RKSS',
                 'RMPC', 'RODN', 'RPLB', 'RPLC', 'RPLL', 'RPVM', 'S03', 'S19', 'S21', 'S24', 'S31', 'S32', 'S40',
                 'S43', 'S48', 'S50', 'S72', 'S83', 'SABE', 'SAEZ', 'SBBR', 'SBCF', 'SBEG', 'SBGL', 'SBGR', 'SBKP',
                 'SBPA', 'SBRF', 'SCEL', 'SEGU', 'SEMT', 'SEQM', 'SEQU', 'SGES', 'SKBO', 'SKBQ', 'SKCG', 'SKCL',
                 'SKRG', 'SKSP', 'SLLP', 'SLVR', 'SMJP', 'SPIM', 'SUMU', 'SVMC', 'SVMI', 'SVVA', 'T03', 'T05', 'T40',
                 'T67', 'T82', 'TAPA', 'TBPB', 'TDPD', 'TGPY', 'TIST', 'TISX', 'TJBQ', 'TJIG', 'TJMZ', 'TJPS', 'TJSJ',
                 'TKPK', 'TLPC', 'TLPL', 'TN85', 'TN98', 'TNCA', 'TNCC', 'TNCM', 'TQPF', 'TRPG', 'TTPP', 'TUPJ',
                 'TX17', 'TX2', 'TX33', 'TXKF', 'TYE', 'U02', 'U10', 'U14', 'U42', 'U68', 'U70', 'UAAA', 'UBBB',
                 'UCFM', 'UHHH', 'UT11 ', 'UT25', 'UT83', 'UUDD', 'UUEE', 'VABB', 'VHHH', 'VI22', 'VIDP', 'VOBG',
                 'VTBD', 'VTBS', 'VVNB', 'VVTS', 'W00', 'W04', 'W13', 'W22', 'W24', 'W28', 'W29', 'W32', 'W39', 'W40',
                 'W48', 'W50', 'W78', 'W91', 'W96', 'WA09', 'WA18', 'WIII', 'WMKK', 'WMKN', 'WMKP', 'WS35', 'WSSL',
                 'WSSS', 'WV27', 'WV42', 'X06', 'X13', 'X14', 'X21', 'X23', 'X26', 'X35', 'X39', 'X46', 'X50', 'X51',
                 'X58', 'X59', 'X60', 'XA14', 'XS40', 'XS73', 'XS90', 'Y19', 'Y31', 'Y50', 'Y55', 'Y65', 'Y70', 'Y96',
                 'YBBN', 'YBHM', 'YMML', 'YSSY', 'Z41', 'ZBAA', 'ZBTJ', 'ZGGG', 'ZGSZ', 'ZHCC', 'ZSPD', 'ZSQD', 'ZUUU']
InputsEType = ['', 'Piston', 'Turbojet', 'Turboprop', 'Turbofan', 'Turboshaft']
InputsENo = ['', '1', '2', '3', '4']
InputsPhase = ['', 'Approach', 'Arrival', 'Climb', 'Departure', 'Descent', 'En Route', 'Landing Roll', 'Local',
               'Parked', 'Take-off Run', 'Taxi']


class Ui_GUI_Start(object):

    def __init__(self):
        # Window object definition
        self.GUI_RsltFltPln = QtWidgets.QMainWindow()
        self.GUI_RsltFltPln_Ui = Ui_GUI_RsltFltPln()
        self.GUI_RsltFltPln_Ui.setupUi(self.GUI_RsltFltPln)

        # Window button actions (Start window button actions near bottom of this script)
        self.GUI_RsltFltPln_Ui.QuitButton.clicked.connect(self.GoToExitScript)
        self.GUI_RsltFltPln_Ui.StartButton.clicked.connect(self.GoToStart)
        self.GUI_RsltFltPln_Ui.PrintButton.clicked.connect(self.PrintRsltFltPln)

    # Page transition and exit functions
    def GoToStart(self):
        GUI_Start.show()
        self.GUI_RsltFltPln.hide()

    def GoToRsltFltPln(self):

        # Ensure all parameters are selected before attempting to run function
        if self.FltPlnMonthBox.currentIndex() != 0 and self.FltPlnTODBox.currentIndex() != 0 and \
                self.FltPlnStateBox.currentIndex() != 0 and self.FltPlnAirportBox.currentIndex() != 0 and \
                self.FltPlnETypeBox.currentIndex() != 0 and self.FltPlnENoBox.currentIndex() != 0 and \
                self.FltPlnPhaseBox.currentIndex() != 0:

            # Populate all inputs onto the results screen
            self.GUI_RsltFltPln_Ui.FltPlnMonthOut.setText(InputsMonth[self.FltPlnMonthBox.currentIndex()])
            self.GUI_RsltFltPln_Ui.FltPlnTODOut.setText(InputsTOD[self.FltPlnTODBox.currentIndex()])
            self.GUI_RsltFltPln_Ui.FltPlnStateOut.setText(InputsState[self.FltPlnStateBox.currentIndex()])
            self.GUI_RsltFltPln_Ui.FltPlnAirportOut.setText(InputsAirport[self.FltPlnAirportBox.currentIndex()])
            self.GUI_RsltFltPln_Ui.FltPlnETypeOut.setText(InputsEType[self.FltPlnETypeBox.currentIndex()])
            self.GUI_RsltFltPln_Ui.FltPlnENoOut.setText(InputsENo[self.FltPlnENoBox.currentIndex()])
            self.GUI_RsltFltPln_Ui.FltPlnPhaseOut.setText(InputsPhase[self.FltPlnPhaseBox.currentIndex()])

            # Assign simple variable names to each of the selected inputs
            month = self.FltPlnMonthBox.currentIndex()
            time_of_day = InputsTOD[self.FltPlnTODBox.currentIndex()]
            state = InputsState[self.FltPlnStateBox.currentIndex()]
            airport_id = InputsAirport[self.FltPlnAirportBox.currentIndex()]
            engine_type = InputsEType[self.FltPlnETypeBox.currentIndex()]
            number_of_engines = InputsENo[self.FltPlnENoBox.currentIndex()]
            phase_of_flight = InputsPhase[self.FltPlnPhaseBox.currentIndex()]

            # Calls function, names, and separates its outputs
            prediction_name = gui_predict_function(state, month, time_of_day, airport_id, engine_type, number_of_engines, phase_of_flight)[0]
            aircraft_list = gui_predict_function(state, month, time_of_day, airport_id, engine_type, number_of_engines, phase_of_flight)[1]

            # Populate all outputs onto the results screen
            self.GUI_RsltFltPln_Ui.FltPlnOutput.setText(prediction_name)

            if len(aircraft_list) > 0:
                self.GUI_RsltFltPln_Ui.FltPlnACOut1.setText(aircraft_list[0])
            else:
                self.GUI_RsltFltPln_Ui.FltPlnACOut1.setText('NONE')

            if len(aircraft_list) > 1:
                self.GUI_RsltFltPln_Ui.FltPlnACOut2.setText(aircraft_list[1])
            else:
                self.GUI_RsltFltPln_Ui.FltPlnACOut2.setText('NONE')

            if len(aircraft_list) > 2:
                self.GUI_RsltFltPln_Ui.FltPlnACOut3.setText(aircraft_list[2])
            else:
                self.GUI_RsltFltPln_Ui.FltPlnACOut3.setText('NONE')

            if len(aircraft_list) > 3:
                self.GUI_RsltFltPln_Ui.FltPlnACOut4.setText(aircraft_list[3])
            else:
                self.GUI_RsltFltPln_Ui.FltPlnACOut4.setText('NONE')

            if len(aircraft_list) > 4:
                self.GUI_RsltFltPln_Ui.FltPlnACOut5.setText(aircraft_list[4])
            else:
                self.GUI_RsltFltPln_Ui.FltPlnACOut5.setText('NONE')

            GUI_Start.hide()
            self.GUI_RsltFltPln.show()

    def GoToExitScript(self):
        sys.exit()

    # Auto-generated code
    def setupUi(self, GUI_Start):
        GUI_Start.setObjectName("GUI_Start")
        GUI_Start.resize(800, 600)
        GUI_Start.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(8)
        GUI_Start.setFont(font)
        GUI_Start.setStyleSheet("background-color: rgb(255, 255, 255);")
        GUI_Start.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(GUI_Start)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TitleBlock = QtWidgets.QFrame(self.centralwidget)
        self.TitleBlock.setMaximumSize(QtCore.QSize(16777215, 100))
        self.TitleBlock.setStyleSheet("background-color: rgb(51, 58, 62);")
        self.TitleBlock.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TitleBlock.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TitleBlock.setObjectName("TitleBlock")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.TitleBlock)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.TitleBlock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(571, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Assets/GUI_StartScreenGraphic.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.TitleBlock)
        self.label_5.setMinimumSize(QtCore.QSize(218, 0))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(51, 58, 62);")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.TitleBlock)
        self.label_6.setMinimumSize(QtCore.QSize(218, 0))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(51, 58, 62);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.TitleBlock)
        self.MainContent = QtWidgets.QFrame(self.centralwidget)
        self.MainContent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainContent.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainContent.setLineWidth(0)
        self.MainContent.setObjectName("MainContent")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainContent)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.MainContent)
        self.frame.setStyleSheet("background-color: rgb(161, 172, 178);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(51, 58, 62);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setLineWidth(1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.FltPlnMonthBox = QtWidgets.QComboBox(self.frame)
        self.FltPlnMonthBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnMonthBox.setFont(font)
        self.FltPlnMonthBox.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnMonthBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FltPlnMonthBox.setObjectName("FltPlnMonthBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.FltPlnMonthBox)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.FltPlnStateBox = QtWidgets.QComboBox(self.frame)
        self.FltPlnStateBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnStateBox.setFont(font)
        self.FltPlnStateBox.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnStateBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FltPlnStateBox.setObjectName("FltPlnStateBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.FltPlnStateBox)
        self.label_9 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.FltPlnAirportBox = QtWidgets.QComboBox(self.frame)
        self.FltPlnAirportBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnAirportBox.setFont(font)
        self.FltPlnAirportBox.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnAirportBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FltPlnAirportBox.setObjectName("FltPlnAirportBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.FltPlnAirportBox)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.FltPlnETypeBox = QtWidgets.QComboBox(self.frame)
        self.FltPlnETypeBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnETypeBox.setFont(font)
        self.FltPlnETypeBox.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnETypeBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FltPlnETypeBox.setObjectName("FltPlnETypeBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.FltPlnETypeBox)
        self.label_11 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.FltPlnENoBox = QtWidgets.QComboBox(self.frame)
        self.FltPlnENoBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnENoBox.setFont(font)
        self.FltPlnENoBox.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnENoBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FltPlnENoBox.setObjectName("FltPlnENoBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.FltPlnENoBox)
        self.label_12 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.FltPlnPhaseBox = QtWidgets.QComboBox(self.frame)
        self.FltPlnPhaseBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnPhaseBox.setFont(font)
        self.FltPlnPhaseBox.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnPhaseBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FltPlnPhaseBox.setObjectName("FltPlnPhaseBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.FltPlnPhaseBox)
        self.label_16 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.FltPlnTODBox = QtWidgets.QComboBox(self.frame)
        self.FltPlnTODBox.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnTODBox.setFont(font)
        self.FltPlnTODBox.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnTODBox.setObjectName("FltPlnTODBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.FltPlnTODBox)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.RsltFltPlnButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.RsltFltPlnButton.setFont(font)
        self.RsltFltPlnButton.setToolTipDuration(0)
        self.RsltFltPlnButton.setStyleSheet("background-color: rgb(101, 117, 125);\n"
"color: rgb(255, 255, 255);")
        self.RsltFltPlnButton.setObjectName("RsltFltPlnButton")
        self.horizontalLayout_4.addWidget(self.RsltFltPlnButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.MainContent)
        self.frame_2.setStyleSheet("background-color: rgb(161, 172, 178);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setMinimumSize(QtCore.QSize(0, 30))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(51, 58, 62);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSpacing(5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.FltPlnParam1Box = QtWidgets.QComboBox(self.frame_2)
        self.FltPlnParam1Box.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnParam1Box.setFont(font)
        self.FltPlnParam1Box.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnParam1Box.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FltPlnParam1Box.setObjectName("FltPlnParam1Box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.FltPlnParam1Box)
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.FltPlnParam2Box = QtWidgets.QComboBox(self.frame_2)
        self.FltPlnParam2Box.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.FltPlnParam2Box.setFont(font)
        self.FltPlnParam2Box.setStyleSheet("background-color: rgb(223, 227, 229);")
        self.FltPlnParam2Box.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.FltPlnParam2Box.setObjectName("FltPlnParam2Box")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.FltPlnParam2Box)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.RsltFunc2Button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.RsltFunc2Button.setFont(font)
        self.RsltFunc2Button.setToolTipDuration(0)
        self.RsltFunc2Button.setStyleSheet("background-color: rgb(101, 117, 125);\n"
"color: rgb(255, 255, 255);")
        self.RsltFunc2Button.setObjectName("RsltFunc2Button")
        self.horizontalLayout_5.addWidget(self.RsltFunc2Button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_5.addWidget(self.MainContent)
        self.ButtonBar = QtWidgets.QFrame(self.centralwidget)
        self.ButtonBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ButtonBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ButtonBar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ButtonBar.setLineWidth(0)
        self.ButtonBar.setObjectName("ButtonBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ButtonBar)
        self.horizontalLayout_3.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.QuitButton = QtWidgets.QPushButton(self.ButtonBar)
        self.QuitButton.setMinimumSize(QtCore.QSize(100, 50))
        self.QuitButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(12)
        self.QuitButton.setFont(font)
        self.QuitButton.setStyleSheet("background-color: rgb(101, 117, 125);\n"
"color: rgb(255, 255, 255);")
        self.QuitButton.setObjectName("QuitButton")
        self.horizontalLayout_3.addWidget(self.QuitButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_5.addWidget(self.ButtonBar)
        self.MainContent.raise_()
        self.TitleBlock.raise_()
        self.ButtonBar.raise_()
        GUI_Start.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GUI_Start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        GUI_Start.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GUI_Start)
        self.statusbar.setObjectName("statusbar")
        GUI_Start.setStatusBar(self.statusbar)

        self.retranslateUi(GUI_Start)
        QtCore.QMetaObject.connectSlotsByName(GUI_Start)

        #Populate combo boxes
        self.FltPlnMonthBox.addItems(InputsMonth)
        self.FltPlnTODBox.addItems(InputsTOD)
        self.FltPlnStateBox.addItems(InputsState)
        self.FltPlnAirportBox.addItems(InputsAirport)
        self.FltPlnETypeBox.addItems(InputsEType)
        self.FltPlnENoBox.addItems(InputsENo)
        self.FltPlnPhaseBox.addItems(InputsPhase)

    def retranslateUi(self, GUI_Start):
        _translate = QtCore.QCoreApplication.translate
        GUI_Start.setWindowTitle(_translate("GUI_Start", "MainWindow"))
        self.label_5.setText(_translate("GUI_Start", "Bird Strike Analysis"))
        self.label_6.setText(_translate("GUI_Start", "AME505 Group 8"))
        self.label_4.setText(_translate("GUI_Start", "Flight Planning"))
        self.label_2.setText(_translate("GUI_Start", "Returns the aircraft class and the highest risk aircraft for the given parameters provided below."))
        self.label_7.setText(_translate("GUI_Start", "Month"))
        self.label_8.setText(_translate("GUI_Start", "State"))
        self.label_9.setText(_translate("GUI_Start", "Airport ID"))
        self.label_10.setText(_translate("GUI_Start", "Engine Type"))
        self.label_11.setText(_translate("GUI_Start", "Number of Engines"))
        self.label_12.setText(_translate("GUI_Start", "Phase of Flight"))
        self.label_16.setText(_translate("GUI_Start", "Time of Day"))
        self.RsltFltPlnButton.setText(_translate("GUI_Start", "Submit"))
        self.label_13.setText(_translate("GUI_Start", "Function 2 Title"))
        self.label_3.setText(_translate("GUI_Start", "Placeholder function 2 description text"))
        self.label_14.setText(_translate("GUI_Start", "Param1"))
        self.label_15.setText(_translate("GUI_Start", "Param2"))
        self.RsltFunc2Button.setText(_translate("GUI_Start", "Submit"))
        self.QuitButton.setText(_translate("GUI_Start", "Quit"))

        # Start Window Button Actions
        self.RsltFltPlnButton.clicked.connect(self.GoToRsltFltPln)
        self.QuitButton.clicked.connect(self.GoToExitScript)

    # Result printing functions
    def PrintRsltFltPln(self):
        print('Flight planning print button successful')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI_Start = QtWidgets.QMainWindow()
    ui = Ui_GUI_Start()
    ui.setupUi(GUI_Start)
    GUI_Start.show()
    sys.exit(app.exec_())
