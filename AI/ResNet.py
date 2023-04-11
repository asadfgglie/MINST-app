from tensorflow.keras import layers
from tensorflow import keras


def ResNet(name: str = None):
    inputs = keras.Input(shape=(28, 28), name="img")
    block_2_output = layers.Conv1D(32, 3, activation="relu")(inputs)

    x = layers.Conv1D(32, 3, activation="relu", padding="same")(block_2_output)
    block_3_output = layers.add([x, block_2_output])

    x = layers.MaxPool1D(3)(block_3_output)
    x = layers.Flatten()(x)
    x = layers.Dense(64)(x)
    outputs = layers.Dense(10)(x)

    if name is None:
        model = keras.Model(inputs, outputs, name="ResNet")
    else:
        model = keras.Model(inputs, outputs, name=name)

    return model
