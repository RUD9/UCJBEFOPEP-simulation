def main():
    simulation_thread = threading.Thread(target=process_simulation)
    simulation_thread.start()
    simulation_thread.join()
