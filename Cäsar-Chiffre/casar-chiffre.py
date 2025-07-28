import sys

def encode_text(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - ascii_offset + key) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def string_histogram(text):
    histogram = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            histogram[char_lower] = histogram.get(char_lower, 0) + 1
    return histogram

def frequencies(histogram):
    chars = sum(histogram.values())
    frequency = []
    for char in "abcdefghijklmnopqrstuvwxyz": #abc lol
        freq = histogram.get(char, 0) / chars if chars > 0 else 0
        frequency.append(freq)
    return frequency

def chi_square(expected, observed):
    chi2 = 0
    for i in range(26):
        if expected[i] > 0:
            chi2+= ((observed[i] - expected[i]) ** 2) / expected[i]
        elif observed[i] > 0:
            chi2+= 1000000
    return chi2

def crack_ceasar(exampletext, encrypted_text):
    example_histogram = string_histogram(exampletext)
    example_frequencies = frequencies(example_histogram)
    min_chi_square = float("inf")
    best_key = 0
    decrypted_text = ""
    for key in range(26):
        current_text = encode_text(encrypted_text, -key)
        decrypted_histogram = string_histogram(current_text)
        decrypted_frequencies = frequencies(decrypted_histogram)
        chi_square_value = chi_square(example_frequencies, decrypted_frequencies)
        if chi_square_value < min_chi_square:
            min_chi_square = chi_square_value
            best_key = key
            decrypted_text = current_text
    print(f"Best key: {best_key}")
    print(f"Chisquare: {min_chi_square:.4f}")
    return decrypted_text

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Provide text and key.")
        sys.exit(1)

    text_to_process = sys.argv[1]

    try:
        key = int(sys.argv[2])
        encoded_result = encode_text(text_to_process, key)
        print(f"original text: {text_to_process}")
        print(f"key: {key}")
        print(f"encoded text: {encoded_result}")
    except ValueError:
        print("Error: Key must be an int.")
        pass

    print(f"continuing with cracking for {text_to_process}...")

    print(f"string histogram for {text_to_process}:")
    histogram_result = string_histogram(text_to_process)
    print(histogram_result)

    print(f"frequencies for {text_to_process}:")
    frequencies_result = frequencies(histogram_result)
    print(frequencies_result)

    print("cracking example texts:")
    example_text = """
    I know that virtue to be in you, Brutus, As well as I do know your outward favour. Well,
    honour is the subject of my story. I cannot tell what you and other men Think of this life; but,
    for my single self, I had as lief not be as live to be In awe of such a thing as I myself. I was
    born free as Caesar; so were you: We both have fed as well, and we can both Endure the
    winter's cold as well as he: For once, upon a raw and gusty day, The troubled Tiber chafing
    with her shores, Caesar said to me 'Darest thou, Cassius, now Leap in with me into this
    angry flood, And swim to yonder point?' Upon the word, Accoutred as I was, I plunged in
    And bade him follow; so indeed he did. The torrent roar'd, and we did buffet it With lusty
    sinews, throwing it aside And stemming it with hearts of controversy; But ere we could
    arrive the point proposed, Caesar cried 'Help me, Cassius, or I sink!' I, as Aeneas, our great
    ancestor, Did from the flames of Troy upon his shoulder The old Anchises bear, so from the
    waves of Tiber Did I the tired Caesar. And this man Is now become a god, and Cassius is A
    wretched creature and must bend his body, If Caesar carelessly but nod on him. He had a
    fever when he was in Spain, And when the fit was on him, I did mark How he did shake: 'tis
    true, this god did shake; His coward lips did from their colour fly, And that same eye whose
    bend doth awe the world Did lose his lustre: I did hear him groan: Ay, and that tongue of his
    that bade the Romans Mark him and write his speeches in their books, Alas, it cried 'Give me
    some drink, Titinius,' As a sick girl. Ye gods, it doth amaze me A man of such a feeble temper
    should So get the start of the majestic world And bear the palm alone.
    """
    encrypted_text = "Reu jf zk zj. Wfi kyzj kzdv Z nzcc cvrmv pfl: Kf-dfiifn, zw pfl gcvrjv kf jgvrb nzky dv, Z nzcc tfdv yfdv kf pfl; fi, zw pfl nzcc, Tfdv yfdv kf dv, reu Z nzcc nrzk wfi pfl."

    cracked_text = crack_ceasar(example_text, encrypted_text)
    print(f"cracked text: {cracked_text}")



