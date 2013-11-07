import sys

def setup(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'action_burn', 50)
	core.skillModService.addSkillMod(actor, 'glancing_blow_vulnerable', 30)
	return
	
def removeBuff(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'action_burn', 50)
	core.skillModService.deductSkillMod(actor, 'glancing_blow_vulnerable', 30)
	return