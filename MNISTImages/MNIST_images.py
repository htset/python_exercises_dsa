import random
import math

class Image:
    def __init__(self, data, id):
        self.data = data[:]
        self.id = id

    def print_image(self):
        for i in range(len(self.data)):
            if self.data[i] == 0:
                print(" ", end="")
            else:
                print("*", end="")
            if (i + 1) % 28 == 0:
                print()

    def euclidean_distance(self, img):
        distance = 0.0
        for i in range(len(self.data)):
            distance += (self.data[i] - img.data[i]) ** 2
        return math.sqrt(distance)

if __name__ == "__main__":
    images = []

    try:
        with open("input.dat", "rb") as file:
            #Skip the metadata at the beginning of the file
            file.seek(16)

            count = 0
            while True:
                pixels = file.read(784)
                if len(pixels) == 0:
                    break
                images.append(Image(list(pixels), count))
                count += 1

    except IOError as e:
        print(e)

    print("Total images:", len(images))

    #Example: Find the closest image to a randomly selected image
    #Seed the random number generator
    rand = random.Random()

    #Generate a random index within the range of the list length
    random_index = rand.randint(0, len(images) - 1)
    print("Random index:", random_index)

    random_image = images[random_index]
    random_image.print_image()

    closest_image = None
    min_distance = float('inf')
    min_index = 0

    for i in range(len(images)):
        distance = random_image.euclidean_distance(images[i])
        if distance != 0 and distance < min_distance:
            min_distance = distance
            min_index = i
            closest_image = images[i]

    #Output the label of the closest image
    print("\nClosest image (distance={}, "
          "index={})\n".format(min_distance, min_index))

    #Print closest image
    if closest_image:
        closest_image.print_image()