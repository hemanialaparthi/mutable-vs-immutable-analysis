# Mutable vs Immutable Analysis

Our All Hands project focuses on the ways that immutable and mutable objects effect our codes run time and RAM usage.

## What We Know

The difference in space overhead when appending elements to mutable collections versus immutable structures comes down to how memory allocation and object copying work.

## What We Expect

### Mutable Collections 

We know mutable collections (such as list) are able to be chnaged using an append. These append operations manage memory dynamically by distrubing extra space between what is needed. This means you can append withoout reallocating memory each time. So we can expect the mutable collecton to be more memory efficient. 

Due to this process when that space does eventually fill up, we can expect the list to resize by distrubuting a larger block of memory. This process would include copying the existing elements to the new memory block. Since it doesn't have to resize each time we can also expect it to take less time.

### Immutable Collections

We know that immutable structures (such as tuples) do not support appends. Meaning we must use a "+=" to create a whole new object thst contains both the original and the appended elements. 

However, because we allocate memory for the entire sequence and copy all elements of the coefficient we can expect a higher memory cost since we must allocate a new memory block each time. We can expect that the time it would take would vary based on how long and short the tuple is.

