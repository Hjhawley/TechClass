        		.global fibonacci
        		.text

fibonacci:
				# write your code here
				li a1, 1 			# a1 = a
				li a2, 1 			# a2 = b
				li a3, 2 			# a3 = i
			1:	add t0, a1, a2 		# temp = a + b
				mv a1, a2			# a = b
				add a2, t0, zero 	# b = temp (+ 0)
				addi a3, a3, 1		# i += 1
				blt a3, a0, 1b		# while i < n goto 1b (a0 = n)
				mv a0, a2			# copy b to a0
				ret