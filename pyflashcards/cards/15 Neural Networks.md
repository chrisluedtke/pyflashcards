## q
When were neural networks first introduced?

## a
In 1943, by neurophysiologist Warren McCulloch and mathematician Walter Pitts

---

## q
When the **artificial neuron** was first developed, what was its structure?

## a
The **aritificial neuron** had one/many binary input neurons, an activation threshold, and a single binary output. These could be structured to compute complex logic.

---

## q
The **perceptron** was invented in 1957. What is its structure?

## a
A **perceptron** is a simple ANN. It is composed of a single layer of **threshold logic unit** (TLU) neurons. Each TLU receives each of the numerical inputs in addition to a **bias** term (typically 1). The TLU multiplies each input by a different **weight**, sums those products, and applies a **step function**. Common step functions include:

* The **heaviside** function: 0 if sum < 0; 1 if sum >= 0
* The **sign** function: -1 if sum < 0; 0 if sum = 0; 1 if sum > 0

---

## q
What is **gradient descent**, and how is it used in neural networks?

## a
**Gradeint descent** is a method of optimizing the weights of neural networks. By computing the derivative of each neuron's functions (activation function and weight multiplication), we **back-progagate** our predition errors to determine how errors relate to the weights of each neuron. We use this information to tweak those weights in the right direction based on a **learning rate**.

---

## q

Do the inputs to a neural network need to be normalized? Why or why not?

## a

It's not 100% necessary to normalize/scale your input data before feeding it to a neural network. The network can learn the appropriate weights to deal with data as long as it is numerically represented. However normalization is recommended as it can make training faster and reduce the chance that gradient descent gets stuck in a local optimum.

---

## q

What is a **Recurrent Neural Network**?

## a

**Recurrent Neural Networks** are loop structures that feed into themselves and receive and/or output *sequences* of data.

---

## q

What is a **Long Short Term Memory** neural network?

## a

**LSTM** models are a specialization of Recurrent Neural Networks. They generally perform better than RNNs due to their handling of backpropagation.

---
