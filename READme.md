# Custom Pseudorandom Number Generator (PRNG) Analysis

## Overview
এই প্রজেক্টে একটি সরল Pseudorandom Number Generator (PRNG) তৈরি করা হয়েছে, যা Linear Congruential Generator (LCG) পদ্ধতি অনুসরণ করে।  
এই PRNG থেকে সংখ্যা জেনারেট করে আমরা তাদের ইউনিফর্মিটি (সমান বণ্টন) এবং ডিপেন্ডেন্সি (পরপর সংখ্যার সম্পর্ক) বিশ্লেষণ করেছি।

## Features
- Seed ব্যবহার করে নির্দিষ্ট পদ্ধতিতে সংখ্যা তৈরি করা
- Histogram প্লট দ্বারা সংখ্যাগুলোর ইউনিফর্মিটি চেক করা
- Scatter প্লট দ্বারা পরপর সংখ্যাগুলোর ডিপেন্ডেন্সি পরীক্ষা করা

## How to Run
1. Python 3.x ইনস্টল করতে হবে  
2. প্রয়োজনীয় লাইব্রেরি ইন্সটল করতে হবে:  
```bash
pip install matplotlib seaborn
