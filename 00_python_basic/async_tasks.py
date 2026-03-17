"""Simple Asyncio program"""
import asyncio

async def task(name, delay):
    """Simulate a task with a given name and delay."""
    for i in range(3):
        print(f"{name} working {i}")
        await asyncio.sleep(delay)

async def main():
    """Main function to run the async tasks."""
    await asyncio.gather(
        task("Order", 1),
        task("Serve", 2)
    )

asyncio.run(main())
