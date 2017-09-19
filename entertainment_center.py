import media
import fresh_tomatoes

# create different movie objects 
machester_by_the_sea = media.Movie("Manchester by the Sea",
                                   "After the death of his older brother Joe, Lee Chandler (Casey Affleck) is shocked that Joe has made him sole guardian of his teenage nephew Patrick. Taking leave of his job as a janitor in Boston, Lee reluctantly returns to Manchester-by-the-Sea, the fishing village where his working-class family has lived for generations. There, he is forced to deal with a past that separated him from his wife, Randi (Michelle Williams), and the community where he was born and raised.",
                                   "https://upload.wikimedia.org/wikipedia/en/d/de/Manchester_by_the_Sea.jpg",
                                   "https://www.youtube.com/watch?v=gsVoD0pTge0")

guardians_of_galaxy = media.Movie("Guardians of the Galaxy Vol. 2",
                                  "Peter Quill and his fellow Guardians are hired by a powerful alien race, the Sovereign, to protect their precious batteries from invaders. When it is discovered that Rocket has stolen the items they were sent to guard, the Sovereign dispatch their armada to search for vengeance. As the Guardians try to escape, the mystery of Peter's parentage is revealed.",
                                  "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
                                  "https://www.youtube.com/watch?v=2cv2ueYnKjg")

kungfu_hustle = media.Movie("Kung Fu Hustle",
                            "When the hapless Sing (Stephen Chow) and his dim-witted pal, Bone (Feng Xiaogang), try to scam the residents of Pig Sty Alley into thinking they're members of the dreaded Axe Gang, the real gangsters descend on this Shanghai slum to restore their fearsome reputation. What gang leader Brother Sum (Chan Kwok-kwan) doesn't know is that three legendary retired kung fu masters (Yu Xing, Dong Zhihua, Chiu Chi-ling) live anonymously in this decrepit neighborhood and don't take kindly to interlopers.",
                            "https://upload.wikimedia.org/wikipedia/en/0/00/KungFuHustleHKposter.jpg",
                            "https://www.youtube.com/watch?v=-m3IB7N_PRk")

the_wailing = media.Movie("The Wailing",
                          "Suspicion leads to hysteria when rural villagers link a series of brutal murders to the arrival of a mysterious stranger (Kunimura Jun).",
                          "https://upload.wikimedia.org/wikipedia/en/e/eb/The_Wailing_%28film%29.png",
                          "https://www.youtube.com/watch?v=43uAputjI4k")

get_out = media.Movie("Get out",
                      "Now that Chris (Daniel Kaluuya) and his girlfriend, Rose (Allison Williams), have reached the meet-the-parents milestone of dating, she invites him for a weekend getaway upstate with Missy and Dean. At first, Chris reads the family's overly accommodating behavior as nervous attempts to deal with their daughter's interracial relationship, but as the weekend progresses, a series of increasingly disturbing discoveries lead him to a truth that he never could have imagined.",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

# create a list of movies using created movie objects above
movies = [machester_by_the_sea, guardians_of_galaxy, kungfu_hustle, the_wailing, get_out]
fresh_tomatoes.open_movies_page(movies)
