import tkinter as tk
from tkinter import ttk
from kiteconnect import KiteConnect
import threading
import time
from PIL import Image, ImageTk
import random

# API credentials
api_key=""
api_secret=""
request_token = ""
access_token = ""  # Replace with your access token

# Create a Kite Connect instance
kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

# Create a list of instrument tokens you are subscribed to
subscribed_instruments = ['NSE:RELIANCE','NSE:TATASTEEL','NSE:TCS', 'NSE:HDFCBANK', 'NSE:ICICIBANK', 'NSE:HINDUNILVR','NSE:INFY','NSE:ITC','NSE:SBIN', 'NSE:BHARTIARTL', 'NSE:KOTAKBANK', 'NSE:BAJFINANCE','NSE:LICI','NSE:LT','NSE:HCLTECH','NSE:ASIANPAINT','NSE:AXISBANK','NSE:MARUTI','NSE:SUNPHARMA','NSE:TITAN','NSE:DMART','NSE:ULTRACEMCO','NSE:BAJAJFINSV','NSE:WIPRO','NSE:ADANIENT','NSE:ONGC','NSE:NTPC','NSE:JSWSTEEL','NSE:POWERGRID','NSE:M&M','NSE:LTIM','NSE:TATAMOTORS','NSE:ADANIGREEN','NSE:ADANIPORTS','NSE:COALINDIA','NSE:TATASTEEL','NSE:HINDZINC','NSE:PIDILITIND','NSE:SIEMENS','NSE:ADANITRANS','NSE:SBILIFE','NSE:IOC','NSE:BAJAJ-AUTO','NSE:GRASIM','NSE:TECHM','NSE:HDFCLIFE','NSE:BRITANNIA','NSE:VEDL','NSE:GODREJCP','NSE:DABUR','NSE:ATGL','NSE:SHREECEM','NSE:HAL','NSE:HINDALCO','NSE:VBL','NSE:DLF','NSE:BANKBARODA','NSE:INDUSINDBK','NSE:EICHERMOT','NSE:DRREDDY','NSE:DIVISLAB','NSE:BPCL','NSE:HAVELLS','NSE:ADANIPOWER','NSE:INDIGO','NSE:CIPLA','NSE:AMBUJACEM','NSE:SRF','NSE:ABB','NSE:BEL','NSE:SBICARD','NSE:GAIL','NSE:BAJAJHLDNG','NSE:TATACONSUM','NSE:ICICIPRULI','NSE:CHOLAFIN','NSE:MARICO','NSE:APOLLOHOSP','NSE:TATAPOWER','NSE:BOSCHLTD','NSE:BERGEPAINT','NSE:JINDALSTEL','NSE:MCDOWELL-N','NSE:UPL','NSE:AWL','NSE:ICICIGI','NSE:TORNTPHARM','NSE:CANBK','NSE:PNB','NSE:TVSMOTOR','NSE:ZYDUSLIFE','NSE:TIINDIA','NSE:TRENT','NSE:IDBI','NSE:NAUKRI','NSE:SHRIRAMFIN','NSE:HEROMOTOCO','NSE:INDHOTEL','NSE:PIIND','NSE:IRCTC','NSE:CGPOWER','NSE:UNIONBAN','NSE:MOTHERSON','NSE:CUMMINSIND','NSE:SCHAEFFLER','NSE:LODHA','NSE:ZOMATO','NSE:PGHH','NSE:YESBANK','NSE:POLYCAB','NSE:MAXHEALTH','NSE:IOB','NSE:PAGEI','NSE:COLPAL','NSE:ASHOKLEY','NSE:ALKEM','NSE:NHPC','NSE:PAYTM','NSE:PFC','NSE:JSWENERGY','NSE:MUTHOOTFIN','NSE:AUBANK','NSE:INDUSTOWER','NSE:BALKRISIND','NSE:UBL','NSE:ABCAPITAL','NSE:TATAELXSI','NSE:DALBHARAT','NSE:HDFCAMC','NSE:INDIANB','NSE:ASTRAL','NSE:BHARATFORG','NSE:LTTS','NSE:MRF','NSE:TATACOMM','NSE:NYKAA','NSE:CONCOR','NSE:PERSISTENT','NSE:PATANJALI','NSE:IRFC','NSE:LINDEINDIA','NSE:IDFCFIRSTB','NSE:PETRONET','NSE:SOLARINDS','NSE:SAIL','NSE:MPHASIS','NSE:HINDPETRO','NSE:APLAPOLLO','NSE:FLUOROCHEM','NSE:NMDC','NSE:HONAUT','NSE:SUPREMEIND','NSE:GUJGASLTD','NSE:BANDHANBNK','NSE:ACC','NSE:OBEROIRLTY','NSE:BANKINDIA','NSE:RECLTD','NSE:AUROPHARMA','NSE:STARHEALTH','NSE:IGL','NSE:LUPIN','NSE:UCOBANK','NSE:JUBLFOOD','NSE:POLICYBZR','NSE:GODREJPROP','NSE:M&MFIN','NSE:IDEA','NSE:OFSS','NSE:FEDERALBNK','NSE:MANYAVAR','NSE:UNOMINDA','NSE:AIAENG','NSE:THERMAX','NSE:OIL','NSE:VOLTAS','NSE:3MINDIA','NSE:COROMANDEL','NSE:SUNDARMFIN','NSE:KPITTECH','NSE:DEEPAKNTR','NSE:ESCORTS','NSE:BIOCON','NSE:TATACHEM','NSE:TORNTPOWER','NSE:GMRINFRA','NSE:BHEL','NSE:SONACOMS','NSE:DELHIVERY','NSE:SYNGENE','NSE:CRISIL','NSE:GICRE''NSE:COFORGE','NSE:PHOENIXLTD','NSE:JKCEMENT','NSE:POONAWALLA','NSE:GLAXO','NSE:MFSL','NSE:METROBRAND','NSE:MSUMI','NSE:SUMICHEM','NSE:RELAXO','NSE:NAVINFLUOR','NSE:SKFINDIA','NSE:CENTRALBK','NSE:GLAND','NSE:KANSAINER','NSE:GRINDWELL','NSE:TIMKEN','NSE:IPCALAB','NSE:SUNDRMFAST','NSE:ATUL','NSE:ZEEL','NSE:L&TFH','NSE:ABFRL','NSE:APOLLOTYRE','NSE:KPRMILL','NSE:ZFCVINDIA','NSE:FORTIS','NSE:AARTIIND','NSE:HATSUN','NSE:CARBORUNIV','NSE:CROMPTON','NSE:VINATIORGA','NSE:IIFL','NSE:BATAINDIA','NSE:BDL','NSE:LICHSGFIN','NSE:RAJESHEXPO','NSE:RAMCOCEM','NSE:ENDURANCE','NSE:DEVYANI','NSE:PSB','NSE:DIXON','NSE:KAJARIACER','NSE:WHIRLPOOL','NSE:MAHABANK','NSE:SUNTV','NSE:PEL','NSE:PRESTIGE','NSE:NIACL','NSE:RADICO','NSE:PFIZER','NSE:NH','NSE:EMAMILTD','NSE:LAURUSLABS','NSE:FIVESTAR','NSE:AJANTPHARM','NSE:INDIAMART','NSE:360ONE','NSE:KEI','NSE:JBCHEPHARM','NSE:LALPATHLAB','NSE:JSL','NSE:IRB','NSE:EXIDEIND','NSE:PVR','NSE:GSPL','NSE:BLUEDART','NSE:NATIONALUM','NSE:RVNL','NSE:CREDITACC','NSE:TRIDENT','NSE:POWERINDIA','NSE:MEDANTA','NSE:GILLETTE','NSE:RATNAMANI','NSE:ELGIEQUIP','NSE:ISEC','NSE:CGCL','NSE:GODREJIND','NSE:CLEAN','NSE:MAZDOCK','NSE:MAHINDCIE','NSE:AEGISCHEM','NSE:FACT','NSE:BLUESTARCO','NSE:SANOFI','NSE:FINEORG','NSE:AFFLE','NSE:GLENMARK','NSE:NAM-INDIA','NSE:SJVN','NSE:REDINGTON','NSE:AAVAS','NSE:IDFC','NSE:FINCABLES','NSE:NUVOCO','NSE:BAJAJELEC','NSE:APTUS','NSE:SUVENPHAR','NSE:ASTERDM','NSE:RHIM','NSE:KEC','NSE:SONATSOFTW','NSE:AETHER','NSE:DCMSHRIRAM','NSE:IEX','NSE:HAPPSTMNDS','NSE:KIMS','NSE:ALKYLAMINE','NSE:CYIENT','NSE:CHAMBLFERT','NSE:ASAHIINDIA','NSE:CASTROLIND','NSE:BRIGADE','NSE:KALYANKJIL','NSE:TTML','NSE:VGUARD','NSE:NLCINDIA','NSE:LAXMIMACH','NSE:TRITURBINE','NSE:FINPIPE','NSE:AKZOINDIA','NSE:MANAPPURAM','NSE:EIHOTEL','NSE:CENTURYPLY','NSE:NATCOPHARM','NSE:KIOCL','NSE:CHOLAHLDNG','NSE:CAMPUS','NSE:CAMS','NSE:AMARAJABAT','NSE:ZYDUSWELL','NSE:BASF','NSE:TEJASNET','NSE:APLLTD','NSE:MGL','NSE:GRINFRA','NSE:ANGELONE','NSE:SFL','NSE:TTKPRESTIG','NSE:APARINDS','NSE:HINDCOPPER','NSE:CDSL','NSE:GODFRYPHLP','NSE:RENUKA','NSE:CUB','NSE:JKLAKSHMI','NSE:ANURAS','NSE:MRPL','NSE:GESHIP','NSE:POLYMED','NSE:NSLNISP','NSE:BIKAJI','NSE:MOTILALOFS','NSE:ABSLAMC','NSE:CESC','NSE:TATAINVEST','NSE:ALLCARGO','NSE:KALPATPOWR','NSE:PNBHOUSING''NSE:HUDCO','NSE:ITI','NSE:ROUTE','NSE:RITES','NSE:VTL','NSE:RBLBANK','NSE:HFCL','NSE:KARURVYSYA','NSE:CERA','NSE:EIDPARRY','NSE:INGERRAND','NSE:GALAXYSURF','NSE:PPLPHARMA','NSE:UTIAMC','NSE:KRBL','NSE:RAYMOND','NSE:ASTRAZEN','NSE:VIPIND','NSE:ACI','NSE:BALRAMCHIN','NSE:SUZLON','NSE:GODREJAGRO','NSE:GNFC','NSE:ERIS','NSE:PGHL','NSE:MEDPLUS','NSE:SAPPHIRE','NSE:DATAPATTNS','NSE:SUNCLAYLTD','NSE:JBMA','NSE:EASEMYTRIP','NSE:CCL','NSE:EQUITASBNK','NSE:CHALET','NSE:RAINBOW','NSE:PNCINFRA','NSE:FSL','NSE:KSB','NSE:BSOFT','NSE:KNRCON','NSE:SHOPERSTOP','NSE:SYMPHONY','NSE:CENTURYTEX','NSE:CANFINHOME','NSE:GRANULES','NSE:TANLA','NSE:JYOTHYLAB','NSE:SPLPETRO','NSE:DEEPAKFERT','NSE:CRAFTSMAN','NSE:BIRLACORPN','NSE:BLS','NSE:SHYAMMETL','NSE:NCC','NSE:GMMPFAUDLR','NSE:LATENTVIEW','NSE:USHAMART','NSE:HOMEFIRST','NSE:JKPAPER','NSE:TMB','NSE:JINDWORLD','NSE:METROPOLIS','NSE:SAREGAMA','NSE:NBCC','NSE:ECLERX','NSE:BALAMINES','NSE:WELSPUNIND','NSE:PRAJIND','NSE:COCHINSHIP','NSE:ZENSARTECH','NSE:AMBER','NSE:LEMONTREE','NSE:PRINCEPIPE','NSE:TRIVENI','NSE:GARFIBRES','NSE:LXCHEM','NSE:STLTECH','NSE:CEATLTD','NSE:BSE','NSE:SPARC','NSE:ALOKINDS','NSE:ORIENTELEC','NSE:INDIACEM','NSE:JUBLINGREA','NSE:KIRLOSENG','NSE:TCIEXP','NSE:JMFINANCIL','NSE:NETWORK18','NSE:BBTC','NSE:SWANENERGY','NSE:GPPL','NSE:KAYNES','NSE:VRLLOG','NSE:INTELLECT','NSE:SWSOLAR','NSE:CHEMPLASTS','NSE:QUESS','NSE:ROLEXRINGS','NSE:MAHLIFE','NSE:ESABINDIA','NSE:MHRIL','NSE:GOCOLORS','NSE:HGS','NSE:BORORENEW','NSE:GAEL','NSE:MAPMYINDIA','NSE:PRSMJOHNSN','NSE:RUSTOMJEE','NSE:IRCON','NSE:RCF','NSE:WELCORP','NSE:BEML','NSE:GRSE','NSE:EPL','NSE:MINDACORP','NSE:GRAPHITE','NSE:HGINFRA','NSE:OLECTRA','NSE:RELINFRA','NSE:JUSTDIAL','NSE:RAIN','NSE:IONEXCHANG','NSE:EDELWEISS','NSE:UJJIVANSFB','NSE:TV18BRDCST','NSE:GPIL','NSE:MTARTECH','NSE:TCI','NSE:RTNINDIA','NSE:VSTIND','NSE:SAFARI','NSE:ACE','NSE:MAHSCOOTER','NSE:DELTACORP','NSE:GLS','NSE:GHCL','NSE:INDIGOPNTS','NSE:MAHSEAMLES','NSE:SUPRAJIT','NSE:KFINTECH','NSE:GSFC','NSE:J&KBANK','NSE:RELIGARE','NSE:MASTEK','NSE:SIS','NSE:JINDALSAW','NSE:TEGA','NSE:TNPL','NSE:KPIGREEN','NSE:BFINVEST','NSE:SESHAPAPER','NSE:DHAMPURSUG','NSE:ANDHRSUGAR','NSE:KIRIINDUS','NSE:TTKHLTCARE','NSE:CARYSIL','NSE:GOCLCORP','NSE:JSWISPL','NSE:STERTOOLS','NSE:SHALBY','NSE:TIDEWATER','NSE:KRSNAA','NSE:KRISHANA','NSE:HUHTAMAKI','NSE:BBL','NSE:SEPC','NSE:ORISSAMINE','NSE:FILATEX','NSE:THEJO','NSE:APTECHT','NSE:ORIENTHOT','NSE:DCXINDIA','NSE:FOSECOIND','NSE:GOLDIAM','NSE:SHANKARA','NSE:INSECTICID','NSE:THANGAMAYL','NSE:SHK','NSE:TEXRAIL','NSE:CANTABIL','NSE:GALLANTT','NSE:HERITGFOOD','NSE:KCP','NSE:MOREPENLAB','NSE:GATI','NSE:RAMASTEEL','NSE:HESTERBIO','NSE:NRBBEARING','NSE:INDOSTAR','NSE:MONTECARLO','NSE:KSL','NSE:KDDL','NSE:TCPLPACK','NSE:MARATHON','NSE:ARVSMART','NSE:DCW','NSE:DEN','NSE:STEELXIND','NSE:EIHAHOTELS','NSE:IGPL','NSE:NITINSPIN','NSE:EXPLEOSOL','NSE:VERANDA','NSE:SALASAR','NSE:STYRENIX','NSE:ADORWELD','NSE:BHAGCHEM','NSE:PCJEWELLER','NSE:GENESYS','NSE:STOVEKRAFT','NSE:RANEHOLDIN','NSE:NDTV','NSE:XPROINDIA','NSE:MANORAMA','NSE:GRWRHITECH','NSE:HARIOMPIPE','NSE:SANDHAR','NSE:AVTNPL','NSE:IWEL','NSE:SJS','NSE:EVERESTIND','NSE:FAIRCHEMOR','NSE:SASKEN','NSE:OAL','NSE:NELCO','NSE:RIIL','NSE:SOLARA','NSE:TAJGVK','NSE:BOMDYEING','NSE:MANGCHEFER','NSE:GOODLUCK','NSE:RPGLIFE','NSE:PATELENG','NSE:SPIC','NSE:INOXGREEN','NSE:GIPCL','NSE:UNIVCABLES','NSE:NSIL','NSE:HMT','NSE:MATRIMONY','NSE:MTNL','NSE:SDBL','NSE:VALIANTORG','NSE:ARMANFIN','NSE:REPCOHOME','NSE:HERANBA','NSE:BFUTILITIE','NSE:PRECWIRE','NSE:AXITA','NSE:GRMOVER','NSE:GTPL','NSE:IGARASHI','NSE:INFOBEAN','NSE:ALICON','NSE:THEMISMED','NSE:TVTODAY','NSE:WHEELS','NSE:RPSGVENT','NSE:RAMCOIND','NSE:SMLISUZU','NSE:AHL','NSE:UNIENTER','NSE:SATIN','NSE:KUANTUM','NSE:GANESHBE','NSE:SUVEN','NSE:SYRMA','NSE:AVANTIFEED','NSE:STARCEMENT','NSE:IBULHSGFIN','NSE:RKFORGE','NSE:CAPLIPOINT','NSE:VAIBHAVGBL','NSE:RBA','NSE:JUBLPHARMA','NSE:SHARDACROP','NSE:NIITLTD','NSE:PCBL','NSE:MASFIN','NSE:SCI','NSE:PDSL','NSE:GUJALKALI','NSE:ELECON','NSE:CMSINFO','NSE:VMART','NSE:ICRA','NSE:JSWHL','NSE:FDC','NSE:CSBBANK','NSE:KTKBANK','NSE:MMTC','NSE:ENGINERSIN','NSE:SUNTECK','NSE:PRIVISCL','NSE:PARADEEP','NSE:SOBHA','NSE:FUSION','NSE:GMDCLTD','NSE:VIJAYA','NSE:JAMNAAUTO','NSE:ANANTRAJ','NSE:SANSERA','NSE:MFL','NSE:AHLUCONT','NSE:BSHSL','NSE:TATACOFFEE','NSE:TEAMLEASE','NSE:JKTYRE','NSE:VARROC','NSE:GREENLAM','NSE:JPPOWER','NSE:INFIBEAM','NSE:SPANDANA','NSE:HSCL','NSE:BHARATRAS','NSE:RAJRATAN','NSE:LAOPALA','NSE:SARDAEN','NSE:RALLIS','NSE:BOROLTD','NSE:RATEGAIN','NSE:SCHNEIDER','NSE:RPOWER','NSE:ARVINDFASN','NSE:TATVA','NSE:POWERMECH','NSE:HCG','NSE:NESCO','NSE:HEIDELBERG','NSE:TECHNOE','NSE:POLYPLEX','NSE:SURYAROSNI','NSE:AUTOAXLES','NSE:JWL','NSE:NFL','NSE:HEG','NSE:RAJRILTD','NSE:CHENNPETRO','NSE:WSTCSTPAPR','NSE:LUXIND','NSE:HIKAL','NSE:MIDHANI','NSE:HLEGLAS','NSE:SHAREINDIA','NSE:NOCIL','NSE:NAZARA','NSE:BANARISUG','NSE:ANANDRATHI','NSE:PRUDENT','NSE:GRAVITA','NSE:GREENPANEL','NSE:VESUVIUS','NSE:DCBBANK','NSE:ROSSARI','NSE:RESPONIND','NSE:TINPLATE','NSE:KIRLOSBROS','NSE:RAILTEL','NSE:AMIORG','NSE:ISGEC','NSE:NEOGEN','NSE:MARKSANS','NSE:NAVA','NSE:NEWGEN','NSE:BECTORFOOD','NSE:TWL','NSE:AARTIDRUGS','NSE:UJJIVAN','NSE:GATEWAY','NSE:SULA','NSE:DAAWAT','NSE:SOUTHBANK','NSE:GET&D','NSE:HARSHA','NSE:PGEL','NSE:RSYSTEMS','NSE:INDOCO','NSE:MOLDTKPAC','NSE:IFBIND','NSE:SBCL','NSE:BCG','NSE:GREAVESCOT','NSE:MOIL','NSE:TATASTLLP','NSE:TARSONS','NSE:SHANTIGEAR','NSE:CHOICEIN','NSE:TIIL','NSE:DHANUKA','NSE:JCHAC','NSE:DODLA','NSE:DALMIASUG','NSE:VOLTAMP','NSE:ASTEC','NSE:SUDARSCHEM','NSE:KSCL','NSE:SUNFLAG','NSE:IBREALEST','NSE:THOMASCOOK','NSE:HBLPOWER','NSE:INOXWIND','NSE:NILKAMAL','NSE:ZENTEC','NSE:TCNSBRANDS','NSE:ADVENZYMES','NSE:STAR','NSE:FCL','NSE:KKCL','NSE:HINDWAREAP','NSE:MAHLOG','NSE:EMIL','NSE:JTEKTINDIA','NSE:MANINFRA','NSE:ITDC','NSE:APCOTEXIND','NSE:PRICOLLTD','NSE:PTC','NSE:AARTIPHARM','NSE:MBAPL','NSE:SAGCEM','NSE:TDPOWERSYS','NSE:JAICORPLTD','NSE:DBL','NSE:BARBEQUE','NSE:UNIPARTS','NSE:UFLEX','NSE:WONDERLA','NSE:PSPPROJECT','NSE:KIRLOSIND','NSE:IPL','NSE:DISHTV','NSE:TATAMETALI','NSE:PAISALO','NSE:PFOCUS','NSE:HEMIPROP','NSE:LGBBROSLTD','NSE:MAITHANALL','NSE:SSWL','NSE:NEULANDLAB','NSE:HATHWAY','NSE:THYROCARE','NSE:ORIENTCEM','NSE:DREAMFOLKS','NSE:ETHOSLTD','NSE:GLOBUSSPR','NSE:GANESHHOUC','NSE:ARVIND','NSE:ICIL','NSE:SHRIPISTON','NSE:WOCKPHARMA','NSE:DBREALTY','NSE:ISMTLTD','NSE:JINDALPOLY','NSE:WABAG','NSE:BAJAJCON','NSE:GENUSPOWER','NSE:BUTTERFLY','NSE:NAVNETEDUL','NSE:GOKEX','NSE:APOLLOPIPE','NSE:LANDMARK','NSE:IFCI','NSE:ATFL','NSE:EVEREADY','NSE:AGI','NSE:TI','NSE:ASHOKA','NSE:SOMANYCERA','NSE:HCC','NSE:JISLJALEQS','NSE:VINDHYATEL','NSE:FIEMIND','NSE:TASTYBITE','NSE:JAYNECOIND','NSE:HONDAPOWER','NSE:UNICHEMLAB','NSE:MUKANDLTD','NSE:CIGNITITEC','NSE:MMFL','NSE:VENKEYS','NSE:RAMKY','NSE:DIVGIITTS','NSE:CAMLINFINE','NSE:SHILPAMED','NSE:GULFOILLUB','NSE:MOL','NSE:DOLLAR','NSE:VSTTILLERS','NSE:SUBROS','NSE:DCAL','NSE:GABRIEL','NSE:MAXVIL','NSE:SIYSIL','NSE:TVSSRICHAK','NSE:ASTRAMICRO','NSE:JKIL','NSE:JAGRAN','NSE:ELECTCAST','NSE:CARERATING','NSE:INDIAGLYCO','NSE:BALMLAWRIE','NSE:KOLTEPATIL','NSE:IMAGICAA','NSE:WELENT','NSE:TIPSINDLTD','NSE:SWARAJENG','NSE:MAYURUNIQ','NSE:GANECOS','NSE:PARAS','NSE:LUMAXTECH','NSE:ACCELYA','NSE:KESORAMIND','NSE:CARTRADE','NSE:MPSLTD','NSE:SEQUENT','NSE:HIL','NSE:GUFICBIO','NSE:ITDCEM','NSE:PILANIINVS','NSE:MSTCLTD','NSE:LSIL','NSE:PANAMAPET','NSE:OPTIEMUS','NSE:SIRCA','NSE:TIRUMALCHM','NSE:DYNAMATECH','NSE:SUNDARMHLD','NSE:TIMETECHNO','NSE:DBCORP','NSE:ASHIANA','NSE:CONFIPET','NSE:DIAMONDYD','NSE:NUCLEUS','NSE:GREENPLY','NSE:JPASSOCIAT','NSE:WENDT','NSE:FINOPB','NSE:FMGOETZE','NSE:SANGHIIND','NSE:VAKRANGEE','NSE:GNA','NSE:AMRUTANJAN','NSE:EMUDHRA','NSE:DATAMATICS','NSE:SHARDAMOTR','NSE:IOLCP','NSE:LUMAXIND','NSE:BAJAJHIND','NSE:STYLAMIND','NSE:ANDHRAPAP','NSE:SOTL','NSE:ADFFOODS','NSE:VIDHIING','NSE:KABRAEXTRU','NSE:BEPL','NSE:RUPA','NSE:NACLIND','NSE:VSSL','NSE:VISHNU','NSE:DWARKESH','NSE:DHANI','NSE:BANCOINDIA','NSE:KINGFA','NSE:SUBEXLTD','NSE:HINDOILEXP','NSE:RTNPOWER','NSE:VADILALIND','NSE:BBOX','NSE:ORCHPHARMA','NSE:PURVA','NSE:COSMOFIRST','NSE:IMFA','NSE:SUPRIYA','NSE:SAKSOFT','NSE:IIFLSEC','NSE:SANGHVIMOV','NSE:GOKULAGRO','NSE:ALEMBICLTD','NSE:VENUSPIPES','NSE:SEAMECLTD','NSE:SATIA','NSE:GULPOLY','NSE:UGARSUGAR','NSE:MANALIPETC','NSE:PIXTRANS','NSE:SHRIRAMPPS','NSE:RADIANTCMS','NSE:PNBGILTS','NSE:INDORAMA','NSE:ASHAPURMIN','NSE:UGROCAP','NSE:AXISCADES','NSE:HITECH','NSE:PUNJABCHEM','NSE:SURYODAY','NSE:EKC','NSE:JASH','NSE:DPSCLTD','NSE:TARC','NSE:BHARATWIRE','NSE:EXCELINDUS','NSE:SPECIALITY','NSE:ANUP','NSE:SKIPPER','NSE:AJMERA','NSE:SHALPAINTS','NSE:GMBREW','NSE:SANGAMIND','NSE:SHIVALIK','NSE:GMRP&UI','NSE:PENIND','NSE:GEOJITFSL','NSE:BCLIND','NSE:DBOL','NSE:SHAILY','NSE:LIKHITHA','NSE:MADRASFERT','NSE:STEELCAS','NSE:MKPL','NSE:ROSSELLIND','NSE:KITEX','NSE:PRAKASH','NSE:ARTEMISMED','NSE:RICOAUTO','NSE:OMAXE','NSE:CENTUM','NSE:ROTO','NSE:PRECAM','NSE:BIGBLOC','NSE:SHREDIGCEM','NSE:CLSEL','NSE:GTLINFRA','NSE:PGIL','NSE:UTTAMSUGAR','NSE:AVADHSUGAR','NSE:PITTIENG','NSE:5PAISA','NSE:NAHARSPING','NSE:SPCENET','NSE:SPORTKING','NSE:DEEPINDS','NSE:PARAGMILK','NSE:AGARIND','NSE:CONTROLPR','NSE:BAJAJHCARE','NSE:KAMDHENU','NSE:CHEMCON','NSE:GICHSGFIN','NSE:MEDICAMEQ','NSE:DLINKINDIA','NSE:ARIHANTSUP','NSE:VHL','NSE:PFS','NSE:HEXATRADEX','NSE:RILINFRA','NSE:CAPACITE','NSE:SPAL','NSE:NCLIND','NSE:63MOONS','NSE:NAVKARCORP','NSE:ORIENTPPR','NSE:DREDGECORP','NSE:AMBIKCO','NSE:CENTRUM','NSE:LINC','NSE:RGL','NSE:SCHAND','NSE:NELCAST','NSE:FAZE3Q','NSE:KICL','NSE:DVL','NSE:JAGSNPHARM','NSE:POKARNA','NSE:IFGLEXPOR','NSE:TRIL','NSE:CENTENKA','NSE:SMCGLOBAL','NSE:ROHLTD','NSE:INDNIPPON','NSE:SHAKTIPUMP','NSE:NGLFINE','NSE:IMPAL','NSE:BLISSGVS','NSE:ALLSEC','NSE:ORIENTBELL','NSE:MANGLMCEM','NSE:SANDESH','NSE:BODALCHEM','NSE:ESTER','NSE:ZOTA','NSE:RSWM','NSE:INDRAMEDCO','NSE:QUICKHEAL','NSE:SRHHYPOLTD','NSE:AURIONPRO','NSE:GSLSU','NSE:SASTASUNDR','NSE:MANAKSIA','NSE:AWHCL','NSE:BLKASHYAP','NSE:RAMRAT','NSE:JINDRILL','NSE:VIMTALABS','NSE:CLOUD','NSE:DPABHUSHAN','NSE:MOLDTECH','NSE:ATULAUTO','NSE:KOKUYOCMLN','NSE:SIGACHI','NSE:HIMATSEIDE','NSE:LINCOLN','NSE:GREENPOWER','NSE:EMAMIPAP','NSE:SATINDLTD','NSE:RAMCOSYS','NSE:HPAL','NSE:OCCL','NSE:FOCUS','NSE:GEPIL','NSE:SUTLEJTEX','NSE:PANACEABIO','NSE:JAIBALAJI','NSE:RML','NSE:JETAIRWAYS','NSE:TRACXN','NSE:KHAICHEM','NSE:TNPETRO', 'NSE:ONWARDTEC','NSE:TFCILTD','NSE:ONMOBILE','NSE:INNOVANA','NSE:GANDHITUBE','NSE:TEXINFRA','NSE:MEDICO','NSE:TVSELECT','NSE:HEUBACHIND','NSE:VINYLINDIA','NSE:PARACABLES','NSE:FOODSIN','NSE:HLVLTD','NSE:COFFEEDAY','NSE:BETA','NSE:APEX','NSE:YUKEN','NSE:ELIN','NSE:MONARCH','NSE:DMCC','NSE:CHEVIOT','NSE:XCHANGING','NSE:VISAKAIND','NSE:SUMMITSEC','NSE:SUKHJITS','NSE:INDIANHUME','NSE:JUBLINDS','NSE:ASALCBR','NSE:DECCANCE','NSE:JAYBARMARU','NSE:COOLCAPS','NSE:APOLLO','NSE:ELDEHSG','NSE:HERCULES','NSE:4THDIM','NSE:KRITI','NSE:AGSTRA','NSE:NAHARPOLY','NSE:MANINDS','NSE:ENIL','NSE:SYNCOMF','NSE:KAMOPAINTS','NSE:NAGAFERT','NSE:SCPL','NSE:HPL','NSE:INDOAMIN','NSE:DCMSRIND','NSE:MENONBE','NSE:VASCONEQ','NSE:VLSFINANCE','NSE:BALAXI','NSE:ZEEMEDIA','NSE:CREATIVE','NSE:KRISHIVAL','NSE:SNOWMAN','NSE:KOPRAN','NSE:SHREYAS','NSE:REFEX','NSE:KSOLVES','NSE:GFLLIMITED','NSE:SPECTRUM','NSE:RUSHIL','NSE:IRISDOREME','NSE:BINDALAGRO','NSE:SELMC','NSE:BHAGERIA','NSE:ZUARI','NSE:TALBROAUTO','NSE:RUBYMILLS','NSE:OSWALSEEDS','NSE:DPWIRES','NSE:SMSPHARMA','NSE:DHARMAJ','NSE:RBL','NSE:GOYALALUM','NSE:NRL','NSE:MIRZAINT','NSE:VIKASLIFE','NSE:WINDLAS','NSE:HITECHGEAR','NSE:SHREEPUSHK','NSE:SPENCERS','NSE:KANORICHEM','NSE:JPOLYINVST','NSE:ASAL','NSE:SILVERTUC','NSE:3IINFOLTD','NSE:MALLCOM','NSE:CREST','NSE:REPRO','NSE:MARINE','NSE:KECL','NSE:DENORA','NSE:EXXARO','NSE:MAGADSUGAR','NSE:ASIANTILES','NSE:JAYAGROGN','NSE:DIGISPICE','NSE:BBTCL','NSE:PREMEXPLN','NSE:SWELECTES','NSE:KELLTONTEC','NSE:MUTHOOTCAP','NSE:APCL','NSE:ASIANENE','NSE:DONEAR','NSE:ADSL','NSE:BANSWRAS','NSE:NAHARCAP','NSE:ICEMAKE','NSE:BAIDFIN','NSE:STCINDIA','NSE:TBZ','NSE:SALZERELEC','NSE:IFBAGRO','NSE:PTL','NSE:ARIHANTCAP','NSE:CSLFINANCE','NSE:JSLL','NSE:UNIVPHOTO','NSE:HARDWYN','NSE:DSSL','NSE:REVATHI','NSE:HCL-INSYS','NSE:PLASTIBLEN','NSE:UNIDT','NSE:CAREERP','NSE:ARROWGREEN','NSE:SREEL','NSE:SBC','NSE:RADIOCITY','NSE:SERVOTECH','NSE:SAKAR','NSE:BALAJITELE','NSE:NXTDIGITAL','NSE:GOACARBON','NSE:BIRLACABLE','NSE:RITCO','NSE:SELAN','NSE:ASCOM','NSE:OSIAHYPER','NSE:HINDCOMPOS','NSE:DHANBANK','NSE:DYCL','NSE:DHUNINV','NSE:EIFFL','NSE:MUNJALAU','NSE:NAHARINDUS','NSE:DELPHIFX','NSE:URJA','NSE:PRIMESECU','NSE:NECLIFE','NSE:NBIFIN','NSE:GRPLTD','NSE:MAWANASUG','NSE:ZIMLAB','NSE:PDMJEPAPER','NSE:ONEPOINT','NSE:MAXIND','NSE:SHYAMCENT','NSE:VARDHACRLC','NSE:RADHIKAJWE','NSE:NPST','NSE:THEINVEST','NSE:HTMEDIA','NSE:NRAIL','NSE:RCOM','NSE:DICIND','NSE:OSWALAGRO','NSE:POCL','NSE:AARTISURF','NSE:SKMEGGPROD','NSE:WEL','NSE:SUPERHOUSE','NSE:LOYALTEX','NSE:BPL','NSE:BIRLAMONEY','NSE:GPTINFRA','NSE:E2E','NSE:SHIVAMAUTO','NSE:DCMNVL','NSE:MAZDA','NSE:MADHAVBAUG','NSE:WINDMACHIN','NSE:BASML','NSE:WALCHANNAG','NSE:SEJALLTD','NSE:UCALFUEL','NSE:MAHEPC','NSE:V2RETAIL','NSE:SAKUMA','NSE:QMSMEDI','NSE:MANAKSTEEL','NSE:EMAMIREAL','NSE:GENCON','NSE:STARPAPER','NSE:GUJAPOLLO','NSE:JAYSREETEA','NSE:NDL','NSE:BCONCEPTS''NSE:GIRRESORTS','NSE:SMLT','NSE:TPLPLASTEH','NSE:TEMBO','NSE:DANGEE','NSE:NIPPOBATRY','NSE:ASIANHOTNR','NSE:BRNL','NSE:PPAP','NSE:PASUPTAC','NSE:FROG','NSE:ASAHISONG','NSE:PRECOT','NSE:MEP','NSE:VENUSREM','NSE:KILITCH','NSE:BTML','NSE:MEGASTAR','NSE:DRCSYSTEMS','NSE:ZODIACLOTH','NSE:HILTON','NSE:INDOTHAI','NSE:JITFINFRA','NSE:EROSMEDIA','NSE:DEVIT','NSE:BIL','NSE:EIMCOELECO','NSE:ANMOL','NSE:COASTCORP','NSE:RAJTV','NSE:KORE','NSE:RELCAPITAL','NSE:MGEL','NSE:FOCE','NSE:INDTERRAIN','NSE:TAKE','NSE:TOTAL','NSE:ACCURACY','NSE:AVG','NSE:HARRMALAYA','NSE:SHREYANIND','NSE:LOKESHMACH','NSE:LGBFORGE','NSE:SYSTANGO','NSE:SIGMA','NSE:MARALOVER','NSE:ABAN','NSE:BAFNAPH','NSE:BEDMUTHA','NSE:SIMPLEXINF','NSE:ARIES','NSE:DTIL','NSE:KRITINUT','NSE:IVC','NSE:IITL','NSE:SWASTIK','NSE:AARON','NSE:VITAL','NSE:AISL','NSE:SHAIVAL','NSE:VINEETLAB','NSE:ARISTO','NSE:TERASOFT','NSE:CROWN','NSE:JFLLIFE','NSE:GLOBE','NSE:3PLAND','NSE:VERA','NSE:MILTON','NSE:ADROITINFO','NSE:SHUBHLAXMI','NSE:AGNI','NSE:LFIC','NSE:VSCL','NSE:MADHAV','NSE:UJAAS','NSE:SUPERSPIN','NSE:RKDL','NSE:AMBICAAGAR','NSE:ACEINTEG','NSE:OMFURN','NSE:SWARAJ','NSE:AJOONI','NSE:KHANDSE','NSE:SAGARDEEP','NSE:REXPIPES','NSE:ADL','NSE:MCON','NSE:CADSYS','NSE:HBSL','NSE:SANGINITA','NSE:GANGAFORGE','NSE:ABINFRA','NSE:PERFECT','NSE:NARMADA','NSE:RMDRIP','NSE:NAGREEKCAP','NSE:LAXMICOT','NSE:PEARLPOLY','NSE:HECPROJECT','NSE:SANWARIA','NSE:MEGAFLEX','NSE:BALKRISHNA','NSE:MTEDUCARE','NSE:GODHA','NSE:GOENKA','NSE:HAVISHA','NSE:QUADPRO','NSE:QFIL','NSE:MADHUCON','NSE:ROLLT','NSE:CYBERMEDIA','NSE:JAKHARIA','NSE:VEEKAYEM','NSE:TGBHOTELS','NSE:VIVIDHA','NSE:FMNL','NSE:WALPAR','NSE:DESTINY','NSE:SUMEETINDS','NSE:ICDSLTD','NSE:LRRPL','NSE:MPTODAY','NSE:21STCENMGM','NSE:HYBRIDFIN','NSE:SABAR','NSE:TFL','NSE:IMPEXFERRO','NSE:INFOMEDIA','NSE:NKIND','NSE:SHANTI','NSE:GRCL','NSE:FEL','NSE:THOMASCOTT','NSE:KHAITANLTD','NSE:WILLAMAGOR','NSE:LCCINFOTEC','NSE:UNIINFO','NSE:ASMS','NSE:VIVO','NSE:GAYAHWS','NSE:CALSOFT','NSE:MOXSH','NSE:ORIENTALTL','NSE:ONELIFECAP','NSE:VIJIFIN','NSE:DIGJAMLMTD','NSE:KRIDHANINF','NSE:SILLYMONKS','NSE:MAKS','NSE:TANTIACONS','NSE:SUPREMEENG','NSE:SILGO','NSE:MOHITIND','NSE:EDUCOMP','NSE:EASTSILK','NSE:KANDARP','NSE:CMICABLES','NSE:NATNLSTEEL','NSE:MITTAL','NSE:SPRL','NSE:ORTINLAB','NSE:BRIGHT','NSE:KAUSHALYA','NSE:GUJRAFFIA','NSE:MASKINVEST','NSE:ISHAN','NSE:CONTI','NSE:AMIABLE','NSE:AILIMITED','NSE:EUROTEXIND','NSE:TIJARIA','NSE:TNTELE','NSE:KALYANI','NSE:ASMS','NSE:VIVO','NSE:GAYAHWS','NSE:CALSOFT','NSE:MOXSH','NSE:ORIENTALTL','NSE:ONELIFECAP','NSE:VIJIFIN','NSE:DIGJAMLMTD','NSE:KRIDHANINF','NSE:SILLYMONKS','NSE:MAKS','NSE:TANTIACONS','NSE:SUPREMEENG','NSE:SILGO','NSE:MOHITIND','NSE:EDUCOMP','NSE:EASTSILK','NSE:KANDARP','NSE:CMICABLES','NSE:NATNLSTEEL','NSE:MITTAL','NSE:SPRL','NSE:ORTINLAB','NSE:BRIGHT','NSE:KAUSHALYA','NSE:GUJRAFFIA','NSE:MASKINVEST','NSE:ISHAN','NSE:CONTI','NSE:AMIABLE','NSE:AILIMITED','NSE:EUROTEXIND','NSE:TIJARIA','NSE:TNTELE','NSE:KALYANI','NSE:SETUINFRA','NSE:GRETEX','NSE:LYPSAGEMS','NSE:METALFORGE','NSE:SSINFRA','NSE:SMVD','NSE:RMCL','NSE:JALAN','NSE:SANCO','NSE:VASA','NSE:KAVVERITEL','NSE:TECHIN','NSE:NORBTEAEXP','NSE:KCK','NSE:SPENTEX','NSE:CREATIVEYE','NSE:ANTGRAPHIC','NSE:TVVISION','NSE:ABNINT','NSE:ARENTERP','NSE:UMESLTD','NSE:SHYAMTEL','NSE:MANAV','NSE:ACCORD','NSE:DRL','NSE:GLFL','NSE:CMMIPL','NSE:NIRAJISPAT','NSE:DCMFINSERV','NSE:SRIRAM','NSE:PREMIER','NSE:SKSTEXTILE','NSE:SABTN','NSE:TARAPUR','NSE:BKMINDST','NSE:ALPSINDUS','NSE:AHIMSA','NSE:BHALCHANDR','NSE:INNOVATIVE','NSE:LAKPRE','NSE:TRANSWIND','NSE:MELSTAR','NSE:SABEVENTS','NSE:INDLMETER','NSE:TECILCHEM','NSE:ABHISHEK','NSE:AHLWEST','NSE:AIFL','NSE:AJRINFRA','NSE:ALCHEM','NSE:AMJUMBO','NSE:ANDHRACEMT','NSE:ANSALAPI','NSE:ARCOTECH','NSE:ARSSINFRA','NSE:ARTEDZ','NSE:ASIL','NSE:ATCOM','NSE:ATLASCYCLE','NSE:ATNINTER','NSE:AUTOLITIND','NSE:AUTORIDFIN','NSE:BANSAL','NSE:BGLOBAL','NSE:BHARATIDIL','NSE:BILENERGY','NSE:BIRLATYRE','NSE:BLUEBLENDS','NSE:BLUECHIP','NSE:BLUECOAST','NSE:BRFL','NSE:CANDC','NSE:CCCL','NSE:CELESTIAL','NSE:CKFSL','NSE:DFMFOODS','NSE:DIAPOWER','NSE:DOLPHINOFF','NSE:DQE','NSE:DSKULKARNI','NSE:EASTSUGIND','NSE:EASUNREYRL','NSE:EMCO','NSE:EON','NSE:EUROCERA','NSE:EUROMULTI','NSE:FEDDERELEC','NSE:FIVECORE','NSE:GAMMONIND','NSE:GANGOTRI','NSE:GBGLOBAL','NSE:GFSTEELS','NSE:GITANJALI','NSE:HINDNATGLS','NSE:ICSA','NSE:INDOSOLAR','NSE:IVRCLINFRA','NSE:JAINSTUDIO','NSE:JBFIND','NSE:JIKIND','NSE:JINDCOT','NSE:JMTAUTOLTD','NSE:JPINFRATEC','NSE:KEERTI','NSE:KGL','NSE:KSERASERA','NSE:KSK','NSE:LAKSHMIEFL','NSE:LEEL','NSE:MANPASAND','NSE:MBECL','NSE:MCDHOLDING','NSE:MERCATOR','NSE:METKORE','NSE:MODTHREAD','NSE:MOHOTAIND','NSE:MVL','NSE:NAKODA','NSE:NITINFIRE','NSE:NTL','NSE:NUTEK','NSE:OISL','NSE:OMKARCHEM','NSE:OPAL','NSE:OPTOCIRCUI','NSE:ORTEL','NSE:PDPL','NSE:PINCON','NSE:PRATIBHA','NSE:PRUDMOULI','NSE:PSL','NSE:PUNJLLOYD','NSE:QUINTEGRA','NSE:RADAAN','NSE:RAINBOWPAP','NSE:RAJVIR','NSE:RMMIL','NSE:RUSHABEAR','NSE:S&SPOWER','NSE:SATHAISPAT','NSE:SBIHOMEFIN','NSE:SHARONBIO','NSE:SHIRPUR-G','NSE:SICAL','NSE:SIIL','NSE:SKIL','NSE:SONISOYA','NSE:SPYL','NSE:SREINFRA','NSE:STAMPEDE','NSE:TALWALKARS','NSE:TALWGYM','NSE:TCIFINANCE','NSE:TECHNOFAB','NSE:THIRUSUGAR','NSE:TULSI','NSE:UNIPLY','NSE:UNITY','NSE:UNIVAFOODS','NSE:USK','NSE:VALECHAENG','NSE:VALUEIND','NSE:VICEROY','NSE:VIDEOIND','NSE:VIKASPROP','NSE:VISUINTL','NSE:VIVIMEDLAB','NSE:WINSOME','NSE:ZICOM']

