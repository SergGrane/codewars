# In this kata you have to deal with "real-life" scenarios, when Morse code transmission speed
# slightly varies throughout the message as it is sent by a non-perfect human operator.
# Also the sampling frequency may not be a multiple of the length of a typical "dot".
# For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· ·
 #                                           .... . -.--   .--- ..- -.. .
# may actually be received as follows:
#
# ;0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000
#
# As you may see, this transmission is generally accurate according to the standard, but some dots and dashes
# and pauses are a bit shorter or a bit longer than the others.
#
# Note also, that, in contrast to the previous kata, the estimated average rate (bits per dot) may not be a whole number
# – as the hypotetical transmitter is a human and doesn't know anything about the receiving side sampling rate.
#
# For example, you may sample line 10 times per second (100ms per sample), while the operator transmits so that his dots
# and short pauses are 110-170ms long. Clearly 10 samples per second is enough resolution for this speed (meaning, each
# dot and pause is reflected in the output, nothing is missed), and dots would be reflected as 1 or 11, but if you try
# to estimate rate (bits per dot), it would not be 1 or 2, it would be about (110 + 170) / 2 / 100 = 1.4. Your algorithm
# should deal with situations like this well.
#
# Also, remember that each separate message is supposed to be possibly sent by a different operator, so its rate and other
# characteristics would be different. So you have to analyze each message (i. e. test) independently, without relying on
# previous messages. On the other hand, we assume the transmission charactestics remain consistent throghout the message,
# so you have to analyze the message as a whole to make decoding right. Consistency means that if in the beginning of a
# message '11111' is a dot and '111111' is a dash, then the same is true everywhere in that message. Moreover, it also
# means '00000' is definitely a short (in-character) pause, and '000000' is a long (between-characters) pause.

bits='0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000'

print(bits.replace('11111111', '-').replace('1111111', '-').replace('111111', '-').replace('11111', '-').replace('1111', '-').replace('111', '.').replace('11', '.').replace('1', '.').replace('0000000', '  ').replace('0000', ' ').replace('0', ''))
