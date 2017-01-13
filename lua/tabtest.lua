function print_t(t)
    for i=1,#t do
    	print(i, t[i])
    end
end

t={1,2,3,4,5}

print_t(t)
print('--------------------')

table.remove(t, 1)
-- t[1]=nil
print_t(t)