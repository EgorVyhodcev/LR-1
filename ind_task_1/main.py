#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sample


if __name__ == "__main__":
    sample_string = (
         "Greetings %F% %N%! You are doing the function closure."
    )
    name, surname = input("Enter your name and surname: ").split()
    print(sample.sample(sample_string, name, surname))
