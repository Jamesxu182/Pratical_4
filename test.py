#!/usr/bin/python3

from multiprocessing import Queue
from passlib.hash import argon2
from threading import Thread
from asyncio import QueueEmpty

class CrackThread (Thread):
    def __init__(self, task_queue, output_queue, password_lines):
        Thread.__init__(self)
        self.task_queue = task_queue
        self.output_queue = output_queue;

    def run(self):
        while True:
            try:
                task = task_queue.get_onwait()
            except Empty:
                break

            print(task)

            for password_line in password_lines:
                guess = password_line.strip('\n')

                hashed_guess = argon2.hash(guess)
                # print(hashed_guess)
                if(argon2_hash == hashed_guess):
                    print(argon2_hash, ':', guess)
                    output_queue.put(argon2_hash, ':', guess)
                    break

if __name__ == '__main__':

    task_queue = Queue()
    output_queue = Queue()

    with open('test.hashes') as argon2_file:
        argon2_hash_lines = argon2_file.readlines()

    with open('test-wordlist') as wordlist_file:
        password_lines = wordlist_file.readlines()

    for argon2_hash_line in argon2_hash_lines:
        argon2_hash = argon2_hash_line.strip('\n')
        task_queue.put(argon2_hash)

    argon2_file.close();
    wordlist_file.close();

    for i in range(8):
        CrackThread(task_queue, output_queue, password_lines).start()

    # with open("argon2.broken", "a") as broken_file:
    #     while True:
    #         broken_file.write(output_queue.get(), '\n')

    # broken_file.close()
