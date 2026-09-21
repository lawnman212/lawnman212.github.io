import os
import datetime
import random
from google import genai

# Retrieve system environment variables set in GitHub Actions Secrets
api_key = os.environ.get("GEMINI_API_KEY")
affiliate_tag = os.environ.get("AFFILIATE_TAG", "yourtag-20")

client = genai.Client(api_key=api_key)
today = datetime.date.today().strftime("%Y-%m-%d")

# Topics focused specifically on your lawn, garden, and outdoor furniture niche
topic_ideas = [
    "Commercial Grade Lawn Mowers for Residential Properties",
    "Weather-Resistant Outdoor Patio Furniture Sets",
    "Electric vs Gas String Trimmers and Edgers",
    "Core Aerators and Lawn Dethatchers for Turf Care",
    "Smart Irrigation Controllers and Hose Timers",
    "Zero-Turn Lawn Mower Attachments and Accessories",
    "Teak vs Aluminum Outdoor Dining Sets",
    "Spreader and Fertilizer Equipment for Home Lawns"
]

selected_topic = random.choice(topic_ideas)

prompt = f"""
You are an expert outdoor living and lawn care specialist who writes detailed, objective buying guides.
Write an in-depth, SEO-optimized buying guide and product review focusing on: '{selected_topic}'.

Requirements:
1. Provide a punchy Title.
2. Break down key features, build quality, and pros/cons for top product choices in this category.
3. Target homeowners who want reliable lawn equipment, lawn care tools, or outdoor furniture.
4. Include call-to-action sections with placeholder Amazon affiliate links formatted exactly like this:
   https://www.amazon.com/dp/ASIN_HERE?tag={affiliate_tag}
5. Keep the tone practical, authoritative, and helpful.

Output the response strictly as valid Jekyll Markdown front matter:
---
title: "ARTICLE TITLE HERE"
date: {today}
layout: post
categories: [Lawn Care, Outdoor Living]
---
ARTICLE CONTENT HERE
"""

# Call Gemini 2.5 Flash (Free Tier)
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

# Define the file path in the Jekyll _posts directory
filename = f"_posts/{today}-outdoor-lawn-guide.md"

os.makedirs("_posts", exist_ok=True)
with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Successfully published new guide: {filename}")
