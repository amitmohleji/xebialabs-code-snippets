<#-- This function recursively digs the values of variables exposed for use in script -->
<#function dig obj level depth captureMethod>
	<#assign result =[] >
	<#assign result = result + ["Complex Object: " + obj] >
	<#assign prefix=".vars.${obj}" >
	<#if prefix?eval?is_hash_ex >
		<#list prefix?eval?keys as key>
			<#assign basevar="${obj}.${key}" >
			<#attempt>
				<#assign valuevar="${basevar}"?eval >
				<#if valuevar?is_method >
					<#if captureMethod >
						<#assign result = result + [r"METHOD: ${" + basevar + r"(...)}"] >
					</#if>
				<#else>
					<#if valuevar?is_string || valuevar?is_boolean || valuevar?is_number>
						<#assign result = result + [r"PROPERTY: ${" + basevar + r"}  ||  VALUE: " + valuevar?string] >
					</#if>
					<#if valuevar?is_hash_ex >
						<#if level < depth >
							<#assign result = result + dig(basevar,level + 1,depth, captureMethod) > 
						</#if>			  				 
					</#if>
				</#if>
			<#recover>
				<#assign result = result + [r"PROPERTY: ${" + basevar + r"}  ||  VALUE: (UNDEFINED/UNRESOLVED) "]>
			</#attempt>
		</#list>
	<#else>
		<#assign result = result + [" Cannot be parsed as {" + obj + "} is not a hash or simple property"] >
	</#if>

	<#return result>
</#function>

<#-- Macro initiates variable digging and then prints them -->
<#macro variableList depth captureMethod>
	<#assign result=[]>
	<#list .data_model?keys as keyouter>
		<#assign result = result + dig(keyouter, 0, depth, captureMethod)> 
	</#list>
VARIABLE LISTING TILL DEPTH: ${depth}
=====================================
	<#list result as item>
		${item}
	</#list>
</#macro> 

<#-- Specify the depth till which to explore -->
<@variableList depth=0 captureMethod=false/>