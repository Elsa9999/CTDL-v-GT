function print_numbers(n)
  for i in 1:n
      print("$i ")
  end
  println()
end

n = 5

@time begin
  print_numbers(n) # Chạy thuật toán
end
