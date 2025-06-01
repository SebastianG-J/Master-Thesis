import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# List of usernames to scrape
usernames = [
 'time24trader', 'MrWave90', 'ValhallaAlgo', 'gerardo_gurrola', 'Ozard_OfWiz', 'crossmargin', 'PolarBearVen', 'TMBS100', 'keeganfreemann',
 'GeorgeWegwitz', 'Jeverson_1984', 'CSJeszek6718', 'mairautafx', 'VictoriaAnd_eth', 'hervecrypto', '_MarketMonkey', 'randomstacker', 'marxcbabu', 'WeZoura', 'DlmebagDarreII', 'AllenBoost', 'pro1xcom', 'CatForecast27', 'jensblack',
 'GVIForex', 'trade_joker', 'BrookeThackray', 'slite998372', 'AlassafSun', 'PRInvestments1', 'strwp', 'Monkey_Trench', 'danthelotte', 'salesboy_1', 'Seismic45', 'nexxtgengroup', 'Pivotal_Trader', 'NexxtGenMarkets', 'epaytogo',
 'AlphafxNadia', 'brienwhite476', 'markets_n_chart', 'hancocktrades', 'LLesego49619', 'smlresearch00', 'Callasxznn', 'aakashchouhan5g', 'RaiyaanTrades', 'J_bobrik', 'TheeRayCordell', 'fxalexj', 'OekonomRichter', 'LILBA_eth', 'Adrian_taqavi',
 'aammiitt2', 'tradingwithdrk', 'Nav369124603', 'liegeshepard', '18Mirex18', 'Cherreyinsights', 'ghattas1994', 'ab1826', 'aligntrading_', 'donaldnguyenit', 'iamvazu', 'WallstreetBarb', 'VikOpine', 'j_jolounge', 'Ronmarkets',
 'ReneCryptoo', 'jrtradin', 'Fx_Chandrika', 'CryptowaveCycle', 'TradingAnalytix', 'sellingalpha', 'alma18499', 'cheatcodes28', 'RJMtweets11', 'JballSv', 'BullDanish', 'Doctor_Chart', 'TSB_US0', 'JohnArcher11', 'Trekewl',
 'AlvaroPalominoo', 'King_Deevee', 'rafstack', 'Trendtrader06', 'Feeble_Minded_', 'ConnorFitzy', 'badger0102', 'AmillionTheWay', '_rcmarkets_', 'RhythmicAnalyst', 'FedInsiders', 'LaudPrashant', 'ImminentSea', 'mei_rei_', 'lunchboxalerts',
 'I_Am_B3', 'traderyerrt', 'cryptomind900', 'Sean_Ottawa', 'AminAssamo', 'AlexKentUK', 'SignalPullback', 'Londonman888', 'SolnetAM', 'TradeBanditLive', 'aaryan_112', 'neilksethi', 'RCthe007', 'unearthed2023', 'CoinflipperA',
 'MCquant_res', 'smv_alexander', 'CRUDEOIL231', 'UglyOldFr0g', 'Picasso_Trades', 'DTrader2019', 'RandomGalic', '0RN0IR', 'spx100club', 'Frimmle', '71macintosh', 'Trader_hardi', 'ViruPandey81', 'MacDBollinger', 'DrDrends',
 'Mujahid94316092', 'barometerca', 'ben_crypto27', 'The_DGen', 'FadeMeIfYouCan', 'flowstate_trade', 'RB_Tradingltd', 'vikranth__reddy', 'YouCannotTrace', 'priceactiongann', 'Boast71', 'DanielZippel', 'pinerylakegroup', 'Trader_Lovex055', 'AakashT0711',
 'hoffip01', 'dp_theboss', 'NathX2001', 'Capitaldhan', 'ecalabro5', 'lsestockpicker', 'akutidaktahu1', 'r289567', 'us5005com', '_kevinkirk', 'cryptokingping7', 'asxpeasant', '_Stoner_Stuff', 'HTrisme', 'X_BlueFin',
 'BRADBRADLEYTTV', 'InvestmentBites', 'xmobitz', 'velmuruganms', 'itsthechuck', 'LUDLONIC_TRADES', 'Kai_Charts', 'FBSadmi90', 'vsz01k3ogf5h', 'istalkstock', 'belegendarycap', 'spxbot', 'runningprofits', 'cdnstocktrader', 'Trader00004',
 'MobileAndApps', '_dburrows', 'OptiScript', 'AdvanceStockT', 'iamericwhite', 'niqomaniac', 'Sayyed_Asma_1', 'NumberOfWealth', 'YinYangAlgo', 'JGtradingcycles', 'URTradingCoder', 'token_ventures', 'JovinSKN', 'jacharakis', 'officialce1este',
 'Mrtrader0', 'DomHexCrypto', 'Mohit_Gupta16', 'TCTALKSYT', 'EricBitetto', 'the_gorilla_22', 'pyradog', 'CryptoZee_CZ', 'NerdTriesBest', 'daypriest', 'EPointCapital', 'Enigmas1Son', 'criptoedbtc', 'sofiaelpidagapi', 'BitcoinLTDA',
 'tradomica', 'uptrader', 'sanmiadeagbo', 'abhilives', 'spxthh', 'Mahdi_m_ict', 'VolValkyrie', 'BUSINESSFIRSTAM', 'fintechsfi', 'mrjackpro', 'Candelstickoff', 'TRWofmarkets', 'sharkforex_', 'greateaglecap', 'JusticePem31204',
 'Snip3rz0', 'eren9107', 'fx_talisman', 'Only_Crypto_X', 'AmbarnathD44454', 'MaxTern156', 'just_a_nobody_c', 'judo_jus', 'MATHEW14735693', 'SignalsPress', 'SP500Surfer', 'story__horse', 'JonTalksFX', 'LRGWealthAdvsrs', 'KaKa_VD13',
 'geopoliticsexp', 'ElliotFxx', 'CryptoTouns', 'Lino_trades', 'ictaddy', 'deltavadertrade', 'deltavadertrada', 'ChrisAI_Hub', 'Texman_nvm', 'FuturesTra67331', 'Dream_it84', 'CmC_Marketer47', 'STIFEL_CORP10', 'JoeTradez67745', 'DrSusanCalvin_1',
 'ImBaak_', 'trqdernickfx', 'YellowLineLife', 'Sleman141218', 'trader_TP11', 'boengmars', 'fxpipcollector', 'BlackbullAD', 'BullBearTrading', 'wonderful_sandy', 'ronisworldwide', 'giapduclong', 'SensaiBR__btc', 'theseventhneo', 'mantraxer',
 '_sachin_goyal', 'StratsLabs', 'CryptoAnbu_', 'tradereliez4r', 'JoseRicaurteJ', 'Akdnzkutay', 'HermanTrades', 'yashutmani', 'cwEmporium1', 'AlexFridd', 'SosyalBorsaci3', 'wowtradingWT', 'thewooofwallst', 'OxSecurities', 'giorgio1593',
 'cryptonut16', 'TheBathymetric', 'JunaidKhan29900', 'MaxMolter1902', '_DesiEconomist', 'CM_Anton_', 'badpienut', 'Teimi_7', 'treidareviver', 'melardev', 'alekseywave', 'tycoonitos', 'thejayrobbins', 'SalvyRE', 'scamg0at',
 'Hellex_io', 'RobTradingICT', 'mobylond', 'Unique00unique', 'BTCStreetBet', 'techmarketcycle', 'BajaPips', 'RUSSHANE_RISE', 'JMCLoongee', 'HUGESKY852', 'OneJuanWon1', '0xethermatt', 'MikeFairbournCS', 'octo_swap', 'ARyan7527',
 'emmabrunsonn', 'InvestingInMy30', 'cryptonikkoid', 'Traderjnb', 'tmourad76', 'Angelface_76', 'ISPANDA6466', 'MerTradesC', 'mac_usama3', 'brainwavesfx', 'Scalperjo', 'Gaurav_Red', 'decentralized_1', 'JatinXxiv', 'saniaandreas',
 'finance_sniper', 'ovocharts_', 'xa_dula', 'trendxinc', 'PjRisk', 'capitalize87', 'Cashcows15072', 'Dayax999', 'MrsEvaMiller', 'AssortedFoods', 'BlackLevin1979', 'Amed894515', 'fsmfinance', 'LungerN', 'jacobotweetsnow',
 'undercoverBobo', 'JrBlackTrade', 'Mmajani1', 'silenceisduck', 'Shan_xbt', 'T_Harth', 'strangerranch', 'fvareladv', 'Jabroni_16', 'btcinsiderr', 'EdTradingfx', 'osenter16', 'Thonayan99', 'Dxejrsol', 'malek99__',
 'BitRwithoutBTC', 'JPStanleyX', 'bunty6400', 'APDST2017', 'SpecuVisionary', 'ExchangePlaza1', 'Tradengineer_MJ', 'akayy713', 'LakshuAg', 'KiaHashemi1', '_WeeklyCharts', 'ST__SNOOPY', 'realjoshbell', 'ChartNerdTA', 'AI_Trader_72',
 'fx_margin_call', 'moetradn', 'DomarkasMD', 'Zackery_SISU', 'montaser1050', '_Vivek_Malik', 'PerfectSelectn', 'GuySinful', 'Palmieri888', 'Ic3WND', 'anarchokapital2', 'thesminemverse', 'nakamoto_prime', 'KrystianLaskow1', 'PortfolioParrot',
 'Gorilla_9797', 'RoBoCo_1', 'balakoteswar', 'Phenomene509', 'NFTConciergeDoc', 'SaroshQ2022', 'Sanju_Lakshya', 'Dave_Starfeld', 'Capt4in007', 'FoxproCanning', 'PorasTiwari2', 'hubrishunter', 'mehmetsahkaraha', 'Sluicebrother', 'Sharketo_',
 'anil_6203', 'TradingParrot', '0xAndr0meda', 'j_mccague', 'WallStreetRule', 'Pips_Exchange', 'AtomicTraderJ', 'investorean', 'Pedr0FS', 'Sam23709', 'spx6900', 'skinnymoonhuntr', 'R4V1_85', 'FahdYK', 'jay_kamadiya',
 'Nishant_Bliss', 'AnonymousAlphaa', 'PitTrading', 'Louie_the_Duck', 'Shubhankan007', 'PenkeTrading', 'mrcabron999', 'mi6lethaltool', 'Ebadian_eth', 'MMMTECHNICALS', 'bagelfish2', 'skywalker_nbn', 'firmamentfox', 'GGreg493', 'JseFred',
 'AchieveLeague', 'Aslanomic', 'adembabo09', 'GeneGoldman', 'amirbennatan', 'ivanitrust', 'Paolisimas', 'nigelfrithfx', 'PickleBiit', 'ctincristian', 'Saad185142', 'INDcryptolawyer', 'GarciaRepetto', 'werethefugawi', 'GabrielBrinzan',
 'forexgoldtrades', 'someoutof_none', 'GregVentura', 'JeffMooreTM', 'marbel2019', 'TKTweets_', 'FabioBusinesss', 'KryptoOnTheMove', 'ZirbenTrader', 'CM_ChrisAk', 'How2BuyBiTCoinz', 'onehellofarun', '9Chriz', 'SunilRe89392848', 'BTDTrades',
 'realhus2', 'ManiarMeta', 'YareemaFx', 'Cotto', 'arwa_zaman', 'ajmera_aadish', '1AmaniQueen1', 'ct_omer', 'TraderFoxyYT', 'mongooseCA', 'TheTradeKnack', 'InTheFlowMR', '125kMarine', 'BraVoCycles', 'trading_gene',
 'options_trd', 'SeanTheNoob', 'abigbrain', 'EdamTrading', 'sapientseraphim', 'kenneth69171543', 'damantis_de', 'Trader_Nebula', 'reganteague', 'coelhopepito', 'albqamy20', '1big_bull', 'saudsaad2012', 'Zainacurlewis', 'F28_Olivia',
 'Labuya5', 'Donjim95', 'shri_1010', 'thomas_tilney2', 'LuckyLuke369', 'SplashIndicator', 'Tradingdengdfx', 'enlightenone369', 'thebtcrebel', 'realhus2_', 'EvanderThane', 'Anuj1e', 'ngenteod', 'SyloTrade', 'WStreetPanther',
 'TheChartKnight', 'whalesonly1', 'finn__crypto', 'TouchWood0X', 'pmptrading', 'elliottwavespot', 'I_am_the_GET', 'BlessyPaulFx', 'Deadpoolinvests', 'HedgeBhai', 'tradingwizard01', 'carati_claudio', 'AayushAgarwalx', 'TeamProfits', 'JesusMorenoM41',
 'LucasMe30', 'AfterDark_999v2', 'bitratepro', 'julie_wade', 'rdharthefirst', 'Rising__22', 'AndreArevalo_09', 'Imran1248751', 'exocientist', 'CryptoFido', 'B2F_Investing', 'AhahdbSbdb32954', 'eigdub1', 'TheWealthVriksh', 'TycoonTrader_In',
 'Trader__Sosa', 'price_xbt', 'Eruditehooman', 'Stocktrader127', 'MrWWolfe', 'adeleketaiwo20', 'I_Mapping', 'GreekTrader90', 'TanukiTrade', 'HsgSkinnyG', 'mattiakabtc', 'NYBD____', 'G_BullCitY919', 'moboslim', 'AzGRID79',
 'CryptoEx_Bablu', 'NFT_Garage_', 'mrjones2020', 'AzamiArsal27923', 'Ramiknfr', 'lakhanhathi', 'Sunil90666519', 'NRiskNFun', 'stocks_profile', 'thesoumyoroy', 'Mtrading0', 'Shawncito830', 'enthuharsh', 'tncckn', 'SwingKing720',
 'h69966', 'wolfslair_io', 'Cryptorphic1', 'ShahryarTrades', 'ud4trade', 'ichiandscratchy', 'CoherentMoney', 's0ulBr0ther', 'LaeeqHumam', 'alessiorastani', '79Traders', 'LiberalWokeMind', 'DrChijox', 'SwapnilDPalande', 'equity_edg3',
 'ELIRANSHORT', 'marketgem', 'PK_Fund', 'ZephyrBoy_', 'Mehdighiasi_', 'apurvansheth', 'thefuturesnet', 'Lemogang_Leburu', 'PiotrMacro', 'ThePropDesk', 'baniyaboi', 'FoxWolfCapital', 'Cr4zy_Chef', 'jfozak', 'TORtrading',
 'sandyyindia', 'Saurabh22683360', 'cryptophilosop3', 'WealthtraderX', 'Nilex_Trader199', 'algopulse_R', 'notbudfox', 'trend57k', 'SamariSamson', 'kakrypto', 'ImmanuelZa16976', 'realgann3', 'D_Builder95', 'alphastock8086', 'aynirealtor',
 'FrogmanCrypto', 'SPXistheGenie', 'JazzHands888', 'veritasPLANET', 'WhoIsDarth', 'CryptoOtia', 'TheTradingEngin', 'DiPavTrade', 'ManthanResearch', 'shahzainrahoo99', 'ImComingDubai', 'Analyst__S7', 'wham_70', 'TAKE_PROFIT_1', 'manki_b',
 'PALDEB4', 'fx_saif10', 'alltcoinera', 'stockmanreal', 'ShitLaurenSHays', 'Sterling_maker', 'JessupWealth', 'LitixApp', 'cashingoutbands', 'WmHasif', 'spetsnaz_3', 'vallieres_david', 'Trippyhendrix_', 'Capt_Alsh', 'mtrader_',
 'Bhavvikkakkaa', 'mannansheikh_', 'GoldhawkInvest1', 'NFTandNFT1', 'justwowhappy', 'SuperCycleBear', 'DovahkinThuum', 'technicalslife', 'justinmmathews', 'maskedtraderrai', 'extremecapital', 'Wyckoff_Insider', '0xKiriKev', 'Ponzituccari', 'trader_aka07',
 'cryptosafari_', 'NutsVNKN', 'onelifecrypto', 'jamesjasmy', 'SelzTrades', 'Cryptoforidn', 'YDB_Trades', 'thesambrunson', 'ZenTrader_7', 'Unicorn_Circle', 'En_Nazer', 'KapilBh11016088', 'DTConsultations', 'TTXAIAnalyst', 'janilgraphics',
 'JuanCarlosJuBa', 'moneyfoxer', 'SFSFrancisco', 'DepecheGST', 'YYDSxjm', 'fxgoldanalysis', 'GrowFinancially', 'IamOzed_', 'Laughing_GG', 'Angievc11', 'ferenc__xyz', 'DocLevente', 'tf_NQES', 'JohnnySignals', 'aped_into',
 'super_mari82692', 'MattTGarraway', 'bitcoin63925', 'silver_3ull', 'Fxtradesignal0', 'CryptoLord100x', 'TradePro16', 'edgarhxss', 'R1venDev', 'TigerTraderFX1', 'materagian', 'FutureMan_Quant', 'Mr_Josh_001', 'forexcomtr', 'SpeedbotT',
 'lan_izz', '0xGrizman', 'mohx911', 'Tradebeta2', '2035biter', 'OhakaV15118', 'cry_bebi', 'PlanSoftG', 'AirAndyBets', 'ethanxMPx', 'GutShotPorkChop', 'antistupidity28', 'Billy_the_whale', 'BRRRR_BTC', 'PiusPioneer',
 'JejeomolaraG', 'Ayo146645', 'Gemini525985', 'QuennarraB02', 'dansquare06', 'degenfinanceonx', 'shrimanRV', 'Rymd_Li', 'subramanyakulk5', 'optionalitie', 'MaxMilko', 'entasiBot', 'baki0i', 'active_fx1512', 'Sarah_GreenOk',
 '_B00giecrypt', 'asiwajuruger01', 'PIUSLORD156737', 'RaidersPho42635', 'Kapi0100', 'TalkingMCI', 'jeje_lara', 'PiusCryptoVibes', 'crypt_GURU_', 'dunsin_crypto', 'Cryptomeni_5', '21teekul', 'harmen13', 'BorisCrypt61737', 'SR_guru_',
 'QuennarraB3', 'crypto_guru_111', 'B00giecrypt_', 'CryptoIssacc79', 'PiusCryptoPro', 'Derryboi465241', 'kizzdaniel24', 'dave85143', 'Larryj2020', 'Laragrace247', 'purplesa_ad8', 'GraceLarry37861', 'BorisFx1739', 'PiusCryptoZone', '2Based_6900',
 'sv_j8', 'ed1_eth', 'matt_tsoi', 'xekotrade', 'sailortrades', 'LegendAROJ', 'BORIS1846693049', 'RealDealSam', 'Brapdemol', 'FanaxShett23897', 'larryj90071', 'sub_seven7', 'Guru_FX_1', 'Nwa_mummy001', 'Derryboi493232',
 'reedickuloux', 'Borris998117', 'Cryptomeni_7', 'ImBoris334441', 'QuennarraB5', 'QuennarraB01', 'harveyspektar', 'PPius074', 'BoneboyJ', 'ShitMyChartSays', 'alpay_cc', 'tonyzipparro', 'youraveragejeet', 'MewingOg', 'PressedSolution',
 'keplihomshi', 'Crypt00_Gem', 'WarriorX61004', 'Dyma_Data', 'YetAnotherSE', 'omolara_je71149', 'omooola45', 'Uchuydemplon', 'PiusCrypFanatic', 'Cryptomeni_1', 'erod_eth', 'Tariff_Ai', 'EliasHad', 'AntoineAlves7', 'SaylorFink',
 'AoTpokerplayer', 'FxSignal729724', 'AthBoris73916', 'Mighty_safe730', 'bossyycrypto', 'nguyenuy1990tn', 'Derryboi416710', 'bnxnfat', 'cryptomeni_6', 'Cookie_Calls', 'CC_Crypto_', 'vintAge__AF', 'Derryboi494407', 'QuennarraB4', 'Quennarra15',
 'emanuele_zeta', 'olaomolara44', 'Blueice27o', 'Ejembiox', 'talentedkid0408', 'Lx_cryptonite', 'G3mini001', 'ka_tty_9', 'MegCryptic', 'SolSPX', 'forexpips111', 'SamCrypt140', 'kapita006', 'KINGKOBAETH', 'QuennarraB6',
 'coolranchkid1', 'Quennarra11', 'picassodeek', 'Stew_EV', 'LONGLGG', 'JejeomolaraD', 'Bond_Safe600', 'Derryboi496464', 'Fukogu', 'PurpleUniFart', 'Godzylaaa', 'dorner_simon', 'TopCalla', 'TheStarBTC', 'niksak888',
 '1V1onlyy', 'cryptomeni_D', 'battousai1987', 'Anuoluwapo7654', '_vint_Age', 'Safewant15_Post', 'PiusCryptoNerd', 'four4cousins', 'michaeljack1946', 'QuennarraB8', 'MGid101010', 'iscrypt234289', 'margid_2', 'Dion85022859', 'Mix_Safe8009',
 'sa_to_shi7', 'iscrypt219021', 'Mr_DragoNero', 'Akshay135768', 'gem_dolphin', 'learning_sharks', 'Risological', 'US30VIPTRADES', 'NBihanon', 'TheKNANC', 'BTCboris517443', 'halder_nabarun', 'Vhilly0812Gt', 'Bor1178741', 'quennarra50',
 'convoscation', 'QuennarraB1', 'abiodun11644936', 'cryptomeni_B', 'GEMINI595681', 'crypto_guru_SR', 'pykecreek', 'CryptoParodykid', 'CryptoB86458', 'PiusInLarge', 'Jammiiee001', 'KryptCaptain', 'HardewalePeter', 'LegendaryAROj08', 'kimbarry78',
 'FX_GURU_2', 'HaghighatKambiz', 'BamzyCrp3462771', 'briggsbelema73', 'SameSafe16566', 'Quennarra0', 'iamkomikaze', 'tradeanalyzert1', 'Thinkwell100', 'Urbi_inv', 'samad31802', 'derryboi462832', 'Quennarra25', 'lenin_pitan', 'BrightNwafor3',
 'ArinNirban67582', 'Twenty3H', 'SwaamdwnBaro', 'QuennarraB2', 'NirojanYog78222', 'KapitanJayy', 'iscrypt290681', 'Fe_Crypto2100', 'Jennie000000000', 'PLORD005', 'pheonixuyo', 'CryptoCurb', 'Dilltor6789', 'aymericbimont', 'madelin_crypto',
 'WarrenBuffeNFT', 'DesMahesa', 'LegendaryAROJ00', 'blaqbonez36', 'igweemmax', 'SHU_RI_KENz', 'QuennarraB7', 'habby_safe', 'PiusCryptoInsig', 'Sumit_24', 'familiar_stray', 'Drac0logic', 'mntyetti', 'PyroPete_', 'Analyst_Rashik',
 'B_Luv618', 'CryptoHeadJesus', 'MagnusCrypto1', 'Ricardo_Marenco', '0xSolKeeper', 'taha_trades', 'satosheet', 'KMTrading_SMC', 'RusseRR09', 'enlightenone222', 'AymanAlsaab', 'singh_atinder', 'freshnessmag', 'Traders_LIQ', 'RS21_trader',
 'Qapitalx', 'Hakaishin_FX', 'VentsiIliev', 'AlgoChirp', 'HeWhoHuntsGems', 'Ernieefung', 'ChartCinema', 'CurioseoRemix', 'ovrclockedjesus', 'loopstate', 'CosmicAlchemyHQ', 'VietcryptoZIL', 'ChesterBlo97724', 'ORBMiguel', 'No_man_one',
 'robert61652', 'Noobieboyy', 'dawievdwest225', 'rakuten130511', 'TENET1st', 'iiiiibelieve', 'MGustaso24', 'Star_Quiver', 'Equinox154417', 'QuantFinDev', 'the95trader', '4ltered4lt', 'damibillions_', 'forlorn737', 'forlorn375',
 'pelele135950', 'silk_sammy', 'SabrinaTay3746', 'Mysterytrader11', 'maddox_darren', 'Bhavbhagwanche0', 'OneRoyalEN', 'InvestmentFella', 'GoldenZ_prime', 'MAGAMandate', 'Navi19649035895', 'PURE_INDICATOR', 'NIPsG0Jpfu8qoic', 'shiba_Fi', 'Picar_00',
 'EPlaysxxekxxek', 'McinnesAvery', 'Mr_Introflirt', 'Chef_x_eth', 'TradosExpertos', '0xsaboo', 'broccoli_tech', 'Super_90000', 'MulgetaAbrha', 'electronfarmer3', 'OptionSigmaApp', 'Francesc_Forex', 'JaboMaga', 'd3rsww', 'officialzacsina',
 'pletar_', 'Vekido_Trade', 'Sistaf4ever', 'shamiul293', 'GlennHodI', 'amital13', 's_aleh1111', 'georgegarner89', 'ethcryptophd', 'iDealer911', 'Allison_0023', 'TradestorYash', 'Bondftm', 'AdamsAkintayo', 'Dam_Dam002',
 'tylan16wallace', 'cryptoempire01', 'cryptoblack36', 'Cryptoblack30', 'cryptoblack37', 'cryptoblack31', 'P_A_Bronson', 'TraderDemircan', 'Crypto5Gs', 'YhungJamie', 'Earnings4sight', 'BiohackingBasic', 'whyte_cryp14075', 'MrCashSebi', 'IhabAhm74184978',
 'Moi_Mathilda', 'cryptoblack38', 'cryptoblack55', 'Cryptoblack42', 'cryptoblack48', 'pushp2771', 'cryptoblack46', 'Daudibrah22', 'legendary7aroj', 'whyte_cryp34389', 'Cryptoblack33', '_DecentralizedT', 'SimonChegeW', 'cryptoempire79', 'Bamiseyitan',
 'AustinCryp85444', 'whyte_cryp88576', 'quitecharlotte', 'cryptoblack29', 'cryptoblack28', 'cryptoblack51', 'rabada16774', 'cryptoblack49', 'DeeTesla', 'JavanJavandegr8', 'YhungJJJ', 'cryptoblack44', 'whyte_cryp43515', 'cryptoblack32', 'whyte_cryp84565',
 'cryptoblack40', 'OluwaseunLokosu', 'Newtown153', 'KryptoKapt_', 'Zenox_Prime5', 'WhyRe39710', 'DogeSpaceXX', 'muratevrenergun', 'Whole_wit', 'mad_lord_punt', 'Lynqverse', 'GannForecasts', 'alnasr_97_7', 'Legendary5aroj', 'VladyslavKoptev',
 'cryptoblack59', 'ArunaShaibu', 'EvilVr0unD', 'SakinaAbdu36311', 'Cryptoblack34', 'cryptoblack50', '500SUI', 'moss_ernie', 'iAmitKumar', 'Steveast11', 'make_macho_cry', 'JCruzInvestor', 'zenox_prime2030', 'M3esTro', 'FavourIyagin',
 'Bamcrypt', 'Xenael201', 'go4zu', 'TomarManinder', 'jieyaoSFD', 'cryptoblack52', '5GReady', 'tomlvs1', 'supremotg', 'elitecharting', 'victornapinvest', 'Forex_expernick', 'goldsignallive', 'ZoyaAnalyst', 'marketwhalez',
 'XVenkam', 'Slowdrip123', 'xauusd_ana', 'finnjclancy', 'TheMeowingLion', 'Quantum_Dine', 'AlfuraijA', 'shsajib', 'RalphHumphrey', 'Spxgigaapu', 'stefanvanersand', 'ThatKidNumber7', 'GoldenOxen', 'pnievesnava', 'FswPort',
 '10_J_0', 'Banana_Fund', 'Dimitris_anemos', '_andy731', 'Tradinvestlysis', 'akila_ramses', 'Dahaky', 'GregDayTrading', 'QuantumLabTech7', 'TOptionStrategy', 'Libermanyesitme', 'Vol_Pokemon', 'Dan23964585', 'CashRising', 'MatrixTrade_',
 'r3marqable', 'StephenC2910', 'AndresAcostaE', 'nothermodel', 'PT_FinTechen', 'nori_krienbuehl', 'HB77178568', 'skoonzoon', 'abdulmohsen_al3', 'kayseeCT', 'KarlinskiD', 'fortunemadu1', 'from_memestreet', 'IrinaBees', 'Rehab0ElHelw',
 'Gurpreetable', 'CMattDye', 'utrada_global', 'OmarAbdelsamea9', 'borsakitaplari', '_legallyhere', 'AvivArazi', 'RadoslawBodys', 'imworkincrypto', 'MikeoTrenbolone', 'Signal_Scoop', 'Gb_crypt0X', 'marsrides', 'aakankshalovely', 'Blockchain1013',
 'domenicola85491', 'sa563753', 'HJrnjf4337', 'ParagSanghvi9', 'trading_RSI', 'skubox555', 'FPGAengr', 'kurtsmock', 'myInvestingMuse', 'gainify_io', 'fatihkhanzada', 'PriceReaderr', 'anonymousXPF', 'rahaf90185', 'Crypto_Sniper__',
 'MattySP500', 'mkztrend', 'MERTOZKAY', 'mmmcharting', 'The_Chart_Degen', 'belkhayate', 'scherfcom', 'prince3833', 'SYNDICATE369', '333blacksea', 'PippinCrazee', 'Srosh_Mayi', 'ArcaneusLord', 'x46gill', 'fugasok',
 'LeonidasPanagi2', '9Muratayhan', 'wallstreetgibs', 'esoteric_jayz', 'DipFinding', 'el2222_H', 'JulyAeternum', 'Crypto_Xleaks', 'CryptonianZee', 'grvcapital22', 'PnFChart1986', 'crypthal', 'rditrych', 'low_cap41279', 'waldalhas1',
 'artimemes', 'StanleyCrypto_1', 'sensei_kong', 'TradingTarzan', 'CelaEndrit', 'BuffaloNYMonkey', 'P_Charlie_88', 'MemeseusMaximus', 'riskreaper001', 'goel_siddharth', 'ErickEliot18', '5TONEOFFICIAL', 'DhandhaPaani', 'That_sHowUFeel', 'milko52250068',
 'bokemtrader', 'Soran989', 'ChiTown_A', 'ChartTarangul', 'AlmuhandesKSA', 'MPBHH', 'OmarAlkhazraji6', 'P85Crypto', 'AeonOrmu', 'Jus_Trades', 'BATM017', 'RicardoVidal899', 'TrendsharksLive', 'AhoNiranjana'
]


# Set Up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# To run without opening a browser window, uncomment the following line:
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# List to store results
data = []

for username in usernames:
    try:
        # Open the profile page
        driver.get(f'https://x.com/{username}')
        driver.implicitly_wait(10)  # Wait for elements to load

        # Locate the follower count using XPath
        follower_count_element = driver.find_element(By.XPATH, '//a[contains(@href,"followers")]/span[1]/span[1]')
        follower_count = follower_count_element.text

        print(f'{username} has {follower_count} followers.')
        data.append([username, follower_count])

    except Exception as e:
        print(f"Could not retrieve follower count for {username}: {e}")
        data.append([username, "Error"])

# Close the browser
driver.quit()

# Save data to an Excel file
df = pd.DataFrame(data, columns=["Username", "Follower Count"])
df.to_excel("C:/Users/sebgu/OneDrive/Skrivebord/xscraper/scraperfolder/x_follower_counts40.xlsx", index=False)

print("Scraping completed.")
