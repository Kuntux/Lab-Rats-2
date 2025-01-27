init 0 python:
    #### UNIFORM POLICY SECTION ####
    uniform_policies_list = []

    def reset_invalid_uniforms(uniform_disobedience_priority): #Called by all uniform policies to clear newly inappropriate planned uniforms.
        slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
        for employee in mc.business.get_employee_list():
            if employee.planned_uniform:
                if employee.planned_uniform.slut_requirement > slut_limit and employee.planned_uniform.slut_requirement > employee.effective_sluttiness():
                    employee.planned_uniform = None
                    employee.apply_outfit()
        return

    def strict_uniform_policy_requirement(): #
        return True

    strict_uniform_policy = Policy(name = "Strict Corporate Uniforms",
        desc = "Requiring certain styles of attire in the business world is nothing new. Allows you to designate overwear sets of sluttiness 5 or less as part of your business uniform.",
        cost = 500,
        toggleable = True,
        requirement = strict_uniform_policy_requirement,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        extra_arguments = {"uniform_disobedience_priority":0}) #Uniform disobedience is only run once, regardless of how many policies are running. The highest priority uniform function is run.


    uniform_policies_list.append(strict_uniform_policy)

    def relaxed_uniform_policy_requirement():
        if strict_uniform_policy.is_owned():
            return True
        else:
            return False

    relaxed_uniform_policy = Policy(name = "Relaxed Corporate Uniforms",
        desc = "Corporate dress code is broadened to include more casual apparel. You can designate overwear sets up to sluttiness 15 as part of your business uniform.",
        cost = 1000,
        toggleable = True,
        requirement = relaxed_uniform_policy_requirement,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = strict_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":1})

    uniform_policies_list.append(relaxed_uniform_policy)

    def casual_uniform_policy_requirement():
        if relaxed_uniform_policy.is_owned():
            return True
        else:
            return False

    casual_uniform_policy = Policy(name = "Casual Corporate Uniforms",
        desc = "Corporate dress code is broadened even further. Overwear sets up to 25 sluttiness are now valid uniforms.",
        cost = 2000,
        toggleable = True,
        requirement = casual_uniform_policy_requirement,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = relaxed_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":2})

    uniform_policies_list.append(casual_uniform_policy)

    def reduced_coverage_uniform_policy_requirment():
        if casual_uniform_policy.is_owned():
            return True
        else:
            return False

    reduced_coverage_uniform_policy = Policy(name = "Reduced Coverage Corporate Uniforms",
        desc = "The term \"appropriate coverage\" in the employee manual is redefined and subject to employer approval. You can now use full outfits or underwear sets as part of your corporate uniform. Underwear sets must have a sluttiness score of 10 or less, outfits to 40 or less.",
        cost = 5000,
        toggleable = True,
        requirement = reduced_coverage_uniform_policy_requirment,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = casual_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":3})

    uniform_policies_list.append(reduced_coverage_uniform_policy)

    def minimal_coverage_uniform_policy_requirement():
        if reduced_coverage_uniform_policy.is_owned():
            return True
        else:
            return False

    minimal_coverage_uniform_policy = Policy(name = "Minimal Coverage Corporate Uniforms",
        desc = "Corporate dress code is broadened further. Uniforms must now only meet a \"minumum coverage\" requirement, generally nothing more than a set of bra and panties. Full uniforms can have a sluttiness score of 60, underwear sets can go up to 15.",
        cost = 10000,
        toggleable = True,
        requirement = minimal_coverage_uniform_policy_requirement,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = reduced_coverage_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":4})

    uniform_policies_list.append(minimal_coverage_uniform_policy)

    def corporate_enforced_nudity_requirement():
        if minimal_coverage_uniform_policy.is_owned():
            return True
        else:
            return False

    corporate_enforced_nudity_policy = Policy(name = "Corporate Enforced Nudity",
        desc = "Corporate dress code is removed in favour of a \"need to wear\" system. All clothing items that are deemed non-essential are subject to employer approval. Conveniently, all clothing is deemed non-essential. Full outfit sluttiness is limited to 80 or less, underwear sets have no limit.",
        cost = 25000,
        toggleable = True,
        requirement = corporate_enforced_nudity_requirement,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = minimal_coverage_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":5})

    uniform_policies_list.append(corporate_enforced_nudity_policy)

    def maximal_arousal_uniform_policy_requirement():
        if corporate_enforced_nudity_policy.is_owned():
            return True
        else:
            return False

    maximal_arousal_uniform_policy = Policy(name = "Maximal Arousal Uniform Policy",
        desc = "Visually stimulating uniforms are deemed essential to the workplace. Any and all clothing items and accessories are allowed, uniform sluttiness is uncapped.",
        cost = 50000,
        toggleable = True,
        requirement = maximal_arousal_uniform_policy_requirement,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = corporate_enforced_nudity_policy,
        extra_arguments = {"uniform_disobedience_priority":6})

    uniform_policies_list.append(maximal_arousal_uniform_policy)

    def male_focused_marketing_requirement():
        if strict_uniform_policy.is_owned():
            return True
        else:
            return False

    male_focused_marketing_policy = Policy(name = "Male Focused Modeling",
        desc = "The adage \"Sex Sells\" is especially true when selling your serum to men. Serum will sell for +1% per point of sluttiness of your marketing uniform.",
        cost = 500,
        toggleable = True,
        requirement = male_focused_marketing_requirement,
        dependant_policies = strict_uniform_policy)

    uniform_policies_list.append(male_focused_marketing_policy)
