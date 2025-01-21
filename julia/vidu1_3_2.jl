function printPairs(n)
    for i in 1:n
        for j in 1:n
            print("($i, $j) ")
        end
    end
    println()
end

n = 3 # Số lượng phần tử

@time printPairs(n) # Đo thời gian thực thi
