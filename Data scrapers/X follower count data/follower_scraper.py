import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# List of 10 username lists to scrape
usernames_list =[['sachinksd1', 'MassyMarket', 'abshrk7', 'tmacktrading', 'TicksOfTheTrade', 'matthew_miskin', 'John_Papadak', 'FredKanyama', 'FXCM_MarketData', 'fuckeduptrader', 'Etoro_Airwalk86', 'BlockchainStox', 'Kunalyv', 'SilviaBellrock', 
'TradeStonknCoin', 'KretzThomas', 'SteadyBerserk', 'PatrickHill1677', 'DonksIn', 'NecoKronos', 'StocksbyPrakhar', 'nietgek', 'atul_vernekar', 'trader_ska', 'MikeWShell', 'KingJulianIAm', '_ttk100_', 'MonkeyDD21', '_dogwalk', 'TheMarketFlows', 
'StockBondTrader', 'Akhil70526854', 'Rakz_27', 'Bitcoin__Banks', 'Kartalkocan', 'Jack_KinComm', 'tumi_VTMarkets', '2021Skg', 'janikibichi', 'BreakingFreeYT', 'KaiSmarket', 'steko170981', 'Mkts_Compass', 'purvirakesh', 'BlockchainTrad', 'Rock228VIX', 
'RedRockCapital', 'Kirtheebane', 'karan_jhamnani', 'Woo_Minkyu', 'karthikb030', 'Niftyspeakloud', 'TheakingAlpha', 'BtcAkira', 'BilalNasirKhanI', 'kingpazn', 'thesanjeevk', 'MerkTrades', 'VikashR96702439', 'Acko8686', 'KshitizBisht', 'ShikhaS18487700', 
'danknemasis', 'akhil1206', 'CryptoKryptid', 'Komorebi_Frisii', 'kevincrates_', 'cryptowhitewalk', '_KrazyA', 'TanukiBTC', 'SkipperTrends', 'jeffkilburg', 'checkerdog87', 'be_livermoore', 'LinkSpartan80', 'ErikSteiner8', 'flyingstocksman', 'Nick_Geeks', 
'StrikingEagle77', 'lawlessyak', 'ozkanozkaynak', 'KansCapital', 'redknighttrader', 'aksh_2018', 'therealkuzybro', 'CMCMarketsAusNZ', 'AkshayChinchal4', 'ALEKOSVENERIS', 'HSiemienczuk', 'Souvik025', 'MajidMirzakazem', 'Hayekjn', 'KAProductions', 'MoneyMa71574583', 
'PhilipJagd', '6sixxk', 'tradingwick_', 'Rookie03061', 'KaziveG', 'stockolog'],
['omarfakhouri', 'rocketmanwealth', 'Market8B', 'Trading__book', 'KnovaWave', 'kworsley81', 'Baskitchbrah', '_K_P_W_', 'danbakalarz', 'CHARTISKING', 'KhanPhelanTrade', 'TheGenNetwork', 'hkenanturk', 'kuurakarahka', '401kRIA', 
'bekind20214', 'Harveyoakville', 'fxtrapking', 'ichimokudoc', 'tradernakamura', 'WVenketas', 'FxMoUK', 'i_am_jackis', 'KhalidSaifuddin', 'Kamen_dushi', 'heknowscrypto', 'roman_pvlk', 'SwingTradeNick', 'imchrischuks', 'KING_sez', 
'kimmyungjung', 'TimerofMarkets', 'PhinkTrade', 'MarcosUk1', 'Lukes_Trades', 'WeekendInvestng', 'NikiNikitaLiana', 'defi_joker', 'Investinmarket1', 'jakub06957091', 'mandageakash', 'Bankit63', 'Grow_Staok', 'unko_coin', 'TukkaNomist', 
'Kreed_Trades', 'BAMBAMTHECHONK', 'youknowwho_Men', 'MarketEagles', 'oleusiek', 'PiotrRosik', 'CompareBroker1', 'gag_kal', 'Flourish_Venkat', 'SikanderRaza20', 'stockbot_dk', 'alittleabtmkt', 'poyrazserok', 'kingmoontrading', 'Sulkhan', 
'mvrzfrmsky', '_Viking_Trades_', 'RVMarkham', 'creatvemike', 'BinkyHole69', 'stokesbaytrader', 'snKdestruktah', 'CryptoWalker46', 'MaheshKh64', 'FGEJonker', 'ArtunBekar', 'Sea2Sky_Trader', 'FarukBB44', 'Maverickov', 'Kryptographics1', 
'TheBullBearMkt', 'MarketsJunkie', 'tradeshock', 'StockmoneyL', 'vojtek_milan', 'Viktokeshi', 'BlackTrading_', 'SparkleandTrade', 'Mark_Astrology', 'anillgoker', 'BlackLionTradi2', 'IlyaSpivak', 'MWhalekiller', 'paragkapdi', 'IchimokuCorner', 
'Kriz_c369', 'AskToRahulSingh', 'knopers_k', 'pkay2402', 'chinmaygnayak', 'HoldwithPriyank', 'sanketrs11', 'henrikrowley', 'shankx', 'KAR__Crypto'],
['SlickJedi', 'X_KRU83', 'Likwid_Finance', 'sorkenma10', 'GurkhaTrades', 'accapitalmarket', 'RealCryptoArka', 'cryptomonk108', 'kshitizkapoor_', 'David_theLawyer', 'gkartikey25', 'glebowski00', 'traderrocko', 'Kim_Sag_87', 'Kofi0243', 'PakNFT', 
'Scand_markets', 'marketoccultat1', '0x10o1', 'patnrekognishn', 'TheQuantMonkey', 'drinkeatw', 'mrtakeprofit_', 'LiquidWicks', 'MP4FMPK', 'ehtesham_a_khan', 'JayneshKasliwal', 'TakeProfitFX1', 'ravikumar753951', 'AdnanKh21678333', 'stonkswhale', 
'stawkgawd', 'kaabar_sofien', 'khurramja', 'calHAMitykelso', 'Worktocreate', 'discretekestrel', 'Fly_divyansh320', 'wiki_2030', 'KukiRanjan', 'anuj_kapur', 'vertinski', 'kummy', 'Hamiltonkatie33', 'SBK_analysis', 'Mck60073231', 'MakerOption', 
'kriptodok', 'wickhunterr', 'cryptoBreakClub', 'MHiesboeck', '5Trakyali0', 'thekashifkhaid', 'onchainfarhan', 'mr_greenb4ck', 'ShivamKole7', 'Just_Jack9', 'kyledoops', 'A8_krunal', 'rpeker', 'TAwithMMk', 'Thre3_Bucks', 'JDUBAKAGOAT', 'WeSeekClarity', 
'NITINKML', 'MarcinooKrypto', 'erashok', 'akshyp15', 'HeikinCrypto', 'PointBlank_Algo', 'DanShkolnik', 'SquawkStreet', 'Kunal14_', 'CryptoFaibik', 'helmigka', 'stockinch', 'Stockjay123', 'LeverageMonkey', 'ashokmalik', 'astocks92', 'MalikAnas95', 
'arekdrozda', 'DarkNexusTrades', 'GregDeSatnick', 'WyckoffAnalysis', 'hunnitbandkris', 'maverickswift13', 'skyz_trades', 'JPodhorsky', 'ktastrologer', 'Fukuhedrons_eth', 'crypto_blok', '_Shikhar_Raj', 'NukeCapital', 'AccidentalBiker', 'yakzTA', 
'StockGodd', 'darksosis', 'kawsarxbt', 'bassel_doueik'],
['DavidSSKCapital', 'dkcrypto13', 'Adityaroypspk', 'brokendegen', 'rikhniyt2012', 'prabhukb1967', 'stevensbiker70', 'ElTrollski', 'KPNMusician', 'Farukb44', 'krshnkapoor', 'ErikaTaylor04', 'ManjunathKampa2', 'riskonandoff', 'stockswithparth', 
'ankursgarg', 'Psychometriks', 'GiriShankTrader', 'Claude_Klotz', 'Klarity', 'RkTrades112', 'KokoToast', 'jainikkhokhani', 'sglikescrypto', 'BullseyeFinUK', 'StephenKalil', 'naked_charts', 'Marios_Kouk', 'sinomark123', 'fusionz_kitchen', 
'brookskcbsradio', '0x_MarketMaker', 'inmuskwebelieve', 'DevakumarVinoth', 'CryptoONEAleks', 'MrTanakasan_X', 'Niharika_Ninja', 'crab_shank', 'TheRealAkshay_', 'ducknsurf', 'JoeyKnishPoker', 'NaharMayank', 'khajanchibabu', 'capitanwhatafak', 
'Kuba_Nosek', '_Kong_BTC', 'Mike__Math', 'marketsday', 'vaibhavkh15', 'Stonk_zaddy', 'CIAZEKACTrader', 'AkA_83', 'kalaiva_eth', 'dao_duck', 'DefibankFunds', 'Daxbreakfst', 'thehorsetrack', 'SilverInvestUK', 'techchartmark', 'market_drawer', 
'_k3no', 'darkfalcon50', 'KTGglobal', 'ekmanalaysay', 'KhosiRakoti', 'crushthemarket', 'NawafPK', 'kryptoniantrade', 'Bandit_Kyoto', 'optionsking430', 'JoSobkowicz', 'stockma34678955', 'Konang__', 'UsmanAK97', 'Prakash_1002', 'ManroMayank', 
'Swiftt100K', 'UKdaytrade', 'MonicaKory88', 'karim_aadib', 'DoctorStock1', 'ReubenEmore', 'BrankoBorkovic', 'Hassaankhaild', 'wstfvcker', 'CryptoKnee', 'John_Darkene', 'skibumtrading', 'mbookers', 'NishantKalaskar', 'VikingEW', 'PerksTrade', 
'WhiteOakFX', 'OnlyStonks81', 'Konstantinos_JP', 'rollingstonks', 'stocksetter', 'MironBanks', 'GOLDMANSAK', 'larenzoyoudork'],
['DKs_Research', 'PointBlank_Espa', 'KurzRamon00', 'JohanKirsten1', 'ashishkhatade', 'Mebhumika', 'MaskedFutures', 'StockEdge2022', 'Stockstudy8', 'ChikosanIL', 'traderRKK', 'Stocks_Mario', 'PRTKINGT', 'erc20_merlin', 'sameer_bhadekar', 'Chongwk5', 
'BlakeMillardCFA', 'blockchain1618', 'keeleytanfx', 'saikatislams', 'nks2708', 'The_Pitchfork', 'ThePickyTrader', 'greek_citizen', 'daddywarbuckxxx', 'thehawk_trader', '1kitapalintisi', 'zzlatko_zz', 'alicanengin35', 'marcin_dzialek', 'kathal_trader', 
'CryptoBlissKD', 'karaywrug', 'kennyhongkong', 'pkfanzine', 'chartspeak_P', 'GregTyminski', 'Keops01530770', 'Kev_Capital_TA', 'HukhoT', 'BullMarketGainz', '0xmrvik', 'RocketScreener', 'TradingRocket73', 'kogamicrypto', 'KACHHOT101', 'KeySpeculator', 
'0xTomK', 'TheNewGekko', 'KingShenoy', 'TheBakerFox', 'Sarj_KAC', 'LepkaStanislav', 'stinkyape69', 'crypto_twerk', '_walkershadow_', 'makeitjain_', 'savvymarkets', 'HenrikZeberg', 'KM69GG', 'shimongotrekt', 'FinlawSiko', 'KingOfTheScalps', 'Walo_nkuna8', 
'cube_markets', '123kriskwidrisk', 'MarketUpdate53', 'zoeparkerfx', 'vikinsa', 'joeblack0007', 'diwakar_solanki', 'Aktrader1991', 'KJCapital21', 'NestorKutsev', 'Galvanoski1', 'Kimpa_7', 'TigerBrokersAU', 'TigerBrokersNZ', 'Defi_Banker615', 'sidd_khemka', 
'sameehsukkari', 'investment_KD', 'sentinel_market', 'andy_blockspace', 'KareemFarid', 'u0ky70gmhi1l1zz', 'CryptoYak', 'officialcashki', 'KCTraders_pro', 'trading__kid', 'QuantStonks', 'Kacim_elliott', 'kgv10000', 'gl0rifiedmonkey', 'Barkworth17', 'descendinghawk', 
'The_Chartpunk', 'BlocksNThoughts', 'MickeymkMickey', 'MoonCake1738'],
['ktrue_', 'InvestmentDk', 'divyakhanna97', 'ashleybrooks05', 'B_Mallinckrodt', 'Warhawk1503', 'Nicksevers0252', 'killerpandapa', 'RookietraderAR', 'KingKotee', 'BhavikBitcoin', 'svinod_kumar', 'Abinandhk1', '_kobmanden_', 'moonvikings', 'cyclonehawk', 
'MarketMobsterUK', 'GauravThakare50', 'IbrahimKabbara0', 'market_surfers', 'Kiing__Bryce', 'fkmarketz', 'stockzones_144', 'tookanarrow', 'jacksonpo7', 'BaghdaliHakim', 'Carolinakeith_1', 'Financial_mrkts', 'backwoodprince', 'metaMonkey__', 'serkasu', 
'MarketsHistory', '69STONK', 'OGSlaki', 'GrasshopperNick', 'PirateKey', 'Honeystocks1', 'codexabcd', 'tetra_kev', 'TakePro65931263', 'SpikeShotCrypto', 'quidikatoken', 'Willy_kamaz', 'mikael_aune', '_Captain_Canuck', 'MBM786kr', 'brokefuk222', 'StockXcapital', 
'Stockkse100', 'SnarkyTrader', 'conkers3', 'FxPro_EU_UK', 'StopLossKingg', 'VezauskisArturs', 'EarningWithFk', 'ask_DSR', 'Kay_B89', 'usmankhan002', '_crkingdom', 'JacobLcmarkets', 'EjikeOdeh', 'blockchainmash', 'MiklosDenkler', 'KelaKalpesh', 'big_sky_crypto', 
'MayankManro', 'CryptoShylock', 'AtobucksK', 'globalmarketrep', 'whunterknight', 'Rollarockaa', 'TroyArthurK', 'LauriHalikka', 'AskCryptoWealth', 'RamakanthBalda1', 'iamtanmaykh', 'duketinkertown', 'NakedTrader3', 'Real_punuking', 'Imkingjon', 'Polkachri', 
'sanskarpoddar', 'teamblacknox', 'Share_Talk', 'ZaksTradersCafe', 'fredrikchrist', 'HasanKhattab1', 'marslan1923', 'ichibroski', 'Zorak_Gm', 'Shareknight', 'KhivrajNaresh', 'findgreatstocks', 'BInkeles', 'K9frog', 'ValueTheMarkets', 'szabolackomacko', 
'kakiphilosopher', 'TKCI_DannyG', 'iammoklasur'],
['crypto_kl', 't_ftalk', 'cryptocookiee', 'Omkarp1528', 'StuckasPM', 'RoyalHappyMan', 'Twannsko38', 'Think_w_Bookmap', 'kbbothra', 'WARMsparks', 'thebracketsco', 'Madhav_kejriwal', 'SirMoh_ke', 'Bryptococcus', 'LykkeTrading', 'tomeksaccount', 'TalkMarkets', 
'MIchaelTulenko1', 'ContraryTrader', 'jkatcher744', 'CEOofstocks', 'KeithvdKraan', 'krintas', 'ACE52weekhigh', 'ard1maloku', 'Maverick_Equity', 'skjinslover57', 'miKryptoAmigo', 'EntryIsKing', 'CryptoTalksPod', 'NickArm79144864', 'KatanaTechnique', 'StockPop1', 
'SFKairi', 'KosmosNFT35', 'miroslavpitak', 'SpookyDeGenaro', 'stockkiddo', 'cryptovk27', 'SupraFast7159', 'positivelikesp1', 'Rocknez_Monstah', 'Theblockvlog', 'DontSendf59kuE', 'PlutoisKing', 'churiwalvikram', 'PerennialRisk', 'awakensoulslove', 'palonakatrades', 
'TwitrWhackoNoMo', 'JackkTUK', 'm4markets_Group', 'IKuramasaki', 'STOCKACTIVATION', 'CMackMost', 'KolenkoArtem', 'jackneels', 'Sankristweets', 'askconradzen', 'Jack_Hons', 'Jack_at_joat', 'US_STOCK_LOVE', 'knightinprofitt', 'kurtulus_topcu', 'shidoitsuka04', 
'perincek_can', 'raymonschalken', 'Kuvera_In', '_CalebK', 'Brockhodl', 'stevekotsis13', 'BlockchainFies2', 'fekdaoui', 'traderfromkit', 'JeredKing', 'WhaleCoinTalk', 'nickboneworld', 'YokozaMD', 'MaskedTradeRick', 'ankush0317', 'Coin_Pick_Giant', 'timothy_musick', 
'forexweeklywo', 'mrstocky', 'Stocks_InColors', 'ghostsquawk', 'Stock_Waver', 'kingdom_pips', 'market_advi', 'Wealthykingdom', 'Petko02654873', 'Trader_Pheneck', 'SchoolHardStock', 'TakeiteasyTrade', 'marketobserved', 'mayankmalik7', '_ParkTF', 'LocusTrading', 
'TheoMikkelsen', 'CryptoStocks14'],
['kuaileangery', 'The_Skippy', 'Stokalarts', 'UKmetaverseuk', 'GO_Markets', 'ev_tech_stocks', 'KStapes561', 'NickScalps', 'toto21k', 'T_stock94', 'KakkarSpeaks', 'bangkokluoglu', 'Coins_Kid', 'niklas_zamzow', 'FractalsMarket', 'macro_meerkat', 'DarthWhiskey', 'vojtikruza', 
'SleekedFx', 'shrkyshf', 'Okudao_eth', 'IpekOzkardeskay', 'mattmusielak_', 'BigmikeMhf', 'kmmmz1', 'slyjake1', 'Nick_Bravery', 'blackbullforex', 'singh17vivek', 'trackrecorder', 'dev_ill_kin', 'WillsOutlook', 'mike_prius', 'Khankin23721094', 'kakasaahib', 'Keeninvestor1', 
'Krampa_', 'stretchmikep', 'TraderJack70', 'kaiser_inj', 'j_radicek', 'JanekKivilo', 'kody_krazy', 'DarkLightHD', 'MarketsRayon', 'marteneriksson', 'Blackgold250876', 'Crypto_Traderok', 'AkshayTrades', 'traderbonk', 'DividendCookie', 'mrmike1357', 'MirakhorHassan', 
'riskytraderJT', 'mattfromblock', 'easy_to_earn80k', 'nikhil_kapoor87', 'TargetHitRick', 'AkuraCrypto', 'AndreasKarlos', 'RKBrittingham', 'skaria26', 'BreaBearBaker', 'AmritKaalFin', 'IgorSekuloski1', 'sktrading15', 'R_NERK', 'kusalungile', '_pblanknews', 'OhmyjackEth', 
'AkashMe57802870', 'LKirschner1860', 'Kartikgupta1008', 'Mil03k', 'pikachu_crypto', 'vijayakumarvar1', 'Giokey', 'Marketrend', 'KVittas', 'Space_J0CKEY', 'pkchin888', '4F3nk', 'CrypticQuark', 'officialsalako', 'Soi_com_pk', 'KeybottheQuant', 'amrudspeak', 'Rookiegonnamak1', 
'AderintoBukola', 'StockMaster1011', 'LearnCryptoUK', 'oekXBT', 'stockvarsity11', 'RealSalluKhan', 'stocksexcel', 'lightstrike', 'Abalosky', 'YanickNFT', 'takechj', 'DegenSmoke420'],
['stock_economics', 'kakiforexcom', 'BbiKkuMi', 'KamaCapital', 'tasawar_khan', 'Ravi_Riskmgmt', 'HankyTrades', 'Twinkle399W', 'FutureCodeUK', 'kalp89771', 'closegreensykes', 'Kamikazetrejder', 'KlavsGO', 'danilisk', 'DanielHipkissTA', 'AnonymBanker', 'lckyali', 'GobbledygookFin', 
'Blackshadow077', 'DrTurk007', 'RocketBullCap', 'Pratik2358', 'StocktalkzUni', 'kephuo143', 'FoxxBlock', 'lolypink_43', 'MaaikolP', 'TiMarkets', 'FintakGlobal', 'FKaisaritis', 'pock3ttrad3r', 'itskhiaboo', '24KCrypto', 'trader_kamikaze', 'NickRokke', 'Makeabuck2', 'duke_606', 
'mibmarkets', 'AkeemJofferok', 'knox_365', 'DerekAmey', 'ssuyogk', 'ApollonKouras', '8szq0LEt0K2hq2Y', 'srbkmr_', 'Bikash2022', 'YANICKJETHA', 'KhanKiMc', 'AlyaAkram20', 'P2Psatoshinaka', 'StockGenieUSA', 'JmsMiniHulk', 'fiatmoneyisfake', 'kathylienfx', 'kings_clan69', 'JDrake45902915', 
'KelvinSCWong', 'meechdoesstocks', 'Dollstoivsky', 'StockCharts', 'phisharkk', 'PUKACharts', 'MarketsMC', 'InterKingdom', 'BurwoodBeike', 'frankblacked', 'DerekInvests', 'JP_5th_Yonkou', 'ExchangeKamva', 'ZiadElkhalil', 'tradernickfx', 'Ankitsood100', 'kazonomics', 'StackzPatt', 
'GrowthUnlocked', 'Alkhalaf777_', 'KeanOpina', 'umakanthonline', 'HomkarAshish', 'Chartslook', 'KyleHanah', 'TodAIMarketNews', 'nobakgaming', 'keerthanatf', 'market_ashram', 'dankahan83', 'kpkiwoong', 'PeterReznicek', 'TaghipourAkbar', 'ShareMarketTip8', 'Wielkieef', 'gorkemtireli', 
'MrkWatcher', 'KhizarKahloon', '0Kiwii3', 'TARGETKW', 'TarunSikka29', 'NKountouriotis', 'Kevin__Raymond', 'RankMyTrade'],
['GapFillingStonk', 'DoveHawkin', 'akalayci34', 'TradingBroskis', 'Tickmill', 'stocks_uptrend', 'rymondIncKenya', 'crypto_karnage', 'SEKTOR_FIVE', 'fomenka_', 'cloaknight87', 'Arbutexpark', 'SalesNurik', 'sohilParikh', 'GulczynskiMG', 'Hakanilyastrade', 'H33xHive', 'erikersay', 'jkath36', 
'MarketEdgeTrade', 'EarnedKnowledge', 'Lparadokss', 'kahiankahi_ajay', 'ItsAmeKaaay', 'allendekoker', 'locke4success', 'bscbinks', 'RickTradez1', 'skyy_andrew', 'Khalifa_4x', 'Yxng100k', 'noJuanbetter', 'kaalabiravaa369', 'blocktradesio', 'ilikeoptions1', 'BleuSkiddew', 'mattpck', 'MarketMaestro1',
'TamirTiko2110', 'TRADE_TALK_', 'NKantidakis', 'MilkywayTrader', 'ThinkMarkets_EN', 'LoonSike', 'TraderK_BTC', 'bekkdy_', 'lok3974esh', 'NPIRACKS', 'Chris_Alkema_', 'JackHoweCFA', 'KaranBhagtani1', 'My_Stock_Life', 'rektfren', 'chiragkb5', 'stockillerswan', 'chris__sunk', 'ClivBke', 'markangeloagu15', 
'Kenneteh2', 'srnayk', 'MatczakKarol', 'ImHardik88', 'cryptobdk', 'KLeeHSanchez', 'GoldSeekcom', 'Stockoptionsdog', 'econakbay', 'sk__be', 'Eko_prabowo2012', 'DocAkaboy', 'kamran22215', 'raadkafasi', 'JacindaKirouac6', 'CaptainJackCem_', 'v_raketa', 'EmaxKapital', 'NishRK12', 'king_pop12', 'AceStocks', 
'kohli0471', 'ThackerShaan', 'mktredline', 'DanielK_phd', 'AhmedKhald37221', 'avara_kutta', 'crypto_funded', 'JosephKaliI', 'Nisargaderki', 'BKlisarski', 'ninakolesnikov', 'sk1larchi', 'rafaeldomynck', 'Rajkumar9631', 'buttoncrycker', 'XMetablock', 'RishiSukheja', 'AarzKiyaHai', 'yeslookup', 'calledkeyy', 
'mkurkdjian'],
['PavelKo097', 'ChuckDeCarlo84', 'RJ_vdAkker', 'syamkp1', 'AzkTrades', 'PK_SendIT', 'blackflagfuture', 'YuriiDruk', 'naked_delta', 'alagstakes', 'daywalkerfromba', 'GekoYves61506', 'gold_kingozzie', 'wineeth_wicky', 'traderDirk', 'bkoszMJ', 'KalusOndrej', 'eknetwork2023', 'KRS_CF', 'traderkoray', 
'HookedOnLithium', 'thinkmarketsza', 'Thinkmarkets_AU', 'Chandorkar_M', 'wickoftrader', 'PratikGad1', 'MarketPlaysApp', 'riskypandas', 'StarkabilityH', 'Marketwizard16', 'KeskinTolga', 'GlobaltrekX', 'AndyCuckooTradi', 'MkeaneTrades', 'LukeLeslie625', 'nikeeeecryptoNL', 'KapitalDevelop', 
'MirekSztramski', '1cryptopk', 'therealbreak0ut', 'Kukotradez', 'marketmayhem_', 'BlackchenOG', 'trader_tracks', 'Iglockyy', 'kealmaar', 'LKhnhPhi1', 'JLrTk', 'Barbara_KVH', 'tawithmike', 'spx500Zak97', 'MoneyTalks90211', 'MrBuckleHead', 'Ducky_Call', '_kartikshah', 'BoeykensBull', 'K2xTrading', 
'kartk_7', 'esbi_kyu', 'MikeChallis2', 'akcakmak', 'Adams_K1', 'TradingJoker', 'ShukriGlobal', 'kuntzxbt', 'Prime_is_Back', 'aneojkee', 'CryptoKimpika', 'aquanetmarketFx', 'youcefbenterkia', 'kingsumc', 'JKK_786', 'Matematikci84', 'SykonCap', 'Zwack_Charts', 'stockbullykash', 'Nikhilns_nbr', 
'blackwidowbtc', 'GROK_EXPLAIN', 'Hekthor_07', 'ronakgala07', 'KingOfFibs', 'JamesPatriking', 'ykwykw2023', 'Minipip_UK', 'maslomonk', 'AArchStock', 'Pajkoss_', 'GerardWalker5', 'ModnyMishka', 'MaryVanAcker12', 'k_wamena', 'linked_trades', 'Shadibakr', 'TheStocksurf', '0xBalkan', 'johnhelka', 
'basicblank_', 'fokoExhibit', 'sensitivesuit'],
['ramyavellanki_', 'tukachalabi', 'KastIronTrade', 'HydrosMarkets', 'maskedTraderOIL', 'Shaheer_Shaikh_', 'AhaskaraInvest', 'khan_m_baber', 'JohnLocke_10_', 'Bonjoeokon', '_tradernickfx', 'stock_shooter08', 'MazidKh98064634', 'Kaustub62304277', 'SockTraduhh', 'stoictraderke', 'Gaurisankar131', 
'GekkoWallSt', 'AkshayS1N', 'omurakyuz611', 'k_krkarthik', 'HardKnocksTrad', 'CrypticClockWrk', 'FP_markets', 'TokenToMe08', 'thedoggwalker', 'FxDaniko', 'theWPRtrader', 'Dersonrocket', 'ThinkOutLoud86', 'Krishna_Equity', 'BlackBeardCapt', 'LewkPatout', 'PrajaySarkar', 'KB6233', '_StockLover', 
'wfkdjrgc2h_x', 'tradertilki', 'TheNachiket', 'BaxiaMarkets', 'KeSmallfat', '_The_Psyko_', 'arkcjleaf', 'ChikwanhaAllan', 'jonvelkavrh', 'Kingpincrypto12', 'ashkeyfos', 'DianeZemnickas', 'liquidsky1967', 'geekdadcr', 'partystocker', 'iAmBillieTheKid', 'nikonleto', 'BlackSharkls', 'skill06s', 
'MakePlaysTrades', 'ulkser', 'RockyMountnBear', 'KairoiAssets', '_interbank', 'CroFrancky', 'King_jaffee_', 'DamianSojka91', 'Stickybungus', 'SoclnetArchitek', 'MDstockmagic', 'kermittrader', 'Bhautik21949762', 'keeganfreemann', 'CSJeszek6718', '_MarketMonkey', 'randomstacker', 'jensblack', 
'trade_joker', 'BrookeThackray', 'Monkey_Trench', 'NexxtGenMarkets', 'markets_n_chart', 'hancocktrades', 'aakashchouhan5g', 'J_bobrik', 'OekonomRichter', 'tradingwithdrk', 'VikOpine', 'Ronmarkets', 'Fx_Chandrika', 'Trekewl', 'King_Deevee', 'rafstack', '_rcmarkets_', 'mei_rei_', 'lunchboxalerts', 
'AlexKentUK', 'SignalPullback', 'neilksethi', 'vikranth__reddy', 'pinerylakegroup', 'AakashT0711', 'ecalabro5', 'lsestockpicker'],
['akutidaktahu1', '_kevinkirk', 'cryptokingping7', 'itsthechuck', 'Kai_Charts', 'vsz01k3ogf5h', 'istalkstock', 'cdnstocktrader', 'AdvanceStockT', 'token_ventures', 'JovinSKN', 'jacharakis', 'TCTALKSYT', 'tradomica', 'uptrader', 'VolValkyrie', 'mrjackpro', 'Candelstickoff', 'TRWofmarkets', 
'sharkforex_', 'JonTalksFX', 'KaKa_VD13', 'CmC_Marketer47', 'ImBaak_', 'trqdernickfx', 'fxpipcollector', 'BlackbullAD', 'Akdnzkutay', 'JunaidKhan29900', 'alekseywave', 'techmarketcycle', 'HUGESKY852', 'MikeFairbournCS', 'cryptonikkoid', 'PjRisk', 'BlackLevin1979', 'JrBlackTrade', 'silenceisduck', 
'btcinsiderr', 'malek99__', 'SpecuVisionary', 'akayy713', 'LakshuAg', 'KiaHashemi1', '_WeeklyCharts', 'DomarkasMD', 'Zackery_SISU', '_Vivek_Malik', 'anarchokapital2', 'nakamoto_prime', 'KrystianLaskow1', 'balakoteswar', 'Sanju_Lakshya', 'mehmetsahkaraha', 'Sharketo_', 'Sam23709', 'skinnymoonhuntr', 
'FahdYK', 'jay_kamadiya', 'Louie_the_Duck', 'Shubhankan007', 'PenkeTrading', 'skywalker_nbn', 'PickleBiit', 'TKTweets_', 'KryptoOnTheMove', 'CM_ChrisAk', 'TheTradeKnack', '125kMarine', 'kenneth69171543', 'LuckyLuke369', 'TheChartKnight', 'AfterDark_999v2', 'TheWealthVriksh', 'Trader__Sosa', 'price_xbt', 
'Eruditehooman', 'Stocktrader127', 'adeleketaiwo20', 'GreekTrader90', 'TanukiTrade', 'HsgSkinnyG', 'mattiakabtc', 'Ramiknfr', 'lakhanhathi', 'NRiskNFun', 'stocks_profile', 'tncckn', 'SwingKing720', 'LiberalWokeMind', 'marketgem', 'PK_Fund', 'Lemogang_Leburu', 'ThePropDesk', 'Cr4zy_Chef', 'jfozak', 
'trend57k', 'kakrypto', 'alphastock8086', 'TAKE_PROFIT_1'],
['manki_b', 'stockmanreal', 'Sterling_maker', 'Bhavvikkakkaa', 'mannansheikh_', 'GoldhawkInvest1', 'DovahkinThuum', 'maskedtraderrai', 'Wyckoff_Insider', '0xKiriKev', 'trader_aka07', 'NutsVNKN', 'KapilBh11016088', 'TTXAIAnalyst', 'SFSFrancisco', 'OhakaV15118', 'GutShotPorkChop', 'Rymd_Li', 'subramanyakulk5', 
'optionalitie', 'MaxMilko', 'baki0i', 'Sarah_GreenOk', 'Kapi0100', 'TalkingMCI', '21teekul', 'kizzdaniel24', 'xekotrade', 'reedickuloux', 'harveyspektar', 'keplihomshi', 'PiusCrypFanatic', 'SaylorFink', 'AoTpokerplayer', 'Cookie_Calls', 'QuennarraB4', 'Quennarra15', 'talentedkid0408', 'ka_tty_9', 'kapita006', 
'KINGKOBAETH', 'coolranchkid1', 'picassodeek', 'Fukogu', 'niksak888', '1V1onlyy', 'michaeljack1946', 'QuennarraB8', 'Akshay135768', 'gem_dolphin', 'learning_sharks', 'TheKNANC', 'pykecreek', 'CryptoParodykid', 'KryptCaptain', 'kimbarry78', 'HaghighatKambiz', 'iamkomikaze', 'Thinkwell100', 'KapitanJayy', 
'SHU_RI_KENz', 'Analyst_Rashik', '0xSolKeeper', 'KMTrading_SMC', 'Hakaishin_FX', 'ovrclockedjesus', 'rakuten130511', 'silk_sammy', 'Mysterytrader11', 'maddox_darren', 'Bhavbhagwanche0', 'EPlaysxxekxxek', 'Vekido_Trade', 'shamiul293', 'AdamsAkintayo', 'cryptoblack36', 'Cryptoblack30', 'cryptoblack37', 'cryptoblack31', 
'BiohackingBasic', 'cryptoblack38', 'cryptoblack55', 'Cryptoblack42', 'cryptoblack48', 'cryptoblack46', 'Cryptoblack33', 'cryptoblack29', 'cryptoblack28', 'cryptoblack51', 'cryptoblack49', 'cryptoblack44', 'cryptoblack32', 'cryptoblack40', 'OluwaseunLokosu', 'KryptoKapt_', 'alnasr_97_7', 'VladyslavKoptev', 
'cryptoblack59', 'SakinaAbdu36311', 'Cryptoblack34'],
['cryptoblack50', 'iAmitKumar', 'make_macho_cry', 'cryptoblack52', 'Forex_expernick', 'marketwhalez', 'XVenkam', 'ThatKidNumber7', 'akila_ramses', 'Dahaky', 'Vol_Pokemon', 'nori_krienbuehl', 'skoonzoon', 'kayseeCT', 'KarlinskiD', 'borsakitaplari', 'imworkincrypto', 'MikeoTrenbolone', 'aakankshalovely', 'Blockchain1013', 
'trading_RSI', 'skubox555', 'FPGAengr', 'kurtsmock', 'fatihkhanzada', 'mkztrend', 'MERTOZKAY', 'belkhayate', 'SYNDICATE369', '333blacksea', 'fugasok', 'Crypto_Xleaks', 'sensei_kong', 'BuffaloNYMonkey', 'riskreaper001', 'ErickEliot18', 'milko52250068', 'bokemtrader', 'AlmuhandesKSA', 'OmarAlkhazraji6', 'TrendsharksLive']
]
# Set Up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# To run without opening a browser window, uncomment the following line:
# options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Initialize an empty DataFrame to store all data
all_data = []

