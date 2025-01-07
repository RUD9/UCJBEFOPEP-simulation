def plot_energy_dynamics(self):
    plt.figure(figsize=(10, 6))
    for label, data in self.energy_history.items():
        plt.plot(data, label=f'{label} фотон')
    plt.title('Динамика энергии фотонов')
    plt.xlabel('Время')
    plt.ylabel('Энергия (Дж)')
    plt.legend()
    plt.show()
#Создает график энергетической динамики фотонов.