# Replace with your subscribed instruments

# Function to filter instruments based on the search input
def filter_instruments(search_text):
    return [instrument for instrument in subscribed_instruments if search_text.lower() in instrument.lower()]

# Function to get the opening price for an instrument (replace this with your logic)
def get_opening_price(instrument_token):
    # Replace this with your logic to get the opening price for the given instrument
    # For now, return a randomly generated opening price
    return random.uniform(1000, 2000)

# Function to update live data for subscribed instruments
def update_live_data():
    while True:
        search_text = search_var.get()
        filtered_instruments = filter_instruments(search_text)
        
        ltp_data = kite.ltp(filtered_instruments)
        for instrument_token, ltp in ltp_data.items():
            update_table(instrument_token, ltp['last_price'])

        app.update_idletasks()
        # Adjust the sleep duration to control the update frequency
        time.sleep(1)  # Update every second

# Function to update the table with instrument, price, and profit/loss
def update_table(instrument_token, price):
    instrument_index = subscribed_instruments.index(instrument_token)
    opening_price = get_opening_price(instrument_token)
    profit_loss = price - opening_price
    tree.item(tree.get_children()[instrument_index], values=(instrument_token, price, profit_loss))

# Function to search for the word in visible text
def search_word(event=None):  # Pass an event to be used as a bind callback
    search_text = search_var.get().lower()
    for instrument_token, ltp_label in ltp_labels.items():
        if search_text in ltp_label.cget("text").lower():
            canvas.yview_moveto(ltp_label.winfo_y() / canvas.winfo_height())
            break

