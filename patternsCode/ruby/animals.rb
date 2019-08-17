class Bird
  def talk
    puts "Chirp! Chirp!"
  end
  def move (destination)
    puts "Flying to the #{destination}."
  end
end

class Dog
  attr_accessor :name, :age

  def report_age
    puts "#{@name} is #{@age} years old."
  end

  def talk
    puts "#{@name} says Bark!"
  end
  def move(destination)
    puts "#{@name} runs to the #{destination}."
  end
end

class Cat
  def talk
    puts "Meow!"
  end
  def move(destination)
    puts "Running to the #{destination}."
  end
end

class Blender
  def close_lid
    puts"Sealed tight!"
  end
  def blend(speed)
    puts"Spinning on #{speed} setting."
  end
end

blender = Blender.new
bird = Bird.new
dog = Dog.new
cat = Cat.new

blender.close_lid
blender.blend("high")
bird.move("tree")
dog.talk
bird.talk
cat.move("house")