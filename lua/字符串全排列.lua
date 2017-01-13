function getCharAt(str, index)
	return string.sub(str, index, index)
end

function replaceChatAt(str, char, index)
	return string.sub(str, 1, index - 1).. char.. string.sub(str, index + 1)
end

function swapCharAt(str, index1, index2)
	local chara = getCharAt(str, index1)
	local charb = getCharAt(str, index2)
	str = replaceChatAt(str, charb, index1)
	str = replaceChatAt(str, chara, index2)
	return str
end

local str = "lamev"

function fullStr(str, step)
	local len = #str
	if step == len then
		print(str)
		return
	end
	for i=step,len do
		local tmpStr = swapCharAt(str, step, i)
		fullStr(tmpStr, step + 1)
	end
end

fullStr(str, 1)