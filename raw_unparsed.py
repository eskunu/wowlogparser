events = """
event
RANGE_DAMAGE
DAMAGE_SPLIT
SPELL_DAMAGE
SPELL_PERIODIC_DAMAGE

event
ENVIRONMENTAL_DAMAGE

event
SWING_DAMAGE
SWING_DAMAGE_LANDED

event
SPELL_PERIODIC_HEAL
SPELL_HEAL

event
SPELL_DRAIN

event
SPELL_PERIODIC_ENERGIZE
SPELL_ENERGIZE

event
SPELL_CAST_SUCCESS

event
SPELL_ABSORBED

event
SPELL_ABSORBED

event
SPELL_MISSED
SPELL_PERIODIC_MISSED
RANGE_MISSED

event
SWING_MISSED

event
SPELL_DISPEL
SPELL_STOLEN
SPELL_AURA_BROKEN_SPELL

event
SPELL_INTERRUPT

event
SPELL_AURA_REMOVED_DOSE
SPELL_AURA_APPLIED_DOSE
SPELL_AURA_APPLIED
SPELL_AURA_REFRESH
SPELL_AURA_REMOVED
SPELL_AURA_BROKEN

event
SPELL_CAST_FAILED

event
SPELL_CAST_START
SPELL_SUMMON
SPELL_CREATE
SPELL_INSTAKILL
SPELL_RESURRECT

event
ENCHANT_APPLIED
ENCHANT_REMOVED

event
UNIT_DIED
PARTY_KILL
UNIT_DESTROYED

event
ENCOUNTER_END

event
ENCOUNTER_START
"""