# Function to handle the window closing event
def on_closing():
    data_thread.join()  # Wait for the data thread to finish
    app.destroy()

# Create the main application window
app = tk.Tk()
app.title("Zerodha Live Market Data")
app.geometry("800x600")  # Set initial window size

# Load logo image
logo_image = Image.open("logo.jpg")  # Replace with the path or URL of your logo image
logo_image = logo_image.resize((150, 150), Image.ANTIALIAS) if hasattr(Image, 'ANTIALIAS') else logo_image.resize((150, 150))
logo_photo = ImageTk.PhotoImage(logo_image)

# Logo label
logo_label = tk.Label(app, image=logo_photo, bg="#17202A")  # Set background color
logo_label.pack(side=tk.TOP, padx=10, pady=10)

# Create a canvas with a vertical scrollbar
canvas = tk.Canvas(app, height=400, width=300, bg="#17202A")  # Set background color
canvas.pack(side=tk.LEFT, fill=tk.Y, expand=False)

scrollbar = tk.Scrollbar(app, command=canvas.yview, bg="#17202A")  # Set background color
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Create labels to display live data for each subscribed instrument
ltp_labels = {}
for instrument_token in subscribed_instruments:
    ltp_label = tk.Label(canvas, text="", font=('Helvetica', 16), bg="#17202A", fg="#ecf0f1")  # Set text color
    ltp_label.pack(pady=10, fill=tk.X)
    ltp_labels[instrument_token] = ltp_label

