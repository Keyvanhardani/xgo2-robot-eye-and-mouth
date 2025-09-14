# XGO2 Robot Eye and Mouth Animation

Open-source Python library for animating the eyes and mouth of XGO2 robots with lifelike expressions synchronized to speech and interaction.

## Features

- **Real-time Eye Tracking**: Advanced algorithms for natural eye movement and tracking
- **Mouth Animation Sync**: Precise synchronization of mouth movements with audio/speech
- **Interactive Expressions**: Dynamic facial expressions that respond to environmental inputs
- **Modular Design**: Easy integration with existing robotics projects
- **Cross-platform**: Compatible with various operating systems

## Installation

```bash
git clone https://github.com/Keyvanhardani/xgo2-robot-eye-and-mouth.git
cd xgo2-robot-eye-and-mouth
pip install -r requirements.txt
```

## Quick Start

```python
from xgo2_animation import EyeController, MouthController

# Initialize controllers
eye_controller = EyeController()
mouth_controller = MouthController()

# Start animation
eye_controller.start_tracking()
mouth_controller.sync_with_audio("speech.wav")
```

## Documentation

For detailed documentation and examples, please refer to the [Wiki](../../wiki).

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: Keyvan Hardani
- **Email**: hardani@hotmail.de
- **LinkedIn**: [keyvanhardani](https://linkedin.com/in/keyvanhardani)

## Acknowledgments

Special thanks to the robotics community for their continuous support and feedback.
