class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        # Sort processor Time in ascending order
        processorTime.sort()
        # Sort tasks in descending order
        tasks.sort(reverse=True)
        # Set the number of processors
        n = len(processorTime)
        # Initialize the max time needed to complete all tasks
        max_time = 0
        for i in range(n):
            for j in range(4):
                # Assign 4 tasks to each processor
                # The j-th task for processor i is tasks[4 * i + j]
                current_max_time = processorTime[i] + tasks[4 * i + j]
                # Update the global max_time
                max_time = max(max_time, current_max_time)
        return max_time