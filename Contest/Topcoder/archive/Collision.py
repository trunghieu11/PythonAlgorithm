class Collision:
    def probability(self, assignments, ids):
        no_mem_answer = 1.0
        assigned_id = 0
        for x in range(sum(assignments)):
            no_mem_answer *= max(float(ids - assigned_id), 0.0) / ids
            assigned_id += 1

        have_mem_answer = 1.0
        assigned_id = assignments[0]
        for x in assignments[1:]:
            for i in range(x):
                if ids - i > 0:
                    have_mem_answer *= max(float(ids - assigned_id - i), 0.0) / (ids - i)
            assigned_id += x

        return abs(no_mem_answer - have_mem_answer)


if __name__ == '__main__':
    solver = Collision()
    answer = solver.probability((20, 20), 1000)
    print(answer)