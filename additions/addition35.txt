def process_simulation():
    while True:
        time.sleep(0.1)
        with open('config_filename2.json', 'r') as config_file:
            if json.load(config_file) == "1":
                with open('config_filename2.json', 'w') as config_file:
                    json.dump('0', config_file)
                break
    photon_sim = PhotonSimulation()
    photon_sim.simulate_interaction()
    spdc_sim = SPDCSimulation()
    down_conversion_result = spdc_sim.simulate_down_conversion()
    polarization_result, entangled_state = spdc_sim.simulate_spdc_type_ii()
    while True:
        time.sleep(0.1)
        with open('config_filename2.json', 'r') as config_file:
            if json.load(config_file) == "1":
                with open('config_filename2.json', 'w') as config_file:
                    json.dump('0', config_file)
                break
    print_simulation_results(down_conversion_result, polarization_result)
    save_polarization_data(polarization_result)

