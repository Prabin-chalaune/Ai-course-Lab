#Q(1). Print all subsets if there is at least one subset of set[]
# with a sum equal to the given sum

flag = False

def printSubset_sum(i, n, _set, target_sum, subset):
	global flag  # to check if at least one valid subset has been found.

	if target_sum == 0:  # If targetSum is zero, then there exists a subset
		flag = True
		print("[", end=" ")  # Prints valid subset
		for element in subset:
			print(element, end=" ")
		print("]", end=" ")
		return

	if i == n:   #end of array then return
		return


	printSubset_sum(i + 1, n, _set, target_sum, subset)    # Not considering the current element _set[i]


	if _set[i] <= target_sum:  # Consider the current element if it is less than or equal to targetSum

		subset.append(_set[i])   # Push the current element into the subset

		printSubset_sum(i + 1, n, _set, target_sum - _set[i], subset)    # Recursive call for considering the current element


		subset.pop()     # Remove the last element after recursive call to restore subset's original configuration


if __name__ == "__main__":

	set_1 = [1, 2, 1]    #Test case 1
	sum_1 = 3
	n_1 = len(set_1)
	subset_1 = []
	print("Output 1:")
	printSubset_sum(0, n_1, set_1, sum_1, subset_1)
	print()
	flag = False


	set_2 = [3, 34, 4, 12, 5, 2]   # Test case 2
	sum_2 = 30
	n_2 = len(set_2)
	subset_2 = []
	print("Output 2:")
	printSubset_sum(0, n_2, set_2, sum_2, subset_2)
	if not flag:
		print("There is no such subset")


