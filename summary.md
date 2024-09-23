1. Why did you choose the tools, libraries, and language you used for the coding exercise?

Python is the language I am the most familiar with.

To my understanding Fetch uses Django, but Django is overkill for a simple exercise like this. Flask is a lightweight framework that works better in this situation.

2. What are the advantages and disadvantages of your solution?

Advantages:

Memory Efficient - Each transaction that is fully spent is removed from memory

Simple - My entire solution fits in one file

Disadvantages:

Volatile - All data is lost after the system turns off because there is no persistent database

Inelastic - All data is stored in each machine's memory. To create a distributed system that could handle more traffic, I would want to use a transactional database that multiple web servers would interact with.

3. What has been a favorite school/personal project thus far? What about it that challenged you?

My graduate distributed systems class used [DSLabs](https://ellismichael.com/dslabs/) for our class projects. Their automated model checking testing suite helped me understand how difficult it is to implement a distributed systems protocol such as Paxos in a completely error free way. I found it really enjoyable to have to dig really deep into a system to make sure every little detail was correct.