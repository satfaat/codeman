# get my number game
# written by: Faat

puts "Welcome to 'Get my number!'"
print "What's your name? "

name = gets.chomp

puts "Welcom, #{name}!"

#Сохранение случайного числа
puts "I've got a random number between 1 and 100."
puts "Can you guess it?"

target = rand(100)+1
# Отслеживание количества попыток
num_guesses = 0

guessed_it = false #Признак продолжения игры

until num_guesses == 10 || guessed_it

  puts "You've got #{10 - num_guesses} guesses left."
  print "Make a guess: "
  guess = gets.to_i

  num_guesses += 1

  #Сравнение введеного числа с загаданым
  if guess < target
    puts "Oops. Your guess was LOW."
  elsif guess > target
    puts "Oops. Your guess was HIGH"
  elsif guess == target
    puts "Good job, #{name}!"
    puts "You guessed my number in #{num_guesses} guesses!"
    guessed_it = true
  end
end

#Если попвток не осталось, сообщить загаданное число.
unless guessed_it
  puts "Sorry. You didn't get my number. (It was #{target}.)"
end


