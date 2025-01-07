def run_animation(self):
    # Создание анимации с 170 кадрами
    anim = FuncAnimation(self.fig, self.update, frames=170, interval=20)
    plt.show()

