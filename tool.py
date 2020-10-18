x = ['timeStamp, event	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorOwner	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	overkill	school	resisted	blocked	absorbed	critical	glancing	crushing	multistrike	environmentalType	overhealing	powerType	extraAmount	absorbGUID	absorbName	absorbFlags	absorbRaidFlags	absorbSpellId	absorbSpellName	absorbSpellSchool	missType	isOffhand	amountMissed	extraSpellId	extraSpellName	extraSchool	auraType	failedType	effect1	effect2	effect3	effect4	effect5	effect6	effect7	effect8	effect9	effect10	effect11	effect12	effect13	encounterID	encounterName	difficultyID	raidSize	endStatus	itemId	itemName	importStatus	importFailureReason	importFailureRow	importRowNumber	importFileName', 'timeStamp, event	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorOwner	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	overkill	school	resisted	blocked	absorbed	critical	glancing	crushing	multistrike', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	environmentalType	amount	overkill	school	resisted	blocked	absorbed	critical	glancing	crushing	multistrike', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	overkill	school	resisted	blocked	absorbed	critical	glancing	crushing	multistrike', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	overhealing	absorbed	critical	multistrike', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	powerType	extraAmount', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel	amount	powerType', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	resourceActor	resourceActorUnknown	hitPoints	maxHitPoints	attackPower	spellPower	resolve	resourceType	resourceAmount	maxResourceAmount	xPosition	yPosition	itemLevel', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	absorbGUID	absorbName	absorbFlags	absorbRaidFlags	absorbSpellId	absorbSpellName	absorbSpellSchool	amount	* Includes attacker ability info', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	absorbGUID	absorbName	absorbFlags	absorbRaidFlags	absorbSpellId	absorbSpellName	absorbSpellSchool	amount', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	missType	isOffhand	multistrike	amountMissed', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	missType	isOffhand	multistrike', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	extraSpellId	extraSpellName	extraSchool', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	auraType	effect1	effect2	effect3	effect4	effect5	effect6	effect7	effect8	effect9	effect10	effect11	effect12	effect13', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool	failedType', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellId	spellName	spellSchool', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags	spellName	itemId	itemName', 'timeStamp	sourceGUID	sourceName	sourceFlags	sourceRaidFlags	destGUID	destName	destFlags	destRaidFlags', 'timeStamp	encounterID	encounterName	difficultyID	raidSize	endStatus', 'timeStamp	encounterID	encounterName	difficultyID	raidSize']

trial = """event
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
ENCOUNTER_START"""
data = []
for li in x:
    a = (li.split())
    data.append(a)
import re
trial = re.findall('(?<=event\n)[_A-Z]+', trial)
print(trial)

keys = ['RANGE_DAMAGE', 'ENVIRONMENTAL_DAMAGE', 'SWING_DAMAGE', 'SPELL_PERIODIC_HEAL', 'SPELL_DRAIN', 'SPELL_PERIODIC_ENERGIZE', 'SPELL_CAST_SUCCESS', 'SPELL_ABSORBED', 'SPELL_ABSORBED', 'SPELL_MISSED', 'SWING_MISSED', 'SPELL_DISPEL', 'SPELL_INTERRUPT', 'SPELL_AURA_REMOVED_DOSE', 'SPELL_CAST_FAILED', 'SPELL_CAST_START', 'ENCHANT_APPLIED', 'UNIT_DIED', 'ENCOUNTER_END', 'ENCOUNTER_START']

print(len(keys))
print(len(data))

for key in range(0, len(keys)):
    temp = f"{keys[key].lower()} = {data[key]}"
    print(temp)