# Search bar with search button in top right
search_var = tk.StringVar()
search_entry = tk.Entry(app, textvariable=search_var, font=('Helvetica', 12), bg="#2C3E50", fg="#ecf0f1", insertbackground="#ecf0f1")  # Set background and text color
search_entry.pack(side=tk.TOP, anchor="e", padx=10, pady=10, fill=tk.X)

search_button = tk.Button(app, text="Search", command=search_word, bg="#3498db", fg="#ecf0f1")  # Set background and text color
search_button.pack(side=tk.TOP, anchor="e", padx=10, pady=5)

# Create a table to display instruments, prices, and profit/loss
columns = ("Instrument", "Price", "Profit/Loss")
tree = ttk.Treeview(app, columns=columns, show="headings", height=15)  # Set height
tree.heading("Instrument", text="Instrument", anchor=tk.CENTER)
tree.heading("Price", text="Price", anchor=tk.CENTER)
tree.heading("Profit/Loss", text="Profit/Loss", anchor=tk.CENTER)
tree.column("Instrument", anchor=tk.CENTER, width=150)
tree.column("Price", anchor=tk.CENTER, width=100)
tree.column("Profit/Loss", anchor=tk.CENTER, width=100)
tree.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

# Insert initial values into the table
for i, instrument in enumerate(subscribed_instruments):
    tree.insert("", i, values=(instrument, "", ""))
    tag = 'evenrow' if i % 2 == 0 else 'oddrow'
    tree.tag_configure(tag, background='#34495e' if tag == 'evenrow' else '#2c3e50')

# Configure the items after inserting them
for i, instrument in enumerate(subscribed_instruments):
    tag = 'evenrow' if i % 2 == 0 else 'oddrow'
    tree.item(tree.get_children()[i], tags=(tag,))

# Create a thread for updating live data
data_thread = threading.Thread(target=update_live_data)
data_thread.daemon = True
data_thread.start()

# Bind the closing event
app.protocol("WM_DELETE_WINDOW", on_closing)

# Start the GUI application
app.mainloop()
