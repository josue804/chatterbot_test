require 'pry'

puts "Here we go\n\n"

while(1) do
  result = system("./pickle.py josue")

  puts "\n\n******FULL CONVERSATION*******\n"
  File.open('josue-robot1', 'r') do |f|
    f.each_line do |line|
      puts line
    end
  end
end