examples = """
timeStamp, event	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorOwner	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	overkill	school	resisted	blocked	absorbed	critical	glancing	crushing	multistrike	environmentalType	overhealing	powerType	extraAmount	absorbGUID	absorbName	absorbFlags	absorbRaidFlags	absorbSpellId	absorbSpellName	absorbSpellSchool	missType	isOffhand	amountMissed	extraSpellId	extraSpellName	extraSchool	auraType	failedType	effect1	effect2	effect3	effect4	effect5	effect6	effect7	effect8	effect9	effect10	effect11	effect12	effect13	encounterID	encounterName	difficultyID	raidSize	endStatus	itemId	itemName	importStatus	importFailureReason	importFailureRow	importRowNumber	importFileName
0,1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79
																																																																														
0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34																																												
																																																																														
timeStamp, event	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorOwner	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	overkill	school	resisted	blocked	absorbed	critical	glancing	crushing	multistrike																																												
2/26 20:16:09.478 RANGE_DAMAGE	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	Creature-0-3136-1448-8600-91331-0000510129	Archimonde	0x10a48	0x0	75	Auto Shot	0x1	Creature-0-3136-1448-8600-91331-0000510129	0	460880850	464132384	0	0	0	0	7339815	7339815	4067.7	-2258.62	103	14557	-1	1	0	0	0	nil	nil	nil	nil																																												
2/28 20:12:22.057 DAMAGE_SPLIT	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x20514	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	6940	Hand of Sacrifice	0x2	Player-XXXX-XXXXXXXX	0	621000	621000	13631	1097	23489	0	32000	32000	4069.32	-2224.72	739	0	-1	1	0	0	2143	nil	nil	nil	nil																																												
2/23 19:13:24.736 SPELL_DAMAGE	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Vehicle-0-3136-967-4962-56167-00004D03B1	Arm Tentacle	0x10a48	0x0	101423	Seal of Righteousness	0x2	Vehicle-0-3136-967-4962-56167-00004D03B1	0	6269183	6447772	0	0	0	1	0	0	-12065.03	12127.18	88	37191	-1	2	0	0	0	1	nil	nil	nil																																												
2/26 20:03:37.961 SPELL_PERIODIC_DAMAGE	0	nil	0x514	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	188796	Fel Corruption	0x4	Player-XXXX-XXXXXXXX	0	447840	506940	7196	1097	0	0	32000	32000	4114	-2154.26	738	59100	-1	4	0	0	0	nil	nil	nil	nil																																												
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	environmentalType	amount	overkill	school	resisted	blocked	absorbed	critical	glancing	crushing	multistrike																																														
2/27 17:45:50.900 ENVIRONMENTAL_DAMAGE	0	nil	0x80000000	0x80000000	Player-XXXX-XXXXXXXX	Offensive-Mal'Ganis	0x512	0x0	Player-XXXX-XXXXXXXX	0	434648	483480	7512	892	0	2	120	120	3882.87	-395.88	729	Lava	48832	0	4	0	0	0	nil	nil	nil	nil																																														
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	overkill	school	resisted	blocked	absorbed	critical	glancing	crushing	multistrike																																															
2/23 19:13:24.711 SWING_DAMAGE	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Vehicle-0-3136-967-4962-56167-00004D03B1	Arm Tentacle	0x10a48	0x0	Player-XXXX-XXXXXXXX	0	677448	677448	10614	1097	0	0	29760	32000	-12088.45	12157.75	737	141398	-1	1	0	0	0	nil	nil	nil	nil																																															
2/23 19:13:24.711 SWING_DAMAGE_LANDED	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Vehicle-0-3136-967-4962-56167-00004D03B1	Arm Tentacle	0x10a48	0x0	Vehicle-0-3136-967-4962-56167-00004D03B1	0	6306374	6447772	0	0	0	1	0	0	-12065.03	12127.18	88	141398	-1	1	0	0	0	nil	nil	nil	nil																																															
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	overhealing	absorbed	critical	multistrike																																																	
2/26 20:03:09.594 SPELL_PERIODIC_HEAL	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x512	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	188550	Lifebloom	0x8	Player-XXXX-XXXXXXXX	0	663540	663540	10036	1089	0	3	100	100	4099.19	-2154.03	732	3953	3953	0	nil	nil																																																	
2/23 19:13:24.872 SPELL_HEAL	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	143924	Leech	0x1	Player-XXXX-XXXXXXXX	0	677448	677448	12493	1097	0	0	29760	32000	-12088.45	12157.75	737	6532	6532	0	nil	nil																																																	
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	powerType	extraAmount																																																			
2/27 16:55:51.777 SPELL_DRAIN	Creature-0-3020-1448-6608-90018-0000D2245C	Hellfire Cannon	0xa18	0x0	Creature-0-3020-1448-6608-90018-0000D2245C	Hellfire Cannon	0xa18	0x0	185042	Hellfire Round	0x1	Creature-0-3020-1448-6608-90018-0000D2245C	0	10832800	10832800	0	0	0	3	40	100	4046.91	-765.84	103	10	3	0																																																			
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	powerType																																																				
2/26 20:07:50.245 SPELL_PERIODIC_ENERGIZE	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	12051	Evocation	0x40	Player-XXXX-XXXXXXXX	0	503640	503640	0	9417	0	0	72966	160000	4046.94	-2185.39	737	48888	0																																																				
2/23 19:13:25.586 SPELL_ENERGIZE	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	98057	Grand Crusader	0x1	Player-XXXX-XXXXXXXX	0	677448	677448	12493	1097	0	0	27653	32000	-12085.42	12157.48	737	1	9																																																				
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel																																																						
2/23 19:13:24.549 SPELL_CAST_SUCCESS	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Vehicle-0-3136-967-4962-56167-00004D03B1	Arm Tentacle	0x10a48	0x0	31935	Avenger's Shield	0x2	Player-XXXX-XXXXXXXX	0	677448	677448	10614	1097	0	0	32000	32000	-12088.45	12157.75	737																																																						
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	absorbGUID	absorbName	absorbFlags	absorbRaidFlags	absorbSpellId	absorbSpellName	absorbSpellSchool	amount
2/27 17:46:42.043 SPELL_ABSORBED	Player-9-0A0F5C66	XXXXXXXXXXX-Hyjal	0x514	0x0	Creature-0-3020-1448-6608-92913-000052245C	Gorebound Berserker	0xa48	0x0	115687	Jab	0x1	Player-9-0A0F5C66	Agilablanca-Kil'jaeden	0x514	0x0	184553	Spirit Shift	0x20	1266																																																											
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	absorbGUID	absorbName	absorbFlags	absorbRaidFlags	absorbSpellId	absorbSpellName	absorbSpellSchool	amount
2/21 20:05:45.918 SPELL_ABSORBED	Creature-0-3022-1448-2980-95280-00004A6AE8	Kaz'rogal	0xa48	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x20514	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	17	Power Word: Shield	0x2	58995																																																														
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	missType	isOffhand	multistrike	amountMissed
2/27 17:46:41.710 SPELL_MISSED	Player-9-0A0F5C66	XXXXXXXXXXX-Hyjal	0x514	0x0	Creature-0-3020-1448-6608-92913-000052245C	Gorebound Berserker	0xa48	0x0	115687	Jab	0x1	ABSORB	nil	1	633																																																															
2/27 17:46:41.367 SPELL_PERIODIC_MISSED	Player-9-0A0F5C66	XXXXXXXXXXX-Hyjal	0x514	0x0	Creature-0-3020-1448-6608-92913-000052245C	Gorebound Berserker	0xa48	0x0	128531	Blackout Kick	0x1	ABSORB	nil	nil	1703																																																															
2/27 17:36:50.294 RANGE_MISSED	Player-58-08B1A96B	XXXXXXXXXXX-Hyjal	0x514	0x0	Creature-0-3020-1448-6608-92142-000052245C	Blademaster Jubei'thos	0xa48	0x0	75	Auto Shot	0x1	ABSORB	nil	nil	23555																																																															
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	missType	isOffhand	multistrike	amountMissed
2/23 19:13:43.417 SWING_MISSED	Creature-0-3136-967-4962-56471-00004D03BA	Mutated Corruption	0x10a48	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	PARRY	nil	nil																																																																			
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	extraSpellId	extraSpellName	extraSchool	auraType																																																															
2/27 17:37:58.263 SPELL_DISPEL	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x512	0x0	Creature-0-3020-1448-6608-92146-000052245B	Gurtogg Bloodboil	0xa48	0x0	19801	Tranquilizing Shot	0x8	184359	Fury	1	BUFF																																																															
2/27 17:24:10.367 SPELL_STOLEN	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	Creature-0-3020-1448-6608-94894-000052245B	Keen-Eyed Gronnstalker	0xa48	0x0	30449	Spellsteal	0x40	139	Renew	2	BUFF																																																															
2/27 17:39:40.210 SPELL_AURA_BROKEN_SPELL	Creature-0-3020-1448-6608-92041-000052245C	Bleeding Darkcaster	0xa48	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x512	0x0	546	Water Walking	0x8	182705	Fel Barrage	4	BUFF																																																															
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	extraSpellId	extraSpellName	extraSchool																																																																
2/27 17:37:47.589 SPELL_INTERRUPT	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x40511	0x0	Creature-0-3020-1448-6608-92144-000052245B	Dia Darkwhisper	0x10a48	0x0	31935	Avenger's Shield	0x2	184675	Void Bolt	32																																																																
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	auraType	effect1	effect2	effect3	effect4	effect5	effect6	effect7	effect8	effect9	effect10	effect11	effect12	effect13
2/26 20:07:38.217 SPELL_AURA_REMOVED_DOSE	0	nil	0x4228	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	159675	Mark of Warsong	0x10	BUFF	9	40																																																																
2/23 19:13:28.482 SPELL_AURA_APPLIED_DOSE	Vehicle-0-3136-967-4962-56167-00004D03B1	Arm Tentacle	0x10a48	0x0	Vehicle-0-3136-967-4962-56167-00004D03B1	Arm Tentacle	0x10a48	0x0	105401	Burning Blood	0x4	BUFF	38																																																																	
2/21 20:06:16.856 SPELL_AURA_APPLIED	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	1454	Life Tap	0x20	DEBUFF	0	0	80586																																																															
2/21 20:05:45.918 SPELL_AURA_REFRESH	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x20514	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x20514	0x0	115069	Stance of the Sturdy Ox	0x1	BUFF	0	25	0	-15	25	900	-6	0	0	-500	3	0	125																																																					
2/23 19:13:25.586 SPELL_AURA_REMOVED	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	85416	Grand Crusader	0x1	BUFF	9	40																																																																
2/26 21:21:44.821 SPELL_AURA_BROKEN	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Vehicle-0-3136-1448-8600-94412-0000511644	Infernal Doombringer	0x10a48	0x2	91807	Shambling Rush	0x1	DEBUFF	38																																																																	
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	failedType																																																																		
2/23 19:13:24.606 SPELL_CAST_FAILED	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	0	nil	0x80000000	0x80000000	35395	Crusader Strike	0x1	Not yet recovered																																																																		
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool																																																																			
2/23 19:13:28.781 SPELL_CAST_START	Creature-0-3136-967-4962-56102-00004D0360	Nozdormu	0xa18	0x0	0	nil	0x80000000	0x80000000	105799	Time Zone	0x1																																																																			
2/26 19:59:45.779 SPELL_SUMMON	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x512	0x0	Creature-0-3136-1448-8600-77789-0000510311	Blingtron 5000	0xa28	0x0	161414	Blingtron 5000	0x1																																																																			
2/26 20:01:17.192 SPELL_CREATE	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	GameObject-0-3136-1448-8600-194108-000051036D	Summoning Portal	0x4228	0x0	698	Ritual of Summoning	0x20																																																																			
2/26 20:05:00.442 SPELL_INSTAKILL	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x514	0x0	Pet-0-3136-1448-8600-1860-0101DFEA52	Ormtast	0x1114	0x0	108503	Grimoire of Sacrifice	0x20																																																																			
2/26 20:23:53.838 SPELL_RESURRECT	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x512	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	20484	Rebirth	0x8																																																																			
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellName	itemId	itemName																																																																			
1/17 21:01:52.804 ENCHANT_APPLIED	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	+50 Haste	124204	Mannoroth's Calcified Eye																																																																			
																																																																														
																																																																														
timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags																																																																						
2/23 19:13:33.370 UNIT_DIED	0	nil	0x80000000	0x80000000	Vehicle-0-3136-967-4962-56167-00004D03B1	Arm Tentacle	0x10a48	0x0																																																																						
2/23 19:13:33.179 PARTY_KILL	Player-XXXX-XXXXXXXX	XXXXXXXXXXX-Hyjal	0x511	0x0	Vehicle-0-3136-967-4962-56167-00004D03B1	Arm Tentacle	0x10a48	0x0																																																																						
2/26 20:07:51.304 UNIT_DESTROYED	0	nil	0x80000000	0x80000000	Creature-0-3136-1448-8600-59764-00005104ED	Healing Tide Totem	0x2114	0x0																																																																						
																																																																														
timeStamp	encounterID	encounterName	difficultyID	raidSize	endStatus																																																																									
2/23 19:15:33.989 ENCOUNTER_END	1299	Madness of Deathwing	4	25	1																																																																									
																																																																														
timeStamp	encounterID	encounterName	difficultyID	raidSize																																																																										
2/26 20:16:06.337 ENCOUNTER_START	1799	Archimonde	16	20																																																																										
"""