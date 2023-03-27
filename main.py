# python3
class Query:
    _multiplier = 263
    _prime = 1000003
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
            return ans % self.bucket_count 

    def add (self,string, string2):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + [string2] + bucket
        else:
            for i in range(0,len(bucket)-1,2):
                if bucket[i] == string:
                    bucket[i+1] = string2


    def delete(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range (len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                bucket.pop(i)
                break
    def find(self, string):
        hashed = self._hash_func(string)
        bucket  = self.buckets[hashed]
        for i in range(0,len(bucket)-1,2):
            if bucket[i] == string:
                return bucket[i + 1]
        return "not found"

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    for cur_query in queries:
        t = list(cur_query.split())
        if t[0] == 'add':
           contacts.add(t[1],t[2])
        elif t[0] == 'del':
            contacts.delete(t[1])
        elif t[0] == 'find':
            result.append(contacts.find(t[1]))
    return result

if __name__ == '__main__':
    n = int(input())
    contacts = Query(n)
    write_responses(process_queries([input() for i in range(n)]))