# Counter for consecutive errors (any error type)
consecutive_errors = 0
max_consecutive_errors = 5

# Loop through each username list
for i, usernames in enumerate(usernames_list):
    print(f"Starting to scrape list {i+1} with {len(usernames)} usernames.")

    # List to store results for this batch
    data = []

    for username in usernames:
        try:
            # Open the profile page
            driver.get(f'https://x.com/{username}')
            driver.implicitly_wait(5)  # Wait for elements to load

            # Locate the follower count using XPath
            follower_count_element = driver.find_element(By.XPATH, '//a[contains(@href,"followers")]/span[1]/span[1]')
            follower_count = follower_count_element.text

            print(f'{username} has {follower_count} followers.')
            data.append([username, follower_count])

            # Reset the error counter after a successful retrieval.
            consecutive_errors = 0

        except Exception as e:
            print(f"Could not retrieve follower count for {username}: {e}")
            data.append([username, "Error"])

            # Increment the counter for every error regardless of its type.
            consecutive_errors += 1

            # If we've hit the error threshold, break the loop.
            if consecutive_errors >= max_consecutive_errors:
                print(f"Encountered {max_consecutive_errors} consecutive errors. Stopping the run for this batch.")
                break

    # Add this batch's data to the overall data list
    all_data.extend(data)

    # Save results to Excel after each list (you can adjust file naming as needed)
    df = pd.DataFrame(data, columns=["Username", "Follower Count"])
    df.to_excel(f"scraper_results_batch_{i+1}.xlsx", index=False)

    print(f"Finished scraping list {i+1}. Data saved to 'scraper_results_batch_{i+1}.xlsx'.")

    # Optional: Restart the browser every batch or after certain intervals
    driver.quit()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Close the browser after the last batch is done
driver.quit()

# Combine all data into a final DataFrame
final_df = pd.DataFrame(all_data, columns=["Username", "Follower Count"])

# Save the final DataFrame to an Excel file
final_df.to_excel("final_scraper_results.xlsx", index=False)

print("Scraping completed for all lists. Final data saved to 'final_scraper_results.xlsx'.")
